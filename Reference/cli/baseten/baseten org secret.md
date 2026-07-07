---
tags: [baseten, reference, cli]
source: https://docs.baseten.co/reference/cli/baseten/org-secret
---

> Manage secrets

## list

```sh theme={"system"}
baseten org secret list [OPTIONS]
```

List secrets (metadata only; values are never returned).

### Options

  Filter JSON output with a jq expression; implies --output json (or jsonl for streamed commands)

  Output format

  One of: `text`, `json`, `jsonl`, `none`

  Use a specific stored profile for this command, overriding BASETEN\_PROFILE and the current profile

  Filter to a specific team by name or ID. Defaults to all teams the caller belongs to.

  Enable verbose logging

### Examples

List secrets across all accessible teams

```sh theme={"system"}
baseten org secret list
```

List secrets in a specific team

```sh theme={"system"}
baseten org secret list --team <team>
```

### Filter output with `--jq`

Print just the secret names

```sh theme={"system"}
baseten org secret list --jq '.secrets[].name'
```

### Output

**Text mode (`--output text`):** Table with columns: NAME, TEAM, CREATED. When no secrets exist, prints "No secrets found." to stderr.

**JSON mode (`--output json`):** payload type `managementapi.Secrets`.

## set

```sh theme={"system"}
baseten org secret set [OPTIONS]
```

Create or update a secret. The value is read from stdin (or prompted interactively on a TTY). `--value` is supported but discouraged: it leaks the secret into shell history and `ps` output. Pass `--team` to target a specific team; without it the organization's default team is used.

### Options

  Filter JSON output with a jq expression; implies --output json (or jsonl for streamed commands)

  Name of the secret.

  Output format

  One of: `text`, `json`, `jsonl`, `none`

  Use a specific stored profile for this command, overriding BASETEN\_PROFILE and the current profile

  Team name or ID the secret belongs to. Defaults to the organization's default team.

  Secret value. Discouraged: leaks into shell history and process list. Prefer stdin or prompt.

  Enable verbose logging

### Examples

Set a secret by piping its value through stdin

```sh theme={"system"}
echo $TOKEN | baseten org secret set --name <name>
```

Set a secret scoped to a specific team

```sh theme={"system"}
echo $TOKEN | baseten org secret set --name <name> --team <team>
```

### Filter output with `--jq`

Print the secret's team

```sh theme={"system"}
echo $TOKEN | baseten org secret set --name <name> --jq '.team_name'
```

### Output

**Text mode (`--output text`):** Prints "Set secret `name`" to stderr on success; no stdout output.

**JSON mode (`--output json`):** payload type `managementapi.Secret`.

## delete

```sh theme={"system"}
baseten org secret delete [OPTIONS]
```

Delete a secret by name.

### Options

  Filter JSON output with a jq expression; implies --output json (or jsonl for streamed commands)

  Name of the secret to delete.

  Output format

  One of: `text`, `json`, `jsonl`, `none`

  Use a specific stored profile for this command, overriding BASETEN\_PROFILE and the current profile

  Team name or ID the secret belongs to. Defaults to the organization's default team.

  Enable verbose logging

### Examples

Delete a secret by name

```sh theme={"system"}
baseten org secret delete --name <name>
```

### Filter output with `--jq`

Print just the deleted secret name

```sh theme={"system"}
baseten org secret delete --name <name> --jq '.name'
```

### Output

**Text mode (`--output text`):** Prints "Deleted secret `name`" to stderr on success; no stdout output.

**JSON mode (`--output json`):** payload type `managementapi.SecretTombstone`.

---
Part of [[Cli (Reference)]]
