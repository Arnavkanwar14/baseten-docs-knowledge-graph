---
tags: [baseten, organization]
source: https://docs.baseten.co/organization/secrets
---

> Store and access sensitive credentials in your deployed models.

Secrets store sensitive credentials like API keys, access tokens, and passwords that your models need at runtime.
Secrets are encrypted and injected into your model's environment when it runs.

> **Note:**
  If your organization uses [[Teams|teams]], secrets are scoped to individual teams.
  Models, Chains, and training projects deployed to a team can only access that team's secrets.

## Create a secret

To create a secret:

1. Navigate to the **Secrets** tab in your settings. If your organization uses [[Teams|teams]], navigate to the team's settings page.
2. Enter a name for the secret.
3. Enter the secret value.
4. Select **Add secret**.

Secret names follow these rules:

* Non-alphanumeric characters are normalized (for example, `hf_access_token` and `hf-access-token` are treated as the same name).
* Editing a secret's value overwrites the previous value.
* Changes take effect immediately for all deployments using the secret.

## Use secrets in your model

To use secrets in your Truss model, see [[Secrets]].

## Security recommendations

* Create secrets through the Baseten dashboard, not in code.
* Use descriptive names that indicate the secret's purpose.
* Rotate secrets periodically by updating the value in the dashboard.
* Delete unused secrets to reduce exposure risk.

---
Part of [[Organization Hub]]
