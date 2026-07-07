---
tags: [baseten, reference, cli]
source: https://docs.baseten.co/reference/cli/truss/cleanup
---

> Clean up Truss data.

```sh theme={"system"}
truss cleanup [OPTIONS]
```

Clears temporary directories created by Truss for operations like building Docker images. Use this to free up disk space.

### Options

  Logging verbosity. `humanfriendly` (default) is pretty-printed; `INFO`, `DEBUG`, `WARNING` produce structured logs.

  Disable interactive prompts. Use in CI/automated contexts where stdin isn't a TTY.

**Example:**

Clean up temporary Truss data:

```sh theme={"system"}
truss cleanup
```

This command produces no output on success. Temporary files are removed from `~/.truss/`.

---
Part of [[Cli (Reference)]]
