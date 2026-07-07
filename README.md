# Baseten Docs — Obsidian Knowledge Graph

The complete [Baseten documentation](https://docs.baseten.co) (410 pages) converted into an Obsidian vault with wikilinks, so the whole doc site is explorable as a visual knowledge graph.

## How to open

1. Open Obsidian → **Open folder as vault** → pick this folder (`obsidian project 1`).
2. Press **Ctrl+G** (or click the graph icon in the left sidebar) to open **Graph view**.
3. Sections are color-coded (Inference, Engines, Training, etc.); white nodes are hub notes.

Start reading from [[Baseten Docs Map]] — it links to every section hub.

## How it's structured

- One note per docs page, in folders matching the docs sections.
- Every internal docs link was converted to a `[[wikilink]]` — those are the graph edges (~2,500 of them).
- `Hubs/` contains index notes so each section forms a connected cluster.
- Each note's frontmatter has the original `source:` URL and section tags.

Built 2026-07-07 from https://docs.baseten.co/llms.txt (raw markdown endpoints).
