---
tags: [baseten, reference, cli]
source: https://docs.baseten.co/reference/cli/truss/init
---

> Create a new Truss project.

```sh theme={"system"}
truss init [OPTIONS] TARGET_DIRECTORY
```

Creates a new Truss project in the specified directory with the standard file structure.

### Options

  Server type to create. Default: `TrussServer`.

  Value assigned to `model_name` in `config.yaml`.

  Use code-first tooling to build the model. Default: `--no-python-config`.

  Logging verbosity. `humanfriendly` (default) is pretty-printed; `INFO`, `DEBUG`, `WARNING` produce structured logs.

  Disable interactive prompts. Use in CI/automated contexts where stdin isn't a TTY.

### Arguments

  Directory where the Truss project is created.

**Examples:**

Create a new Truss project:

```sh theme={"system"}
truss init my-model
```

You should see:

```
Truss my-model was created in /path/to/my-model
```

This creates the following directory structure:

```
my-model/
├── config.yaml
├── data/
├── model/
│   ├── __init__.py
│   └── model.py
└── packages/
```

Create a Truss with a custom name:

```sh theme={"system"}
truss init --name "My Model" my-model
```

Create a Truss with TRT\_LLM backend:

```sh theme={"system"}
truss init --backend TRT_LLM my-trt-model
```

---
Part of [[Cli (Reference)]]
