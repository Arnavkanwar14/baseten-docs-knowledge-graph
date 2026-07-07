---
tags: [baseten, reference, cli]
source: https://docs.baseten.co/reference/cli/index
---

> Truss authors model code and the Baseten CLI manages your workspace: what each is for, where they overlap, and how to use them together.

The **Truss CLI** authors and deploys models: write a `config.yaml`, iterate with `truss watch`, and push to Baseten. It also runs the [[Chains CLI reference|Chains]], [[Training CLI reference|Training]], and [[Loops CLI reference|Loops]] workflows. Install with `uvx truss` or `pip install truss`.

The **Baseten CLI** <span className="preview-badge">Beta</span> manages your workspace: organizations, API keys, secrets, and the deployment lifecycle, from promoting deployments to terminating replicas. It also calls models and the Baseten API. Every command supports `--output json` and `--jq` filtering, built for scripts and CI. Install with [[Baseten CLI overview|Homebrew]].

Both CLIs are open source and authenticate against the same Baseten backend.

## Which one do I use?

| Task                                                                   | CLI                                                  |
| ---------------------------------------------------------------------- | ---------------------------------------------------- |
| Authoring `model.py` or `config.yaml` and iterating with `truss watch` | Truss                                                |
| Deploying a model from your editor                                     | Truss (`truss push`)                                 |
| Deploying a model from a CI workflow that parses output                | Baseten CLI (`baseten model push`)                   |
| Authoring a Chain, Training job, or Loop                               | Truss (`truss chains`, `truss train`, `truss loops`) |
| Creating or deleting an org API key                                    | Baseten CLI (`baseten org api-key`)                  |
| Promoting a development deployment to production                       | Baseten CLI (`baseten model deployment promote`)     |
| Querying a model from a shell pipeline                                 | Baseten CLI (`baseten model predict --jq ...`)       |
| Managing org secrets                                                   | Baseten CLI (`baseten org secret`)                   |
| Terminating a deployment replica                                       | Baseten CLI (`baseten model deployment replica`)     |

## Overlapping commands

A few commands exist in both CLIs:

| Action         | Truss              | Baseten CLI                     | Pick based on                                                                                                                   |
| -------------- | ------------------ | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Authenticate   | `truss login`      | `baseten auth login`            | Whichever CLI you already have installed. Both hit the same backend.                                                            |
| Deploy a model | `truss push`       | `baseten model push`            | `truss push` while iterating locally (supports `--watch`). `baseten model push` from CI (structured output, scriptable errors). |
| Tail logs      | `truss model-logs` | `baseten model deployment logs` | Match the workflow you're already in.                                                                                           |

## Use both together

`baseten truss` forwards arguments to the `truss` binary on your `PATH`, so `baseten truss push` works as a synonym for `truss push`.

## Next steps

  - **[[Build your model|Author a model]]**
    Use Truss to package and deploy your first model.
  

  - **[[Baseten CLI overview|Manage your workspace]]**
    Use the Baseten CLI for orgs, deployments, and automation.
  

  - **[[Your first Chain|Build a Chain]]**
    Create multi-step inference pipelines with `truss chains`.
  

  - **[[CICD|Wire CI/CD]]**
    Use `baseten model push` in GitHub Actions and other pipelines.

---
Part of [[Cli (Reference)]]
