---
tags: [baseten, reference, cli]
source: https://docs.baseten.co/reference/cli/truss/container
---

> Run and manage Truss containers locally.

```sh theme={"system"}
truss container [OPTIONS] COMMAND [ARGS]...
```

Manage Docker containers for your Truss.

***

## `kill`

Kill containers related to a specific Truss.

```sh theme={"system"}
truss container kill [OPTIONS] [TARGET_DIRECTORY]
```

### Arguments

  A Truss directory. Defaults to current directory.

**Example:**

Kill containers for the current Truss:

```sh theme={"system"}
truss container kill
```

***

## `kill-all`

Kill all Truss containers that are not manually persisted.

```sh theme={"system"}
truss container kill-all [OPTIONS]
```

**Example:**

Kill all Truss containers:

```sh theme={"system"}
truss container kill-all
```

***

## `logs`

Get logs from a running Truss container.

```sh theme={"system"}
truss container logs [OPTIONS] [TARGET_DIRECTORY]
```

### Options

  Logging verbosity. `humanfriendly` (default) is pretty-printed; `INFO`, `DEBUG`, `WARNING` produce structured logs.

  Disable interactive prompts. Use in CI/automated contexts where stdin isn't a TTY.

### Arguments

  A Truss directory. Defaults to current directory.

**Example:**

View logs from the current Truss container:

```sh theme={"system"}
truss container logs
```

---
Part of [[Cli (Reference)]]
