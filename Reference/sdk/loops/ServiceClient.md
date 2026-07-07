---
tags: [baseten, reference, sdk]
source: https://docs.baseten.co/reference/sdk/loops/service-client
---

> Provision trainer and sampling servers, manage the Loops session, and list checkpoints.

`ServiceClient` is the entry point for every session. It calls the Baseten control plane to create a `TrainerSession`, then provisions trainer and sampling servers within that session on demand. It returns the [[TrainingClient|`TrainingClient`]] and [[SamplingClient|`SamplingClient`]] you drive for the rest of a run.

Provision a trainer and get a `TrainingClient`:

```python theme={"system"}
from baseten.loops import ServiceClient

service_client = ServiceClient()
training_client = service_client.create_lora_training_client(
    base_model="Qwen/Qwen3.5-2B", rank=16,
)
```

  Construct a `ServiceClient` and create a new `TrainerSession` on the Baseten control plane. Omit `training_project_id` to use the default project for the org, or pass one to target a specific training project. `api_key` defaults to the `BASETEN_API_KEY` environment variable.

  Pass `reuse_from_session_id` to reuse a prior session's trainer and sampler for `create_lora_training_client` and `create_sampling_client` calls instead of provisioning fresh. The named session must belong to the same team. `ServiceClient` reads the `LOOPS_REUSE_FROM_SESSION_ID` environment variable when no kwarg is passed; the kwarg wins when both are set. Reuse is best-effort: if the prior deployment is stopped, failed, or unhealthy, a fresh one is provisioned and the call still succeeds. See [[Concepts (Loops)|Reuse infrastructure across sessions]].

  Bind to already-running local trainer and sampler processes without contacting the control plane. Pass `trainer_url` and `sampler_url` as the base URLs of local server processes. Useful for end-to-end testing.

  Provision a `TrainerServer` for the given Hugging Face `base_model` and return a connected [[TrainingClient|`TrainingClient`]]. The control plane also provisions a paired sampling server in the same call; `save_weights_and_get_sampling_client` uses that paired URL to gate on version readiness. Pass a [[Types|`WandbConfig`]] instance to stream training metrics to a Weights & Biases run.

  Return a [[TrainingClient|`TrainingClient`]] initialized with the weights saved at `path`. The optimizer starts fresh. Use this to resume from a saved checkpoint when you do not need the prior optimizer state.

  Return a [[TrainingClient|`TrainingClient`]] that resumes from `path` with the optimizer state and step count intact. Use this to continue a run exactly where it left off.

  Provision a standalone `SamplingServer` for `base_model` and return a connected [[SamplingClient|`SamplingClient`]]. Use this when you want to sample from a base model independently of a training run. The `model_path` argument is reserved and not yet implemented; passing it raises `NotImplementedError`. To sample from a specific checkpoint, use `TrainingClient.create_sampling_client(model_path=...)` on a live run instead.

  Return the control plane's view of supported base models and the GPU classes it can provision them on. Useful for confirming a base model is available before calling `create_lora_training_client`. Returns [[Types|`ServerCapabilities`]].

  List checkpoints saved by the run identified by `run_id`. Calls the [[List checkpoints|list checkpoints API]], not the trainer server directly. Returns a list of [[Types|`Checkpoint`]].

  Return presigned URLs for every file in the specified checkpoint folder. Checkpoint IDs are globally unique, so no run scoping is required. The Loops stack writes checkpoints as unzipped directories rather than archives, so this returns a file list instead of a single archive URL. If the checkpoint files live in S3, export `S3_REGION` to that bucket's AWS region before calling this method. Wraps the [[Get checkpoint files|get checkpoint files API]].

  Property. The session ID assigned by the control plane. Available after construction.

---
Part of [[Sdk (Reference)]]
