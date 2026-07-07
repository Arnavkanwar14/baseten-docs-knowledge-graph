---
tags: [baseten, reference, cli]
source: https://docs.baseten.co/reference/cli/truss/whoami
---

> Show user information.

```sh theme={"system"}
truss whoami [OPTIONS]
```

Shows the currently authenticated user information and exits. Use this command to verify your authentication status.

### Options

  Name of the remote in `.trussrc` to check.

  Display your [[OpenID Connect (OIDC) authentication|OIDC configuration]] for workload identity, including org ID, team IDs, issuer, audience, and the subject claim format used for cloud provider trust policies.

  Logging verbosity. `humanfriendly` (default) is pretty-printed; `INFO`, `DEBUG`, `WARNING` produce structured logs.

  Disable interactive prompts. Use in CI/automated contexts where stdin isn't a TTY.

**Examples:**

Check the current authenticated user:

```sh theme={"system"}
truss whoami
```

You should see:

```
my-workspace\user@example.com
```

View your OIDC configuration for setting up cloud provider trust policies:

```sh theme={"system"}
truss whoami --show-oidc
```

This displays your OIDC configuration for workload identity:

| Field                 | Description                                                   | Example                                                                                                                      |
| --------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Org ID                | Your organization identifier                                  | `Mvg9jrRd`                                                                                                                   |
| Teams                 | Team IDs within your organization                             | `AviIZ0y3 (my-team)`                                                                                                         |
| Issuer                | The Baseten OIDC issuer URL                                   | `https://oidc.baseten.co`                                                                                                    |
| Audience              | The expected audience claim                                   | `oidc.baseten.co`                                                                                                            |
| Workload Type Options | Available workload types for subject claims                   | `model_container`, `model_build`                                                                                             |
| Subject Claim Format  | Pattern used in cloud provider trust policies to scope access | `v=1:org=<org_id>:team=<team_id>:model=<model_id>:deployment=<deployment_id>:environment=<environment>:type=<workload_type>` |

Use the org and team IDs from this output when configuring trust policies in [[OpenID Connect (OIDC) authentication|AWS]] or [[OpenID Connect (OIDC) authentication|GCP]].

---
Part of [[Cli (Reference)]]
