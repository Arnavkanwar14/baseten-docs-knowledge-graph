"""Build an Obsidian knowledge-graph vault from Baseten's docs.

Downloads every page listed in https://docs.baseten.co/llms.txt (served as raw
markdown), converts internal links to [[wikilinks]], adds frontmatter + tags,
and generates hub notes so each doc section forms a cluster in graph view.
Stdlib only.
"""

import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

VAULT = Path(r"C:\Users\bifro\OneDrive\Desktop\obsidian project 1")
BASE = "https://docs.baseten.co/"
ROOT_HUB = "Baseten Docs Map"

SECTION_NAMES = {
    "": "Basics",
    "api-reference": "API Reference",
    "concepts": "Concepts",
    "deployment": "Deployment",
    "development": "Development",
    "engines": "Engines",
    "examples": "Examples",
    "frontier-gateway": "Frontier Gateway",
    "inference": "Inference",
    "loops": "Loops",
    "observability": "Observability",
    "organization": "Organization",
    "reference": "Reference",
    "status": "Status",
    "training": "Training",
    "troubleshooting": "Troubleshooting",
}

ILLEGAL = re.compile(r'[\\/:*?"<>|#^\[\]]')


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")


def sanitize(name: str) -> str:
    name = ILLEGAL.sub("", name).strip().rstrip(".")
    return re.sub(r"\s+", " ", name)


def parse_index(text: str):
    """Yield (title, url_path, description) from llms.txt."""
    for m in re.finditer(
        r"^- \[(?P<title>[^\]]+)\]\((?P<url>https://docs\.baseten\.co/[^)\s]+?)\.md\)"
        r"(?::\s*(?P<desc>.*))?$",
        text,
        re.M,
    ):
        path = m.group("url")[len(BASE):]
        yield m.group("title").strip().rstrip("."), path, (m.group("desc") or "").strip()


def build_registry(entries):
    """Assign each url path a unique note title and a vault-relative file path."""
    reg = {}          # url_path -> dict(title, file, section)
    used_titles = {}  # lowercased title -> url_path
    for title, path, desc in entries:
        parts = path.split("/")
        section_key = parts[0] if len(parts) > 1 else ""
        section = SECTION_NAMES.get(section_key, section_key.replace("-", " ").title())
        base_title = sanitize(title) or sanitize(parts[-1].replace("-", " ").title())
        note_title = base_title
        if note_title.lower() in used_titles:
            # disambiguate with the parent folder name
            qualifier = sanitize(parts[-2].replace("-", " ").title()) if len(parts) > 1 else section
            note_title = f"{base_title} ({qualifier})"
        n = 2
        while note_title.lower() in used_titles:
            note_title = f"{base_title} ({n})"
            n += 1
        used_titles[note_title.lower()] = path
        folder = Path(section) if len(parts) == 1 else Path(section, *[p.replace("-", " ") for p in parts[1:-1]])
        reg[path] = {
            "title": note_title,
            "file": folder / f"{note_title}.md",
            "section": section,
            "desc": desc,
        }
    return reg


def strip_mdx(text: str) -> str:
    # Drop the injected "Documentation Index" header block
    text = re.sub(r"\A(?:>.*\n)+\n?", "", text)
    # <Card title="X" href="/path"> -> bold link line (href resolved later with other links)
    text = re.sub(
        r'<Card\b[^>]*?title="([^"]*)"[^>]*?href="([^"]*)"[^>]*?/?>',
        r"- **[\1](\2)**",
        text,
    )
    text = re.sub(
        r'<Card\b[^>]*?href="([^"]*)"[^>]*?title="([^"]*)"[^>]*?/?>',
        r"- **[\2](\1)**",
        text,
    )
    # Callout-ish tags -> blockquote marker kept simple
    text = re.sub(r"<(Note|Tip|Warning|Info|Check)>", lambda m: f"> **{m.group(1)}:**", text)
    # Remove remaining JSX open/close/self-closing tags (keep inner content)
    text = re.sub(r"</?[A-Z][A-Za-z0-9]*\b[^>]*/?>", "", text)
    # Collapse 3+ blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def link_repl(reg):
    def repl(m):
        label, target = m.group(1), m.group(2)
        t = target.lstrip("/").split("#")[0].split("?")[0]
        if t.endswith(".md"):
            t = t[:-3]
        info = reg.get(t)
        if info:
            if label.strip() == info["title"]:
                return f"[[{info['title']}]]"
            return f"[[{info['title']}|{label}]]"
        return m.group(0)
    return repl


def convert_links(text: str, reg) -> str:
    # internal absolute-path links: [text](/path...) or [text](https://docs.baseten.co/path...)
    text = re.sub(
        r"\[([^\]]+)\]\((?:https://docs\.baseten\.co)?(/[^)\s]+)\)",
        link_repl(reg),
        text,
    )
    return text


def main():
    print("Fetching index...")
    idx = fetch(BASE + "llms.txt")
    entries = list(parse_index(idx))
    print(f"{len(entries)} pages in index")
    reg = build_registry(entries)

    results = {}
    def grab(path):
        try:
            results[path] = fetch(BASE + path + ".md")
        except Exception as e:
            results[path] = None
            print(f"  FAILED {path}: {e}")

    print("Downloading pages (16 threads)...")
    with ThreadPoolExecutor(max_workers=16) as ex:
        list(ex.map(grab, reg.keys()))

    ok = sum(1 for v in results.values() if v)
    print(f"Downloaded {ok}/{len(reg)} pages")

    # group notes by section and by sub-folder for hubs
    by_section = {}
    for path, info in reg.items():
        if results.get(path) is None:
            continue
        by_section.setdefault(info["section"], []).append(path)

    # write notes
    print("Writing notes...")
    for path, info in reg.items():
        raw = results.get(path)
        if raw is None:
            continue
        body = convert_links(strip_mdx(raw), reg)
        # drop the H1 (Obsidian shows filename as title) but keep description quote
        body = re.sub(r"\A# .*\n+", "", body)
        section = info["section"]
        parts = path.split("/")
        sub = parts[1].replace("-", " ").title() if len(parts) > 2 else None
        hub = f"{sub} ({section})" if sub and len(by_section_sub(by_section, reg, section, parts[1])) >= 4 else f"{section} Hub"
        tags = [section.lower().replace(" ", "-")]
        if sub:
            tags.append(parts[1])
        fm = (
            "---\n"
            f"tags: [baseten, {', '.join(tags)}]\n"
            f"source: {BASE}{path}\n"
            "---\n\n"
        )
        footer = f"\n\n---\nPart of [[{hub}]]\n"
        out = VAULT / info["file"]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(fm + body.strip() + footer, encoding="utf-8")

    # hubs: section hubs + sub-hubs for big subfolders
    print("Writing hub notes...")
    hub_dir = VAULT / "Hubs"
    hub_dir.mkdir(exist_ok=True)
    section_hub_lines = {}
    for section, paths in sorted(by_section.items()):
        subgroups = {}
        loose = []
        for p in paths:
            parts = p.split("/")
            if len(parts) > 2:
                subgroups.setdefault(parts[1], []).append(p)
            else:
                loose.append(p)
        lines = [f"# {section}", "", f"Part of [[{ROOT_HUB}]]", ""]
        for sub, sps in sorted(subgroups.items()):
            if len(sps) >= 4:
                subname = f"{sub.replace('-', ' ').title()} ({section})"
                lines.append(f"- [[{subname}]] *({len(sps)} pages)*")
                sub_lines = [f"# {subname}", "", f"Part of [[{section} Hub]]", ""]
                sub_lines += [f"- [[{reg[p]['title']}]]" for p in sorted(sps, key=lambda x: reg[x]["title"])]
                (hub_dir / f"{sanitize(subname)}.md").write_text(
                    "---\ntags: [baseten, hub]\n---\n\n" + "\n".join(sub_lines) + "\n", encoding="utf-8"
                )
            else:
                loose.extend(sps)
        for p in sorted(loose, key=lambda x: reg[x]["title"]):
            d = f" — {reg[p]['desc']}" if reg[p]["desc"] else ""
            lines.append(f"- [[{reg[p]['title']}]]{d}")
        (hub_dir / f"{section} Hub.md").write_text(
            "---\ntags: [baseten, hub]\n---\n\n" + "\n".join(lines) + "\n", encoding="utf-8"
        )
        section_hub_lines[section] = len(paths)

    root = [f"# {ROOT_HUB}", "", "Baseten documentation as a knowledge graph. Open graph view to explore.", ""]
    for section, count in sorted(section_hub_lines.items()):
        root.append(f"- [[{section} Hub]] *({count} pages)*")
    (VAULT / f"{ROOT_HUB}.md").write_text("\n".join(root) + "\n", encoding="utf-8")
    print("Done.")


def by_section_sub(by_section, reg, section, sub):
    return [p for p in by_section.get(section, []) if p.split("/")[1:2] == [sub] and len(p.split("/")) > 2]


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
