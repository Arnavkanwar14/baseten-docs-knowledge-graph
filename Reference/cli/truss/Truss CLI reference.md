---
tags: [baseten, reference, cli]
source: https://docs.baseten.co/reference/cli/truss/overview
---

> Deploy, manage, and develop models using the Truss CLI.

```sh theme={"system"}
truss [OPTIONS] COMMAND [ARGS]...
```

**Options:**

  Show the version and exit.

  Customize logging verbosity.

  Disable interactive prompts. Use in CI or automated execution contexts.

  Show help message and exit.

### Main commands

| Command                                         | Description                       |
| ----------------------------------------------- | --------------------------------- |
| [[truss init|`init`]]             | Create a new Truss project        |
| [[truss push|`push`]]             | Deploy a model to Baseten         |
| [[truss watch|`watch`]]           | Live reload during development    |
| [[truss model-logs|`model-logs`]] | Fetch logs for the packaged model |

### Advanced commands

| Command                                       | Description                             |
| --------------------------------------------- | --------------------------------------- |
| [[truss image|`image`]]         | Build and manage Truss Docker images    |
| [[truss container|`container`]] | Run and manage Truss containers locally |
| [[truss cleanup|`cleanup`]]     | Clean up Truss data                     |

### Other commands

| Command                                             | Description                                                |
| --------------------------------------------------- | ---------------------------------------------------------- |
| [[truss auth|`auth`]]                 | Manage authentication (login, logout, status)              |
| [[truss login|`login`]]               | Authenticate with Baseten                                  |
| [[truss configure|`configure`]]       | Configure Truss settings                                   |
| [[truss download|`download`]]         | Download the Truss for a deployed model                    |
| [[truss migrate|`migrate`]]           | Migrate `model_cache` / `external_data` to the weights API |
| [[truss model-config|`model-config`]] | Fetch the config of a deployed model                       |
| [[truss run-python|`run-python`]]     | Run a Python script in the Truss environment               |
| [[truss ssh|`ssh`]]                   | Configure SSH access to workloads                          |
| [[truss upgrade|`upgrade`]]           | Upgrade the Truss CLI to the latest version                |
| [[truss whoami|`whoami`]]             | Show user information and exit                             |

> **Note:**
  All commands support `--help` to display usage information.

---
Part of [[Cli (Reference)]]
