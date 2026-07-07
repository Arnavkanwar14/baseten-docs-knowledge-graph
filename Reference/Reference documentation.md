---
tags: [baseten, reference]
source: https://docs.baseten.co/reference/overview
---

> For deploying, managing, and interacting with machine learning models on Baseten.

This reference section documents Baseten's APIs, CLIs, and Python SDKs for deploying models, managing your workspace, running training jobs, and calling endpoints in production.

## API reference

Baseten provides APIs for inference, workspace management, training, and the Frontier Gateway:

  - **[[Overview (Inference Api)|Inference API]]**
    For calling deployed models and chains.
  

  - **[[Overview (Management Api)|Management API]]**
    For managing models, workspaces, and deployments.
  

  - **[[Overview (Training Api)|Training API]]**
    For managing training projects and jobs, including the Loops API.
  

  - **[[Overview (Gateway)|Frontier Gateway API]]**
    For managing gateway endpoints, groups, and federated API keys.
  

## CLI reference

Truss authors and deploys model code; the Baseten CLI manages your workspace. The [[Baseten command-line tools|CLI overview]] explains when to use each.

* [[Truss CLI reference]]: Commands for initializing, deploying, and managing models.
* [[Baseten CLI overview|Baseten CLI reference]]: Commands for managing organizations, API keys, secrets, and the deployment lifecycle from scripts and CI.
* [[Chains CLI reference]]: Commands for orchestrating multi-model workflows.
* [[Training CLI reference]]: Commands for managing training jobs.
* [[Loops CLI reference]]: Commands for deploying and inspecting Loops sessions, runs, samplers, and checkpoints.

***

## Truss configuration

The [[Truss configuration|Truss configuration reference]] documents every key in `config.yaml`: model resources, dependencies, secrets, and engine settings.

***

## SDK reference

The Python SDKs provide an abstraction for deploying models, managing deployments, and interacting with models through code.

* [[Truss SDK Reference|Truss SDK reference]]: Deploy and interact with Truss models using Python.
* [[Chains SDK Reference|Chains SDK reference]]: Build and manage inference chains programmatically.
* [[Training SDK|Training SDK reference]]: Deploy and interact with trained models using Python.
* [[Loops SDK reference]]: Python clients for Loops training, sampling, and session management.

***

## CI/CD

The [[Truss Push GitHub Action]] deploys and validates a Truss model or chain from GitHub Actions.

---
Part of [[Reference Hub]]
