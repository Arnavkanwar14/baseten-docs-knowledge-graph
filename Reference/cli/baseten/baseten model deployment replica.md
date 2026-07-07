---
tags: [baseten, reference, cli]
source: https://docs.baseten.co/reference/cli/baseten/model-deployment-replica
---

> Manage replicas of a deployment

## terminate

```sh theme={"system"}
baseten model deployment replica terminate [OPTIONS]
```

Terminate a single replica of a model deployment.

Prompts for yes/no confirmation. Pass `--yes` to skip the prompt. When stdin is not a terminal, `--yes` is required.

### Options

  ID of the deployment.

  Filter JSON output with a jq expression; implies --output json (or jsonl for streamed commands)

  ID of the model.

  Mutually exclusive with other flags in group `model-ref`.

  Name of the model. Use --team to disambiguate when the same name exists in multiple teams.

  Mutually exclusive with other flags in group `model-ref`.

  Output format

  One of: `text`, `json`, `jsonl`, `none`

  Use a specific stored profile for this command, overriding BASETEN\_PROFILE and the current profile

  ID of the replica.

  Team name or ID. Only valid with --model-name.

  Skip the interactive confirmation prompt. Required when stdin is not a terminal.

  Enable verbose logging

### Examples

Terminate a replica without the confirmation prompt

```sh theme={"system"}
baseten model deployment replica terminate --model-id <model-id> --deployment-id <deployment-id> --replica-id <replica-id> --yes
```

### Filter output with `--jq`

Print just the success flag

```sh theme={"system"}
baseten model deployment replica terminate --model-id <model-id> --deployment-id <deployment-id> --replica-id <replica-id> --yes --jq '.success'
```

### Output

**Text mode (`--output text`):** On success, prints "Terminated replica `id` of deployment `id`" to stderr; no stdout output.

**JSON mode (`--output json`):** payload type `managementapi.TerminateReplicaResponse`.

---
Part of [[Cli (Reference)]]
