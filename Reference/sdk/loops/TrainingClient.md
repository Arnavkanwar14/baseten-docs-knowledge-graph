---
tags: [baseten, reference, sdk]
source: https://docs.baseten.co/reference/sdk/loops/training-client
---

> Run forward and backward passes, optimizer steps, and publish weights against a live Loops trainer.

`TrainingClient` talks directly to a `dp_worker` instance. Long-running operations use a submit-and-retrieve protocol: the submit fires immediately on the calling thread (so validation errors surface at call time) and `.result()` long-polls the server until the operation finishes. You can submit multiple operations before awaiting any of them. Construct one with [[ServiceClient|`ServiceClient.create_lora_training_client`]].

Run one training step and save a checkpoint. Each long-running call is submit-then-`.result()`:

```python theme={"system"}
from baseten.loops import Datum, ModelInput, TensorData, AdamParams

# tokens and targets come from tokenizing a masked prompt/answer pair;
# see the quickstart for the full tokenization step.
datum = Datum(
    model_input=ModelInput.from_ints(tokens),
    loss_fn_inputs={"target_tokens": TensorData(data=targets, dtype="int64", shape=[len(targets)])},
)

fb = training_client.forward_backward(data=[datum]).result(timeout=600.0)
training_client.optim_step(AdamParams(learning_rate=4e-5)).result(timeout=600.0)
save_resp = training_client.save_state(name="step-1").result(timeout=600.0)
```

> **Note:**
  Every long-running server operation on `ServiceClient`, `TrainingClient`, and `SamplingClient` (for example, `forward_backward`, `sample`, `create_lora_training_client`) has an `await`-able `*_async` counterpart for callers running their own event loop. The async variants accept the same arguments as their synchronous names. Simpler blocking calls like `health`, `ensure_ready`, `get_tokenizer`, and `close` (whose async form is `aclose`) have no `*_async` twin.

  Run a forward and backward pass over `data` (a list of [[Types|`Datum`]] objects) using the specified loss function. Returns a `ForwardBackwardFuture`; call `.result()` to block until the pass completes and retrieve the loss.

  `loss_fn` defaults to `"cross_entropy"`. The trainer accepts:

  * `cross_entropy`: supervised fine-tuning. Put per-token targets in each `Datum`'s `loss_fn_inputs` under `target_tokens`, using `-100` for positions to ignore. No `loss_fn_config` needed.
  * `importance_sampling`, `ppo`: reinforcement learning. Each `Datum`'s `loss_fn_inputs` must include per-position `logprobs` and `advantages`.
  * `dppo`, `cispo`, `dro`: additional reinforcement-learning losses.

  Run a forward pass without gradient computation. Same inputs and output shape as `forward_backward`, but the gradient buffer is left untouched, so it is safe to interleave with gradient accumulation steps.

  Apply the accumulated gradients using the Adam optimizer configured by [[Types|`AdamParams`]]. Call this after one or more `forward_backward` calls.

  Persist a local training checkpoint under `name`. When a weight sync URI is configured server-side, `save_state` also publishes the LoRA adapter so a polling sampler can hot-swap to the new weights.

  Publish the LoRA adapter to the paired sampling server under `name` without returning a snapshot-pinned `SamplingClient`. Use this when you don't need the version gate that `save_weights_and_get_sampling_client` provides.

  Publish the LoRA adapter to the paired sampling server under `name` and return a future that resolves to a [[SamplingClient|`SamplingClient`]] pinned to the newly published version. Calling `.result()` runs two stages: the trainer publishes weights, then the SDK polls the sampler until at least one replica reports the new version loaded. The sampler-wait phase has a fixed 600-second ceiling independent of the `timeout=` you pass to `.result()`; if no replica reports the new version by then, the call raises `RuntimeError`. The returned `SamplingClient` carries `X-Min-Policy-Version` on every subsequent `sample()` call, so requests only land on replicas that have the right weights.

  Load weights from a `bt://loops:<run_id>/weights/<checkpoint>` URI into this trainer. Use to resume training from a checkpoint.

  Same as `load_state` but also restores Adam moments. Use when you want bit-exact resumption.

  List checkpoints for the run bound to this client. Requires that this client was constructed using `ServiceClient.create_lora_training_client` (which populates the necessary session and run IDs automatically). Returns a list of [[Types|`Checkpoint`]].

  Return presigned URLs for every file in a checkpoint folder. If the checkpoint files live in S3, export `S3_REGION` to that bucket's AWS region before calling this method. Same semantics as [[ServiceClient|`ServiceClient.get_checkpoint_archive_url`]].

  Return a [[SamplingClient|`SamplingClient`]] bound to the paired sampler, loading the weights at `model_path` (a `bt://loops:<run_id>/sampler_weights/<checkpoint>` URI). Distinct from `ServiceClient.create_sampling_client`, which provisions a fresh sampler.

  Return the Hugging Face `PreTrainedTokenizer` for the base model. Cached after the first load.

  Return the model configuration for this training session (base model name, LoRA rank, and max sequence length) without a server round-trip.

  Property. The run ID this client is bound to. Use this when filtering checkpoints or making [[Loops API reference|HTTP API]] calls against the same run.

  Property. The number of `optim_step` calls applied to the trainer so far. Each access issues a `GET /policy_version` round-trip, so read it deliberately rather than in a tight loop.

  Reset trainer state to a fresh LoRA adapter at `lora_rank`. Use to start a new adapter on an existing trainer without reprovisioning.

  Check the trainer's `/health` endpoint. Returns `None` on success and raises if the trainer is unreachable or unhealthy.

  Close the client's HTTP connections and finish any active Weights & Biases run. In `async` code, call `aclose()` instead.

  Async counterpart to `close()` for callers running their own event loop.

---
Part of [[Sdk (Reference)]]
