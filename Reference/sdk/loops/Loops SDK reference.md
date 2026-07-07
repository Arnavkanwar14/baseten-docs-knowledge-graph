---
tags: [baseten, reference, sdk]
source: https://docs.baseten.co/reference/sdk/loops/overview
---

> Python client for Loops: ServiceClient, TrainingClient, SamplingClient, types, and errors.

The Loops Python SDK runs LoRA training on Baseten from Python. For installation and an end-to-end walkthrough, see the [[Quickstart|Loops quickstart]]. This reference documents each class and type.

## Clients

* [[ServiceClient|`ServiceClient`]]: provision trainer and sampling servers, manage the session, and list checkpoints.
* [[TrainingClient|`TrainingClient`]]: run forward and backward passes, optimizer steps, and publish weights.
* [[SamplingClient|`SamplingClient`]]: generate completions from current or version-pinned weights.

## Commonly used methods

* [[ServiceClient|`create_lora_training_client()`]]: provision a trainer and get a `TrainingClient`.
* [[TrainingClient|`forward_backward()`]] and [[TrainingClient|`optim_step()`]]: run one training step.
* [[TrainingClient|`save_state()`]]: save a checkpoint.
* [[TrainingClient|`save_weights_and_get_sampling_client()`]]: publish weights and get a pinned `SamplingClient`.
* [[SamplingClient|`sample()`]]: generate from the trained model.
* [[TrainingClient|`list_checkpoints()`]]: list a run's checkpoints.

## Reference

* [[Types]]: training inputs, configuration, and result handles.
* [[Errors]]: the SDK exception types and when each is raised.

## Tinker compatibility

Install with the `[tinker]` extra and `import tinker` to run existing Tinker training scripts unchanged. For the mapped names and behavioral differences, see the [[Tinker compatibility|Tinker compatibility guide]].

---
Part of [[Sdk (Reference)]]
