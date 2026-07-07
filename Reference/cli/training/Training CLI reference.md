---
tags: [baseten, reference, cli]
source: https://docs.baseten.co/reference/cli/training/training-cli
---

> Deploy, manage, and monitor training jobs using the Truss CLI.

The `truss train` command provides subcommands for managing the full training job lifecycle.

```sh theme={"system"}
truss train [COMMAND] [OPTIONS]
```

***

## init

Initialize a training project from templates or create an empty project.

```sh theme={"system"}
truss train init [OPTIONS]
```

### Options

  List all available examples.

  Customizes logging.

  Disables interactive prompts, use in CI / automated execution contexts.

### Examples

Initialize a project from a template:

```sh theme={"system"}
truss train init --examples qwen3-8b-lora-dpo-trl
```

Initialize multiple templates:

```sh theme={"system"}
truss train init --examples qwen3-8b-lora-dpo-trl,qwen3-8b-lora-verl
```

List available templates:

```sh theme={"system"}
truss train init --list-examples
```

Create an empty training project:

```sh theme={"system"}
truss train init
```

***

## push

Submit and run a training job.

```sh theme={"system"}
truss train push [OPTIONS] CONFIG
```

### Arguments

  Path to the training configuration file (for example, `config.py`).

### Options

  Remote to use.

  Tail for status + logs after push.

  Name of the training job.

  Team name for the training project

  > **Note:**
    The `--team` flag is only available if your organization has teams enabled. [Contact us](mailto:support@baseten.co) to enable teams, or see [[Teams]] for more information.
  

  Interactive session trigger mode

  Interactive session timeout in minutes

  Accelerator type and count (e.g., H200:8)

  Number of compute nodes

  Entrypoint command.

  Job priority (higher values run first when capacity frees up).

  Customizes logging.

  Disables interactive prompts, use in CI / automated execution contexts.

### Examples

Submit a training job:

```sh theme={"system"}
truss train push config.py
```

Submit and stream logs:

```sh theme={"system"}
truss train push config.py --tail
```

Submit to a specific team:

```sh theme={"system"}
truss train push config.py --team my-team-name
```

Submit with a custom job name:

```sh theme={"system"}
truss train push config.py --job-name fine-tune-v1
```

***

## logs

Fetch and stream logs from a training job.

```sh theme={"system"}
truss train logs [OPTIONS]
```

### Options

  Remote to use.

  Project ID.

  Project name or project id.

  Job ID.

  Tail for ongoing logs.

  Customizes logging.

  Disables interactive prompts, use in CI / automated execution contexts.

### Examples

Stream logs for a specific job:

```sh theme={"system"}
truss train logs --job-id abc123 --tail
```

View logs for a job without streaming:

```sh theme={"system"}
truss train logs --job-id abc123
```

***

## metrics

View real-time metrics for a training job including CPU, GPU, and storage usage.

```sh theme={"system"}
truss train metrics [OPTIONS]
```

### Options

  Project ID.

  Project name or project id.

  Job ID.

  Remote to use.

  Customizes logging.

  Disables interactive prompts, use in CI / automated execution contexts.

### Examples

View metrics for a specific job:

```sh theme={"system"}
truss train metrics --job-id abc123
```

***

## view

List training projects and jobs, or view details for a specific job. This command lists jobs in the `TRAINING_JOB_PENDING` state (waiting for GPU capacity) alongside other active jobs.

```sh theme={"system"}
truss train view [OPTIONS]
```

### Options

  View training jobs for a project.

  Project name or project id.

  View a specific training job.

  Remote to use.

  Customizes logging.

  Disables interactive prompts, use in CI / automated execution contexts.

### Examples

List all training projects:

```sh theme={"system"}
truss train view
```

View jobs in a specific project:

```sh theme={"system"}
truss train view --project my-project
```

View details for a specific job:

```sh theme={"system"}
truss train view --job-id abc123
```

***

## stop

Stop a running or pending training job.

```sh theme={"system"}
truss train stop [OPTIONS]
```

### Options

  Project ID.

  Project name or project id.

  Job ID.

  Stop all running jobs.

  Remote to use.

  Customizes logging.

  Disables interactive prompts, use in CI / automated execution contexts.

### Examples

Stop a specific job:

```sh theme={"system"}
truss train stop --job-id abc123
```

Stop all running jobs:

```sh theme={"system"}
truss train stop --all
```

***

## recreate

Recreate an existing training job with the same configuration.

```sh theme={"system"}
truss train recreate [OPTIONS]
```

### Options

  Job ID of Training Job to recreate

  Remote to use.

  Tail for status + logs after recreation.

  Customizes logging.

  Disables interactive prompts, use in CI / automated execution contexts.

### Examples

Recreate a specific job:

```sh theme={"system"}
truss train recreate --job-id abc123
```

Recreate and stream logs:

```sh theme={"system"}
truss train recreate --job-id abc123 --tail
```

***

## download

Download training job artifacts to your local machine.

```sh theme={"system"}
truss train download [OPTIONS]
```

### Options

  Job ID.

  Remote to use.

  Directory where the file should be downloaded. Defaults to current directory.

  Instructs truss to not unzip the folder upon download.

  Customizes logging.

  Disables interactive prompts, use in CI / automated execution contexts.

### Examples

Download artifacts to current directory:

```sh theme={"system"}
truss train download --job-id abc123
```

Download to a specific directory:

```sh theme={"system"}
truss train download --job-id abc123 --target-directory ./downloads
```

Download without extracting:

```sh theme={"system"}
truss train download --job-id abc123 --no-unzip
```

***

## deploy\_checkpoints

Deploy a trained model checkpoint to Baseten's inference platform.

```sh theme={"system"}
truss train deploy_checkpoints [OPTIONS]
```

### Options

  Project ID.

  Project name or project id.

  Job ID.

  path to a python file that defines a DeployCheckpointsConfig

  Generate a truss config without deploying

  Path to output the truss config to. If not provided, will output to truss\_configs/`model_version_name`*`model_version_id` or truss\_configs/dry\_run*`timestamp` if dry run.

  Remote to use.

  Customizes logging.

  Disables interactive prompts, use in CI / automated execution contexts.

### Examples

Deploy checkpoints interactively:

```sh theme={"system"}
truss train deploy_checkpoints
```

Deploy checkpoints from a specific job:

```sh theme={"system"}
truss train deploy_checkpoints --job-id abc123
```

Preview deployment without deploying:

```sh theme={"system"}
truss train deploy_checkpoints --job-id abc123 --dry-run
```

### Output

After a successful deployment, the command prints a labeled block with the Model ID, Deployment ID, and a link to the deployment's logs page.

***

## get\_checkpoint\_urls

Get presigned URLs for checkpoint artifacts.

```sh theme={"system"}
truss train get_checkpoint_urls [OPTIONS]
```

### Options

  Job ID.

  Remote to use.

  Customizes logging.

  Disables interactive prompts, use in CI / automated execution contexts.

### Examples

Get checkpoint URLs for a job:

```sh theme={"system"}
truss train get_checkpoint_urls --job-id abc123
```

***

## checkpoints list

List and interactively explore checkpoints for a training job.

```sh theme={"system"}
truss train checkpoints list [OPTIONS]
```

### Options

  Remote to use.

  Project ID.

  Project name or project id.

  Job ID.

  Jump directly into a specific checkpoint's files.

  Sort checkpoints by checkpoint-id, size, created date, or type.

  Sort order: ascending or descending.

  Output format: cli-table (default), csv, or json.

  Customizes logging.

  Disables interactive prompts, use in CI / automated execution contexts.

### Interactive mode

When using the default `cli-table` format in an interactive terminal, the command launches a checkpoint explorer:

1. **Checkpoint picker**: fuzzy-search and select a checkpoint from the list.
2. **File explorer**: navigate the checkpoint's directory tree. Press `→` or `Enter` to open a directory or view a file. Press `←` to go back. Press `Ctrl-C` to quit.

For `.safetensors` files, the explorer displays a tensor summary (layer names, dtypes, shapes, and parameter counts) instead of raw binary content. Text files display with syntax highlighting based on their file extension (for example, `.json`, `.py`, `.yaml`, `.toml`), falling back to plain text for unrecognized types.

### Examples

List checkpoints for the most recent job:

```sh theme={"system"}
truss train checkpoints list
```

List checkpoints for a specific job:

```sh theme={"system"}
truss train checkpoints list --job-id abc123
```

Jump directly into a checkpoint's files:

```sh theme={"system"}
truss train checkpoints list --job-id abc123 --checkpoint-name ckpt-001
```

Export checkpoint list as JSON:

```sh theme={"system"}
truss train checkpoints list --job-id abc123 --output-format json
```

Sort by size descending:

```sh theme={"system"}
truss train checkpoints list --job-id abc123 --sort size --order desc
```

***

## cache summarize

View a summary of the training cache for a project.

```sh theme={"system"}
truss train cache summarize [OPTIONS] PROJECT
```

### Arguments

  Project name or project ID.

### Options

  Remote to use.

  Sort files by filepath, size, modified date, file type, or permissions.

  Sort order: ascending or descending.

  Output format: cli-table (default), csv, or json.

  Customizes logging.

  Disables interactive prompts, use in CI / automated execution contexts.

### Examples

View cache summary:

```sh theme={"system"}
truss train cache summarize my-project
```

Sort by size descending:

```sh theme={"system"}
truss train cache summarize my-project --sort size --order desc
```

Export as JSON:

```sh theme={"system"}
truss train cache summarize my-project --output-format json
```

***

## isession

View or update interactive session details for a training job, including auth codes and connection status.

```sh theme={"system"}
truss train isession [OPTIONS]
```

### Options

  Job ID of the training job.

  Remote to use.

  Minutes to extend the session timeout by

  Change the session trigger (cannot be changed on on\_startup sessions)

  Output format (default: table)

  Customizes logging.

  Disables interactive prompts, use in CI / automated execution contexts.

### Examples

View session details for a job:

```sh theme={"system"}
truss train isession --job-id abc123
```

Extend session timeout:

```sh theme={"system"}
truss train isession --job-id abc123 --update-timeout 60
```

Output as JSON:

```sh theme={"system"}
truss train isession --job-id abc123 --format json
```

***

## update\_session

Update the interactive session configuration on a running training job. At least one of `--trigger` or `--timeout-minutes` must be provided.

```sh theme={"system"}
truss train update_session [OPTIONS] JOB_ID
```

### Arguments

  Job ID of the training job to update.

### Options

  When to create the interactive session: 'on\_startup' creates on job start, 'on\_failure' creates on job failure, 'on\_demand' allows manual session creation.

  Number of minutes before the interactive session times out.

  Remote to use.

  Customizes logging.

  Disables interactive prompts, use in CI / automated execution contexts.

### Examples

Change the session trigger:

```sh theme={"system"}
truss train update_session abc123 --trigger on_startup
```

Update the session timeout:

```sh theme={"system"}
truss train update_session abc123 --timeout-minutes 120
```

> **Warning:**
  `truss train update_session` requires API support that may not be available in all environments.
  If you receive a 404 error, set the trigger mode at push time using `--interactive on_startup` or `--interactive on_failure` instead.

***

## workstation

Spin up an SSH workstation on Baseten training infrastructure.

```sh theme={"system"}
truss train workstation [OPTIONS]
```

### Options

  GPU type for the workstation (default: H100).

  Number of GPUs for a single-node workstation (1-8, default: 1). Mutually exclusive with `--node-count`.

  Name of the training project that owns the workstation. Defaults to `workstation-\{accelerator}`, for example `workstation-H100`.

  Number of full nodes to provision, each using all of its GPUs. Values above 1 bootstrap a Slurm cluster across the nodes. Mutually exclusive with `--gpu-count`.

  > **Note:**
    See [[Slurm workstations]] for the cluster topology, verification steps, and how to launch distributed work.
  

  Orchestrator bootstrapped across multi-node workstations. `slurm` is the only supported value. Ignored for single-node workstations.

  Docker base image for every node (default: `nvidia/cuda:12.8.1-devel-ubuntu24.04`). Multi-node workstations install Slurm with `apt` at startup, so use a Debian-based image.

  Mount checkpoint storage on the workstation. See [[Checkpoints]].

  Path inside the container to save checkpoints.

  Checkpoint volume size in GiB.

  Job ID to load the latest checkpoint from.

  Name of the remote in `.trussrc` to use.

  Stream workstation status and logs after launch.

  Customizes logging.

  Disables interactive prompts, use in CI / automated execution contexts.

### Examples

Launch a workstation with default settings:

```sh theme={"system"}
truss train workstation
```

Launch a multi-GPU workstation:

```sh theme={"system"}
truss train workstation --accelerator H200 --gpu-count 4
```

Launch a workstation with a custom base image:

```sh theme={"system"}
truss train workstation --image pytorch/pytorch:2.7.0-cuda12.8-cudnn9-runtime
```

***

## capacity

Show GPU capacity limits and current usage for the organization.

```sh theme={"system"}
truss train capacity [OPTIONS]
```

### Options

  Name of the remote to use

### Examples

View capacity for the default remote:

```sh theme={"system"}
truss train capacity
```

***

## Ignore files and folders

Create a `.truss_ignore` file in your project root to exclude files from upload. Uses `.gitignore` syntax.

```plaintext .truss_ignore theme={"system"}
# Python cache files
__pycache__/
*.pyc
*.pyo
*.pyd

# Type checking
.mypy_cache/

# Testing
.pytest_cache/

# Large data files
data/
*.bin
```

---
Part of [[Cli (Reference)]]
