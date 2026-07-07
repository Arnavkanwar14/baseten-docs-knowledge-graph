---
tags: [baseten, reference, cli]
source: https://docs.baseten.co/reference/cli/baseten/overview
---

> Manage your Baseten workspace from the command line: organizations, API keys, secrets, deployment lifecycle, replicas, and raw API access. Designed for automation.

The Baseten CLI manages your Baseten workspace from the command line: models, deployments, environments, secrets, API keys, and raw API access. Every Baseten-native command supports `--output json` and `--jq` filtering, so anything you do interactively is scriptable.

The CLI is open source on [GitHub](https://github.com/basetenlabs/baseten-cli), where you can browse the code, watch for new releases, and file issues.

> **Note:**
  The Baseten CLI is in **beta** and under active development. Commands, flags, output schemas, and the install path may change before general availability.

For authoring Chains, Training jobs, and Loops, use the [[Truss CLI reference|Truss CLI]]. The [[Baseten command-line tools|CLI overview]] explains when to reach for each.

## Install

Install with Homebrew on macOS or Linux:

```sh theme={"system"}
brew tap basetenlabs/baseten
brew trust basetenlabs/baseten
brew install baseten
```

Upgrade later with `brew upgrade baseten`.

  Download and extract the `baseten` binary for your platform, then place it on your `PATH`.

  
    
      Download and extract `baseten` into `/usr/local/bin`:

      ```sh theme={"system"}
      curl -sL https://github.com/basetenlabs/baseten-cli/releases/download/v0.2.0/baseten_0.2.0_darwin_arm64.tar.gz \
        | sudo tar xz -C /usr/local/bin baseten
      ```
    

    
      Download and extract `baseten` into `/usr/local/bin`:

      ```sh theme={"system"}
      curl -sL https://github.com/basetenlabs/baseten-cli/releases/download/v0.2.0/baseten_0.2.0_linux_amd64.tar.gz \
        | sudo tar xz -C /usr/local/bin baseten
      ```
    

    
      Download and extract the archive, then move `baseten.exe` to a directory on your `PATH`:

      ```powershell theme={"system"}
      Invoke-WebRequest `
        https://github.com/basetenlabs/baseten-cli/releases/download/v0.2.0/baseten_0.2.0_windows_amd64.zip `
        -OutFile baseten.zip; Expand-Archive -Force baseten.zip .
      ```
    
  

  For other platforms or a specific version, download an archive from [GitHub releases](https://github.com/basetenlabs/baseten-cli/releases) and move `baseten` onto your `PATH`.

Verify the install:

```sh theme={"system"}
baseten version
```

## Authenticate

Log in interactively:

```sh theme={"system"}
baseten auth login
```

For automation, set `BASETEN_API_KEY` in the environment instead. See [[baseten auth|`baseten auth`]] for browser login, reading a key from stdin, switching accounts, and credential storage.

## Output and filtering

Every Baseten-native command supports four output formats through `--output`:

* `text` (default): human-readable narrative.
* `json`: a single JSON document. Pair with `--jq EXPR` to extract one field.
* `jsonl`: one JSON record per line. Used by commands that stream results.
* `none`: suppress stdout entirely.

```sh theme={"system"}
baseten model push --jq '.predict_url'
```

`--jq` implies `--output json` (or `jsonl` for streamed commands), so a single flag turns any command into a clean value for the next stage of your pipeline.

## Global flags

These flags work on every Baseten-native command:

| Flag              | Description                                                                                           |
| ----------------- | ----------------------------------------------------------------------------------------------------- |
| `--profile`       | Use a specific stored profile for this command, overriding `BASETEN_PROFILE` and the current profile. |
| `--output`, `-o`  | Output format: `text`, `json`, `jsonl`, or `none`. See [Output and filtering](#output-and-filtering). |
| `--jq`, `-q`      | Filter JSON output with a jq expression. See [Output and filtering](#output-and-filtering).           |
| `--verbose`, `-v` | Enable verbose logging.                                                                               |

## Command groups

The `baseten` CLI organizes commands by resource:

```
baseten [OPTIONS] COMMAND [SUBCOMMAND] [ARGS]...
```

Start from the resource you need to manage.

| Command group                                                                         | Use it to                                                                                                            |
| ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| [[baseten api|`baseten api`]]                                           | Make raw management or inference API requests.                                                                       |
| [[baseten auth|`baseten auth`]]                                         | Log in, log out, switch accounts, and inspect the active account.                                                    |
| [[baseten model|`baseten model`]]                                       | Push, watch, list, describe, predict against, and delete models.                                                     |
| [[baseten model deployment|`baseten model deployment`]]                 | Activate, configure, download, promote, delete, describe, list, stream logs from, and fetch metrics for deployments. |
| [[baseten model deployment replica|`baseten model deployment replica`]] | Terminate an individual deployment replica.                                                                          |
| [[baseten model environment|`baseten model environment`]]               | Activate, deactivate, describe, and list model environments.                                                         |
| [[baseten model-api|`baseten model-api`]]                               | List and inspect Baseten Model APIs.                                                                                 |
| [[baseten org api-key|`baseten org api-key`]]                           | List, create, and delete organization API keys.                                                                      |
| [[baseten org billing|`baseten org billing`]]                           | Inspect organization billing usage.                                                                                  |
| [[baseten org secret|`baseten org secret`]]                             | List, set, and delete organization secrets.                                                                          |
| [[baseten truss|`baseten truss`]]                                       | Forward commands to the `truss` binary on your `PATH`.                                                               |
| [[baseten version|`baseten version`]]                                   | Print Baseten CLI version information.                                                                               |

## Next steps

  - **[[CICD|Deploy from CI]]**
    Use `baseten model push` from GitHub Actions and other CI runners.
  

  - **[Compare with Truss](/reference/cli)**
    See when to reach for `baseten` vs `truss` for each task.

---
Part of [[Cli (Reference)]]
