---
tags: [baseten, reference, cli]
source: https://docs.baseten.co/reference/cli/baseten/model
---

> Manage Baseten models

Create, list, and push Baseten models.

Authentication is through 'baseten auth login' or the BASETEN\_API\_KEY environment variable.

## push

```sh theme={"system"}
baseten model push [OPTIONS] [--dir DIR]
```

Build a model archive, upload it to Baseten, and create either a new model or a new deployment of an existing model.

The current directory is used by default; pass `--dir` to push a model directory at another path.

The model is identified by the `model_name` field in config.yaml. Use `--override-name` to override that for this push only.

### Options

  Deployment timeout as a Go duration (e.g. 30m, 1h); allowed range 10m to 24h.

  Human-readable name for the new deployment.

  Push as a development deployment: the model's single mutable dev slot, created if absent and overwritten in place otherwise. Incompatible with --environment and --deployment-name.

  Model directory to push. Defaults to the current directory.

  Disable archive download for the new model. Only valid for new models.

  Validate the push and request upload credentials without uploading or creating anything.

  Stable environment to push to.

  Filter JSON output with a jq expression; implies --output json (or jsonl for streamed commands)

  User-provided labels for the deployment as a JSON object, e.g. '\{"team":"ml","priority":1}'.

  Force a full rebuild without using cached layers.

  Output format

  One of: `text`, `json`, `jsonl`, `none`

  Use this deployment's instance type instead of preserving the target environment's. Only meaningful when an environment is targeted.

  Override the model\_name from config.yaml for this push only. The on-disk config.yaml is not modified.

  Use a specific stored profile for this command, overriding BASETEN\_PROFILE and the current profile

  Stream build and runtime logs to stderr after pushing. Logs are always text-formatted; use 'baseten model deployment logs --tail' for structured log streaming.

  Team the model belongs to. Only valid for new models.

  Block until the deployment is active. Exits non-zero on a terminal-failure status.

  After pushing, watch the model directory and live-patch the development deployment on change. Implies --develop.

  With --watch, hot-reload the running container when every change is to model code; mixed changes fall back to a cold patch.

  With --watch, let the development deployment scale to zero while watching. By default it is kept warm by periodic pings.

  Enable verbose logging

### Examples

Push the current directory as a new deployment

```sh theme={"system"}
baseten model push
```

Push and stream build/runtime logs until the deployment is active

```sh theme={"system"}
baseten model push --tail --wait
```

### Filter output with `--jq`

Print the new deployment's predict URL

```sh theme={"system"}
baseten model push --jq '.predict_url'
```

### Output

**Text mode (`--output text`):** Narrative summary on stdout: success banner, deployment status, log/predict URLs and example next-step commands. Under `--output json` the narrative is redirected to stderr so stdout stays a clean JSON document.

**JSON mode (`--output json`):** payload type `cmd.ModelPushResult`.

Under `--dry-run` no upload or deployment happens; the push is validated, upload credentials are requested, and stdout is the empty JSON object `\{\}`. Otherwise stdout is the full model+deployment result.

## watch

```sh theme={"system"}
baseten model watch [--dir DIR]
```

Watch a model directory and live-patch its development deployment. It applies each change as you save and runs until you interrupt it.

### Options

  Model directory to watch. Defaults to the current directory.

  Hot-reload the running container when every change is to model code; mixed changes fall back to a cold patch.

  Filter JSON output with a jq expression; implies --output json (or jsonl for streamed commands)

  Let the development deployment scale to zero while watching. By default it is kept warm by periodic pings.

  Output format

  One of: `text`, `json`, `jsonl`, `none`

  Use a specific stored profile for this command, overriding BASETEN\_PROFILE and the current profile

  Team the model belongs to. Use to disambiguate when the same model\_name exists in multiple teams.

  Enable verbose logging

### Examples

Watch the current directory against its model's development deployment

```sh theme={"system"}
baseten model watch
```

Watch another directory and hot-reload on model-code changes

```sh theme={"system"}
baseten model watch --dir ./my-model --hot-reload
```

### Output

**Text mode (`--output text`):** Streams patch and sync status to stderr as changes are applied. Produces no stdout output.

## list

```sh theme={"system"}
baseten model list [OPTIONS]
```

List Baseten models.

### Options

  Filter JSON output with a jq expression; implies --output json (or jsonl for streamed commands)

  Output format

  One of: `text`, `json`, `jsonl`, `none`

  Use a specific stored profile for this command, overriding BASETEN\_PROFILE and the current profile

  Team name or ID to scope the listing to. Defaults to all teams the caller can see.

  Enable verbose logging

### Examples

List all models accessible to the caller

```sh theme={"system"}
baseten model list
```

List only models in a specific team

```sh theme={"system"}
baseten model list --team my-team
```

### Filter output with `--jq`

Print just the model IDs

```sh theme={"system"}
baseten model list --jq '.models[].id'
```

### Output

**Text mode (`--output text`):** Table with columns: ID, NAME, TEAM, DEPLOYMENTS, CREATED. When no models exist, prints "No models found." to stderr.

**JSON mode (`--output json`):** payload type `managementapi.Models`.

## describe

```sh theme={"system"}
baseten model describe [OPTIONS]
```

Describe a Baseten model.

### Options

  Filter JSON output with a jq expression; implies --output json (or jsonl for streamed commands)

  ID of the model.

  Mutually exclusive with other flags in group `model-ref`.

  Name of the model. Use --team to disambiguate when the same name exists in multiple teams.

  Mutually exclusive with other flags in group `model-ref`.

  Output format

  One of: `text`, `json`, `jsonl`, `none`

  Use a specific stored profile for this command, overriding BASETEN\_PROFILE and the current profile

  Team name or ID. Only valid with --model-name.

  Enable verbose logging

### Examples

Describe a model by ID

```sh theme={"system"}
baseten model describe --model-id <model-id>
```

Describe a model by name

```sh theme={"system"}
baseten model describe --model-name <name>
```

### Filter output with `--jq`

Print the production deployment ID

```sh theme={"system"}
baseten model describe --model-id <model-id> --jq '.production_deployment_id'
```

### Output

**Text mode (`--output text`):** Field-per-line summary: ID, Name, Team, Deployments, Instance, Production, Development, Created. Optional fields are omitted when unset.

**JSON mode (`--output json`):** payload type `managementapi.Model`.

## predict

```sh theme={"system"}
baseten model predict [OPTIONS]
```

POST a JSON request to a model and write the response to stdout.

Targets the production environment by default. Use `--environment`, `--deployment-id`, or `--regional` to target something else.

Streaming responses (Transfer-Encoding: chunked) are passed through as they arrive. For machine-readable streaming JSON from OpenAI-compatible models, use `--output jsonl`.

### Options

  Inline JSON request body.

  Mutually exclusive with other flags in group `predict-input`.

  Specific deployment to target. Mutually exclusive with --environment and --regional.

  Environment to target (e.g. production, development). Defaults to production. Mutually exclusive with --deployment-id and --regional.

  Path to a JSON file containing the request body. Use '-' for stdin.

  Mutually exclusive with other flags in group `predict-input`.

  Filter JSON output with a jq expression; implies --output json (or jsonl for streamed commands)

  ID of the model.

  Mutually exclusive with other flags in group `model-ref`.

  Name of the model. Use --team to disambiguate when the same name exists in multiple teams.

  Mutually exclusive with other flags in group `model-ref`.

  Output format

  One of: `text`, `json`, `jsonl`, `none`

  Use a specific stored profile for this command, overriding BASETEN\_PROFILE and the current profile

  Regional environment name; routes through the regional hostname. Mutually exclusive with --environment and --deployment-id.

  Team name or ID. Only valid with --model-name.

  Use the WebSocket predict endpoint. Sends the body as one frame, reads one frame back, then closes. Not for multi-message or back-and-forth sessions.

  Enable verbose logging

### Examples

Send an inline JSON body

```sh theme={"system"}
baseten model predict --model-id <model-id> --data '{"prompt":"hello"}'
```

Send a request body from a file

```sh theme={"system"}
baseten model predict --model-id <model-id> --file request.json
```

### Filter output with `--jq`

Extract a field when the model returns JSON

```sh theme={"system"}
baseten model predict --model-id <model-id> --data '{"x":1}' --jq '.result'
```

### Output

**Text mode (`--output text`):** The model's response body, passed through verbatim. May be JSON, plain text, or binary, and may stream when the model uses chunked transfer encoding or SSE.

**JSON mode (`--output json`):** payload type `cmd.JSONUndefined`.

Under `--output json`, binary frames are base64-encoded under a 'body' key. Under `--output jsonl`, each SSE or binary chunk is emitted as its own record, one per line.

## delete

```sh theme={"system"}
baseten model delete [OPTIONS]
```

Delete a Baseten model and all of its deployments.

Prompts for the model name to confirm the deletion. Pass `--yes` to skip the prompt. When stdin is not a terminal, `--yes` is required.

### Options

  Filter JSON output with a jq expression; implies --output json (or jsonl for streamed commands)

  ID of the model.

  Mutually exclusive with other flags in group `model-ref`.

  Name of the model. Use --team to disambiguate when the same name exists in multiple teams.

  Mutually exclusive with other flags in group `model-ref`.

  Output format

  One of: `text`, `json`, `jsonl`, `none`

  Use a specific stored profile for this command, overriding BASETEN\_PROFILE and the current profile

  Team name or ID. Only valid with --model-name.

  Skip the interactive confirmation prompt. Required when stdin is not a terminal.

  Enable verbose logging

### Examples

Delete by ID without confirmation

```sh theme={"system"}
baseten model delete --model-id <model-id> --yes
```

Delete by name with interactive confirmation

```sh theme={"system"}
baseten model delete --model-name <name>
```

### Filter output with `--jq`

Print the deleted model's ID

```sh theme={"system"}
baseten model delete --model-id <model-id> --yes --jq '.id'
```

### Output

**Text mode (`--output text`):** On success, prints "Deleted model `name` (`id`)" to stderr; no stdout output.

**JSON mode (`--output json`):** payload type `managementapi.ModelTombstone`.

---
Part of [[Cli (Reference)]]
