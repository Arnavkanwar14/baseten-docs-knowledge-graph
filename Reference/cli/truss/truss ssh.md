---
tags: [baseten, reference, cli]
source: https://docs.baseten.co/reference/cli/truss/ssh
---

> SSH access to Baseten workloads.

```sh theme={"system"}
truss ssh [COMMAND] [OPTIONS]
```

Configures SSH access to Baseten workloads: training jobs and model replicas. For training usage, see [[SSH access (Training)|SSH access]]. For models, enable [[Truss configuration|`runtime.remote_ssh`]] in your Truss config.

## Subcommands

### setup

Configures OpenSSH on your machine to authenticate with Baseten and connect to workloads. Run this once per machine.

```sh theme={"system"}
truss ssh setup [OPTIONS]
```

Generates an SSH keypair, installs a `ProxyCommand` script, and adds a wildcard `Host` entry to `~/.ssh/config`. After running this once, connect to any running workload:

```sh theme={"system"}
# Training job, per node
ssh training-job-<job_id>-<node>.ssh.baseten.co

# Model deployment (requires runtime.remote_ssh.enabled in the Truss config)
ssh model-<model_id>-<deployment_id>.ssh.baseten.co

# Specific replica of a model deployment
ssh model-<model_id>-<deployment_id>-<replica_id>.ssh.baseten.co
```

#### Options

  Path to a Python 3.10+ interpreter for the `ProxyCommand`. Auto-detected if omitted. Use this if you see TLS errors with the default Python.

  Default remote to use when the hostname doesn't specify one and `~/.trussrc` has multiple remotes. If you have a single remote, Baseten uses it automatically.

  Logging verbosity. `humanfriendly` (default) is pretty-printed; `INFO`, `DEBUG`, `WARNING` produce structured logs.

  Disable interactive prompts. Use in CI/automated contexts where stdin isn't a TTY.

#### Examples

Run one-time setup:

```sh theme={"system"}
truss ssh setup
```

If you see TLS errors, specify a newer Python:

```sh theme={"system"}
truss ssh setup --python /opt/homebrew/bin/python3.13
```

Set a default remote when multiple are configured:

```sh theme={"system"}
truss ssh setup --default-remote baseten-dev
```

---
Part of [[Cli (Reference)]]
