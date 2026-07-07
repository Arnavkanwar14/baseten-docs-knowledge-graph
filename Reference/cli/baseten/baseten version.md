---
tags: [baseten, reference, cli]
source: https://docs.baseten.co/reference/cli/baseten/version
---

> Print the baseten CLI version

Print the version of the baseten CLI.

## version

```sh theme={"system"}
baseten version [OPTIONS]
```

### Options

  Filter JSON output with a jq expression; implies --output json (or jsonl for streamed commands)

  Output format

  One of: `text`, `json`, `jsonl`, `none`

  Use a specific stored profile for this command, overriding BASETEN\_PROFILE and the current profile

  Enable verbose logging

### Examples

Print the CLI version

```sh theme={"system"}
baseten version
```

### Filter output with `--jq`

Print just the version string from JSON

```sh theme={"system"}
baseten version --jq '.version'
```

### Output

**Text mode (`--output text`):** Prints the CLI version on a single line.

**JSON mode (`--output json`):** payload type `cmd.VersionResult`.

---
Part of [[Cli (Reference)]]
