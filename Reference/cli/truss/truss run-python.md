---
tags: [baseten, reference, cli]
source: https://docs.baseten.co/reference/cli/truss/run-python
---

> Run a Python script in the Truss environment.

```sh theme={"system"}
truss run-python [OPTIONS] SCRIPT [TARGET_DIRECTORY]
```

Runs a Python script in the same environment as your Truss. This builds a Docker
image matching your Truss environment, mounts the script, and executes it. Use
this to test scripts with the same dependencies your model uses.

### Arguments

  Path to the Python script to run.

  A Truss directory. Defaults to current directory.

**Example:**

Run a script in the Truss environment:

```sh theme={"system"}
truss run-python test_script.py
```

Run a script with a specific Truss directory:

```sh theme={"system"}
truss run-python test_script.py /path/to/my-truss
```

---
Part of [[Cli (Reference)]]
