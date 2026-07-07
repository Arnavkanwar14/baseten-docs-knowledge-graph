---
tags: [baseten, reference, cli]
source: https://docs.baseten.co/reference/cli/truss/upgrade
---

> Upgrade the truss package to the latest or a specified version.

```sh theme={"system"}
truss upgrade [OPTIONS] [VERSION]
```

Upgrades the installed `truss` package. Truss detects how the package was installed (for example, `pip`, `uv`, `pipx`, or `uv tool`) and runs the matching upgrade command. By default, it upgrades to the latest published version.

### Options

  Logging verbosity. `humanfriendly` (default) is pretty-printed; `INFO`, `DEBUG`, `WARNING` produce structured logs.

  Disable interactive prompts. Skips the `Proceed with upgrade?` confirmation and applies the upgrade. Use in CI/automated contexts.

### Arguments

  Specific version to install (for example, `0.17.0`). If omitted, upgrades to the latest version.

**Examples:**

Upgrade to the latest version:

```sh theme={"system"}
truss upgrade
```

You should see:

```
Detected installation method: pip
Will run: pip install --upgrade truss
Proceed with upgrade? [Y/n]
```

Pin to a specific version:

```sh theme={"system"}
truss upgrade 0.17.0
```

Upgrade non-interactively (skip the confirmation prompt), useful in CI:

```sh theme={"system"}
truss --non-interactive upgrade
```

> **Note:**
  If Truss can't detect the installation method (for example, an editable install from source), it exits with a message asking you to upgrade manually.

---
Part of [[Cli (Reference)]]
