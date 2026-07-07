---
tags: [baseten, reference, sdk]
source: https://docs.baseten.co/reference/sdk/loops/sampling-client
---

> Generate completions from current or version-pinned Loops weights.

`SamplingClient` generates text completions from the model the sampler currently has loaded. There are two creation paths with different version semantics: [[ServiceClient|`ServiceClient.create_sampling_client`]] returns an auto-updating client that follows whatever weights the sampler currently holds, while [[TrainingClient|`TrainingClient.save_weights_and_get_sampling_client`]] returns a snapshot client pinned to the trained version. Both clients expose the same `sample` method.

For high-concurrency workloads, the SDK configures a large HTTP connection pool by default. Override it with `BT_LOOPS_MAX_CONNECTIONS` when you need a different limit, for example on a VM behind Cloud NAT with a tight port budget.

Generate from the current weights:

```python theme={"system"}
from baseten.loops import ModelInput, SamplingParams

result = sampling_client.sample(
    prompt=ModelInput.from_ints(prompt),
    num_samples=1,
    sampling_params=SamplingParams(max_tokens=16),
)
print(result.sequences[0].tokens)
```

  Generate `num_samples` completions from `prompt` (a [[Types|`ModelInput`]]). Pass a [[Types|`SamplingParams`]] instance to control temperature, top-p, top-k, max tokens, seed, and stop sequences; omit it to use defaults. Set `include_prompt_logprobs=True` to get per-token log-probabilities for the input tokens alongside the output, and set `topk_prompt_logprobs` above `0` to also return the top-k alternatives at each prompt position. The sampler resolves which adapter or base model to serve from the version headers the client carries, so there is no per-call model override.

  Return the per-token log-probabilities for `prompt` without generating any new tokens. Index 0 is always `None` because the first token has no preceding context to score against. Other positions may also be `None` if the sampler can't compute a log-probability for that token.

  Return the base model ID from the sampler's `/v1/models` list, specifically the entry with no parent. Retries with backoff while the sampler is still deploying.

  Return the currently registered LoRA adapter ID (the first `/v1/models` entry with a non-null parent), or `None` if no adapter is loaded.

  Return the base model ID this sampling client was created with, without contacting the server.

  Return the Hugging Face `PreTrainedTokenizer` for the base model this client was created with.

  Block until the sampler's deployment status is `ACTIVE`. A scaled-to-zero deployment triggers one wake; terminal-failure states raise. No-op for local deployments.

  Class method. Block until `deployment` reports ready, using a throwaway `SamplingClient` so you can wait without holding one. Polls up to `ready_timeout` seconds and applies the same readiness semantics as `ensure_ready`.

---
Part of [[Sdk (Reference)]]
