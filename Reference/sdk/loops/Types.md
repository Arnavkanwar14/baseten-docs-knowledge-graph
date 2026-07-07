---
tags: [baseten, reference, sdk]
source: https://docs.baseten.co/reference/sdk/loops/types
---

> Training inputs, configuration, and result handles passed to and from the Loops clients.

Shared data types passed to and returned from the [[ServiceClient]], [[TrainingClient]], and [[SamplingClient]].

## Training inputs

  A single training example: a `ModelInput` paired with a dict of `TensorData` loss function inputs.

  A tokenized prompt, represented as a list of `ModelInputChunk` objects. Construct with `ModelInput.from_ints(token_ids)` for the common case.

  A discriminated union of `EncodedTextChunk` (a list of token IDs) and `ImageChunk` (a base64-encoded image with an expected token count).

  A serializable tensor with a flat data list, a dtype string, and a shape. Convert to and from `torch.Tensor` with `TensorData.to_torch()` and `TensorData.from_torch(tensor)`.

## Configuration

  Controls for text generation: `temperature`, `top_p`, `top_k`, `max_tokens`, `seed`, and `stop`.

  Optimizer hyperparameters: `learning_rate`, `beta1`, `beta2`, `eps`, `weight_decay`, and `grad_clip_norm`.

  Optional Weights & Biases settings (`project` and an optional run `name`) passed to `create_lora_training_client` to stream training metrics.

## Results and handles

  The full response from `sample()`: a list of `SampledSequence` objects in `sequences`, the `policy_version` the sampler replica was running, and `prompt_logprobs` / `topk_prompt_logprobs` populated when the matching `sample()` flags are set.

  A single generated sequence: a list of output token IDs, optional per-token log-probabilities, and a stop reason.

  Metadata for a saved checkpoint, populated by `list_checkpoints()`.

  A paginated list of presigned file URLs for a checkpoint, populated by `get_checkpoint_archive_url()`.

  One entry in a `CheckpointFilesResponse.presigned_urls` list: a presigned URL plus `relative_file_name`, `node_rank`, `size_bytes`, and `last_modified` metadata.

  Returned by `ServiceClient.get_server_capabilities()`; describe which base models the control plane can provision and on which GPU classes.

  A handle to a long-running training operation. Call `.result()` or `.result(timeout=seconds)` to block until the operation completes and return the result. The `forward` and `forward_backward` methods return a `ForwardBackwardFuture` subclass, and `save_weights_and_get_sampling_client` returns a composed future; both expose the same `.result()` contract.

  Response payloads returned by the matching `TrainingClient` and `SamplingClient` methods.

---
Part of [[Sdk (Reference)]]
