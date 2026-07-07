---
tags: [baseten, reference, cli]
source: https://docs.baseten.co/reference/cli/loops/loops-cli
---

> Deploy and inspect Loops sessions, runs, samplers, and checkpoints using the Truss CLI.

The `truss loops` command provides subcommands for the [[Concepts (Loops)|Loops]] deployment lifecycle: pushing a deployment for a base model, viewing runs and samplers, and listing or deploying checkpoints from a run.

```sh theme={"system"}
truss loops [OPTIONS] COMMAND [ARGS]...
```

| Command                                     | Description                                             |
| ------------------------------------------- | ------------------------------------------------------- |
| [`push`](#push)                             | Provision a session, run, and sampler for a base model. |
| [`deactivate`](#deactivate)                 | Shut down the active deployment for a base model.       |
| [`view`](#view)                             | List active Loops deployments.                          |
| [`logs`](#logs)                             | Fetch logs from a Loops deployment or its sampler.      |
| [`runs view`](#runs-view)                   | List Loops runs.                                        |
| [`samplers view`](#samplers-view)           | List Loops samplers.                                    |
| [`checkpoints view`](#checkpoints-view)     | List checkpoints for a Loops run.                       |
| [`checkpoints deploy`](#checkpoints-deploy) | Deploy checkpoints from a Loops run.                    |

***

## `push`

Provision a Loops session, run, and paired sampler for a base model. If the project already has an active Loops deployment for the base model, the command fails with a validation error.

```sh theme={"system"}
truss loops push [OPTIONS] BASE_MODEL
```

### Arguments

  Hugging Face model ID for the base model (for example, `Qwen/Qwen3-8B`).

### Options

  Training project ID to associate the deployment with.

  Number of data-parallel trainer replicas to provision. The trainer deployment runs this many copies of the base model's preset node group (for example, `--replicas 4` on a 4-node preset provisions 16 nodes across 4 data-parallel workers). Must be a positive integer; defaults to 1.

  Name of the remote in `.trussrc` to deploy to.

  Logging verbosity. `humanfriendly` (default) is pretty-printed; `INFO`, `DEBUG`, `WARNING` produce structured logs.

  Disable interactive prompts. Use in CI/automated contexts where stdin isn't a TTY.

**Example:**

```sh theme={"system"}
truss loops push Qwen/Qwen3-8B
```

***

## `deactivate`

Shut down a Loops deployment. Saved checkpoints remain accessible after deactivation.

```sh theme={"system"}
truss loops deactivate [OPTIONS] DEPLOYMENT_ID
```

### Arguments

  ID of the deployment to shut down. Get the deployment ID from `truss loops view`.

### Options

  Name of the remote in `.trussrc`.

  Skip the confirmation prompt.

  Logging verbosity. `humanfriendly` (default) is pretty-printed; `INFO`, `DEBUG`, `WARNING` produce structured logs.

  Disable interactive prompts. Use in CI/automated contexts where stdin isn't a TTY.

**Example:**

```sh theme={"system"}
truss loops deactivate <deployment_id> --yes
```

***

## `view`

List the caller's active Loops deployments. Deployments whose latest status is `STOPPED` are filtered out server-side.

```sh theme={"system"}
truss loops view [OPTIONS]
```

### Options

  Name of the remote in `.trussrc`.

  Include deployments in terminal states (STOPPED, FAILED).

  Output format: cli-table (default) or json.

  Logging verbosity. `humanfriendly` (default) is pretty-printed; `INFO`, `DEBUG`, `WARNING` produce structured logs.

  Disable interactive prompts. Use in CI/automated contexts where stdin isn't a TTY.

**Example:**

```sh theme={"system"}
truss loops view
```

The command prints a table with the deployment ID, base model, base URL, and deployment URL.

***

## `logs`

Fetch logs from one half of a Loops deployment. A Loops deployment and its sampler have separate log streams, so pass exactly one of `--loops-deployment-id` or `--sampler-deployment-id` depending on which side you're debugging.

```sh theme={"system"}
truss loops logs [OPTIONS]
```

### Options

  Fetch logs from a Loops deployment. The id is the `Deployment ID` column in `truss loops view`.

  Fetch logs from the sampler's inference deployment. The id is the `Sampler Deployment ID` column in `truss loops samplers view`. The companion model id is resolved automatically by matching against the caller's active Loops deployments.

  Continue polling for new log lines until the deployment goes inactive (or Ctrl+C).

  Remote to use.

  Customizes logging.

  Disables interactive prompts, use in CI / automated execution contexts.

**Examples:**

```sh theme={"system"}
truss loops logs --loops-deployment-id <deployment_id>
```

Stream the sampler's logs and keep polling until the deployment goes inactive:

```sh theme={"system"}
truss loops logs --sampler-deployment-id <sampler_deployment_id> --tail
```

Get the deployment IDs from `truss loops view` (`Deployment ID`) and `truss loops samplers view` (`Sampler Deployment ID`).

***

## `runs view`

List Loops runs visible to the caller. Both filters are optional and can be combined; omit both to list every run.

```sh theme={"system"}
truss loops runs view [OPTIONS]
```

### Options

  Filter to a specific run ID.

  Filter runs by base model name.

  Reverse the default order (oldest first) so the most recent run is shown first.

  Name of the remote in `.trussrc`.

  Logging verbosity. `humanfriendly` (default) is pretty-printed; `INFO`, `DEBUG`, `WARNING` produce structured logs.

  Disable interactive prompts. Use in CI/automated contexts where stdin isn't a TTY.

**Example:**

List the most recent runs for a base model:

```sh theme={"system"}
truss loops runs view --base-model Qwen/Qwen3-8B --reverse
```

***

## `samplers view`

List Loops samplers visible to the caller.

```sh theme={"system"}
truss loops samplers view [OPTIONS]
```

### Options

  Reverse the default order (oldest first) so the most recent sampler is shown first.

  Name of the remote in `.trussrc`.

  Logging verbosity. `humanfriendly` (default) is pretty-printed; `INFO`, `DEBUG`, `WARNING` produce structured logs.

  Disable interactive prompts. Use in CI/automated contexts where stdin isn't a TTY.

**Example:**

```sh theme={"system"}
truss loops samplers view --reverse
```

***

## `checkpoints view`

List checkpoints for a Loops run. Identify the run with `--run-id`, or pass `--base-model` to pick the most recent run for that base model. The two filters are mutually exclusive.

```sh theme={"system"}
truss loops checkpoints view [OPTIONS]
```

### Options

  Loops run ID to list checkpoints for. Mutually exclusive with `--base-model`.

  Base model name. Resolves to the most recent Loops run for that model. Mutually exclusive with `--run-id`.

  Sort checkpoints by checkpoint ID, creation time, size, or type.

  Sort order.

  Output format.

  Name of the remote in `.trussrc`.

  Logging verbosity. `humanfriendly` (default) is pretty-printed; `INFO`, `DEBUG`, `WARNING` produce structured logs.

  Disable interactive prompts. Use in CI/automated contexts where stdin isn't a TTY.

**Examples:**

List checkpoints for the most recent run of a base model:

```sh theme={"system"}
truss loops checkpoints view --base-model Qwen/Qwen3-8B
```

Get the largest checkpoints first, as JSON:

```sh theme={"system"}
truss loops checkpoints view --run-id <run_id> --sort size --order desc -o json
```

***

## `checkpoints deploy`

Deploy checkpoints from a Loops run as a vLLM-backed inference deployment. You must pass one of `--run-id`, `--checkpoint-ids`, or `--config`.

```sh theme={"system"}
truss loops checkpoints deploy [OPTIONS]
```

### Options

  Loops run ID. Opens an interactive picker so you can choose checkpoints from the run. Cannot be combined with `--checkpoint-ids`.

  Comma-separated Loops checkpoint IDs (for example, `vL3pQrS8,wK4tUvW9`). Bypasses the interactive picker. Use `truss loops checkpoints view` to find IDs. Cannot be combined with `--run-id` or `--config`.

  Path to a Python file that defines a `DeployCheckpointsConfig`. The config must populate `checkpoint_details.loops_checkpoint_ids`. Cannot be combined with `--checkpoint-ids`.

  Render the generated truss config to stdout without deploying.

  Name of the remote in `.trussrc`.

  Logging verbosity. `humanfriendly` (default) is pretty-printed; `INFO`, `DEBUG`, `WARNING` produce structured logs.

  Disable interactive prompts. Use in CI/automated contexts where stdin isn't a TTY.

**Examples:**

Pick checkpoints interactively from a run:

```sh theme={"system"}
truss loops checkpoints deploy --run-id <run_id>
```

Deploy specific checkpoint IDs:

```sh theme={"system"}
truss loops checkpoints deploy --checkpoint-ids vL3pQrS8,wK4tUvW9
```

Render the generated config without deploying:

```sh theme={"system"}
truss loops checkpoints deploy --run-id <run_id> --dry-run
```

## Related

* [[Concepts (Loops)|Loops concepts]]: How sessions, runs, samplers, and checkpoints fit together.
* [[Supported base models|Loops supported models]]: Base models you can pass to `truss loops push`.
* [[Training SDK|Training SDK reference]]: `CheckpointList` and `DeployCheckpointsConfig` Python types used with `--config`.

---
Part of [[Cli (Reference)]]
