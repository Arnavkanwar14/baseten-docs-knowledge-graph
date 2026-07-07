---
tags: [baseten, reference, cli]
source: https://docs.baseten.co/reference/cli/truss/model-logs
---

> Fetch logs for a deployed model.

```sh theme={"system"}
truss model-logs [OPTIONS]
```

Fetches logs for a deployed model. Use this command to debug issues or monitor model behavior in production.

### Options

  Name of the remote in `.trussrc`.

  ID of the model.

  ID of the deployment.

  Tail for ongoing logs. Streams new log entries as they arrive.

  Start of the log time range (ISO 8601). No-timezone values are local. Defaults to a short look-back ending at --end. Window must be \<= 7 days.

  End of the log time range (ISO 8601). No-timezone values are local. Defaults to now. Window must be \<= 7 days.

  Logs from a relative time ago until now, written as a number plus a unit of `s`, `m`, `h`, or `d` (for example `90s`, `2h`, or `3d`). Max `7d`. Cannot be combined with `--start` or `--end`.

  Minimum log severity. Defaults to all lines. Any value returns lines at or above that severity and drops lines with no level.

  Case-sensitive substring that must appear in the message (repeatable).

  Case-sensitive substring that drops any line containing it (repeatable).

  RE2 regex matched against the message. Prefer --includes/--excludes.

  Only return logs emitted by this replica (5-char short ID).

  Only return logs tagged with this inference request ID.

  Logging verbosity. `humanfriendly` (default) is pretty-printed; `INFO`, `DEBUG`, `WARNING` produce structured logs.

  Disable interactive prompts. Use in CI/automated contexts where stdin isn't a TTY.

**Example:**

Fetch logs for a specific deployment:

```sh theme={"system"}
truss model-logs --model-id YOUR_MODEL_ID --deployment-id YOUR_DEPLOYMENT_ID
```

Stream logs in real-time:

```sh theme={"system"}
truss model-logs --model-id YOUR_MODEL_ID --deployment-id YOUR_DEPLOYMENT_ID --tail
```

Fetch logs from the last two hours:

```sh theme={"system"}
truss model-logs --model-id YOUR_MODEL_ID --deployment-id YOUR_DEPLOYMENT_ID --since 2h
```

Fetch logs for a specific time window:

```sh theme={"system"}
truss model-logs --model-id YOUR_MODEL_ID --deployment-id YOUR_DEPLOYMENT_ID --start 2026-06-01T00:00:00 --end 2026-06-01T01:00:00
```

Filter logs to errors only:

```sh theme={"system"}
truss model-logs --model-id YOUR_MODEL_ID --deployment-id YOUR_DEPLOYMENT_ID --min-level error
```

### Rate limits

Baseten limits the deployment logs endpoint (`POST /v1/models/{model_id}/deployments/{deployment_id}/logs`) to 30 requests/second per API key. Interactive use, including `--tail`, stays well under that limit.

Scripts that wrap `truss model-logs` in a tight poll loop can hit the limit and receive `429 Too Many Requests`. Wait for the response's `retry_after` value (in seconds) before retrying. For the full response shape and a retry example, see [[Rate limits|management API rate limits]].

---
Part of [[Cli (Reference)]]
