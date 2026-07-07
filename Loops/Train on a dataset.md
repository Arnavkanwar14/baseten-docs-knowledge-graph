---
tags: [baseten, loops]
source: https://docs.baseten.co/loops/train-on-your-data
---

> Move from the quickstart's single example to a batched SFT loop with resumable checkpoints and mid-training evals.

The [[Quickstart|quickstart]] trains on one hardcoded prompt-and-answer pair. This guide runs the same round trip over a real dataset: batch the data into `Datum` lists, loop over it, save checkpoints you can resume from, and evaluate against the live sampler between steps.

The example dataset is [pirate-ultrachat-10k](https://huggingface.co/datasets/winglian/pirate-ultrachat-10k), chat-format conversations that teach the model pirate dialect. It's the same dataset the [[Get started (Training)|Truss Train tutorial]] uses, so you can compare the two paths on identical work.

## Turn a dataset into training data

Each training example becomes a [[Types|`Datum`]]: input tokens plus loss targets that mask the prompt and supervise the answer, with the same label shift the quickstart uses. For chat data, render the conversation with the tokenizer's chat template and treat the final assistant message as the answer.

Add `datasets` to your project (`uv add datasets`) and start `train_dataset.py`:

```python train_dataset.py theme={"system"}
import tinker
from datasets import load_dataset

BASE_MODEL = "Qwen/Qwen3.5-2B"

service_client = tinker.ServiceClient()
training_client = service_client.create_lora_training_client(
    base_model=BASE_MODEL,
    rank=16,
)
tokenizer = training_client.get_tokenizer()

def to_datum(example):
    messages = example["messages"]
    prompt = tokenizer.apply_chat_template(
        messages[:-1], tokenize=False, add_generation_prompt=True
    )
    p = tokenizer.encode(prompt, add_special_tokens=False)
    a = tokenizer.encode(messages[-1]["content"], add_special_tokens=False)
    full = p + a
    tokens = full[:-1]
    targets = [-100] * (len(p) - 1) + list(a)
    return tinker.Datum(
        model_input=tinker.ModelInput.from_ints(tokens),
        loss_fn_inputs={
            "target_tokens": tinker.TensorData(
                data=targets, dtype="int64", shape=[len(targets)]
            )
        },
    )

dataset = load_dataset("winglian/pirate-ultrachat-10k", split="train[:64]")
data = [to_datum(ex) for ex in dataset]
print(f"prepared {len(data)} examples")
```

The `train[:64]` slice keeps this guide's run short. Use the full split for a real fine-tune.

## Run the training loop

Each iteration is the quickstart's round trip over a batch: one `forward_backward()` on a list of `Datum`, one `optim_step()`. Append:

```python train_dataset.py theme={"system"}
BATCH_SIZE = 8

for step, start in enumerate(range(0, len(data), BATCH_SIZE), 1):
    batch = data[start : start + BATCH_SIZE]
    fb = training_client.forward_backward(data=batch).result(timeout=600.0)
    training_client.optim_step(
        tinker.AdamParams(learning_rate=4e-5)
    ).result(timeout=600.0)
    print(f"step {step} loss={fb.loss:.4f}")
```

## Save a resumable checkpoint

The quickstart's `save_weights_for_sampler()` publishes weights for sampling and deployment but omits optimizer state. For a checkpoint you can resume training from, use [[TrainingClient|`save_state()`]]; to publish the same point for sampling, save both. Append:

```python train_dataset.py theme={"system"}
state = training_client.save_state(name="epoch-1").result(timeout=600.0)
save_resp = training_client.save_weights_for_sampler(name="epoch-1").result(timeout=600.0)
print(f"resumable state at {state.path}")
print(f"sampler weights at {save_resp.path}")
```

To resume later, provision a training client and call [[TrainingClient|`load_state_with_optimizer()`]] with the saved `state.path`.

## Evaluate against the live sampler

The sampler already has your published weights, so an eval between epochs is one call, no deploy step. Append:

```python train_dataset.py theme={"system"}
sampling_client = training_client.create_sampling_client(model_path=save_resp.path)
prompt = tokenizer.apply_chat_template(
    [{"role": "user", "content": "How do I learn Python?"}],
    tokenize=False,
    add_generation_prompt=True,
)
sample = sampling_client.sample(
    prompt=tinker.ModelInput.from_ints(
        tokenizer.encode(prompt, add_special_tokens=False)
    ),
    num_samples=1,
    sampling_params=tinker.SamplingParams(max_tokens=48),
)
print(tokenizer.decode(sample.sequences[0].tokens))
```

Run the script with `uv run python train_dataset.py`. Values vary, but a successful run prints falling losses, both checkpoint paths, and a completion:

```output theme={"system"}
prepared 64 examples
step 1 loss=2.3548
step 2 loss=2.3185
...
step 8 loss=2.0167
resumable state at bt://loops:v31yx93/weights/epoch-1
sampler weights at bt://loops:v31yx93/sampler_weights/epoch-1
Learning Python is one of the fastest and most rewarding ways to start programming. ...
```

Loss falls across the eight steps, but the completion still reads like the base model: 64 examples isn't enough to change its dialect. Training on the full split is what makes the model answer like the dataset. When you're done, [[Quickstart|shut down the session]].

## Next steps

* **[[Deploy a checkpoint]]**: Serve `epoch-1` as a production endpoint.
* **RL and advanced recipes**: The [Tinker cookbook](https://github.com/thinking-machines-lab/tinker-cookbook) recipes run on Loops; see [[Tinker compatibility]] for setup.

---
Part of [[Loops Hub]]
