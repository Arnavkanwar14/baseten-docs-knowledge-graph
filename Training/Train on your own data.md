---
tags: [baseten, training]
source: https://docs.baseten.co/training/your-own-data
---

> Swap the tutorial's dataset, config, and hardware for your real fine-tuning workload.

The [[Get started (Training)|getting started tutorial]] fine-tunes Qwen3-4B on a demo dataset. Moving to your own workload changes the dataset, how weights and data load, the training config, and the hardware. Everything else (the project layout, `truss train push`, checkpoint sync, deployment) stays the same.

## Swap the dataset

The tutorial's `train.py` loads a public Hugging Face dataset:

```python theme={"system"}
dataset = load_dataset("winglian/pirate-ultrachat-10k", split="train")
```

Point `load_dataset()` at your own Hugging Face repo, or at files bundled with your project (everything in your project directory ships with `truss train push`):

```python theme={"system"}
dataset = load_dataset("json", data_files="data/train.jsonl", split="train")
```

For gated or private Hugging Face models or datasets, add your `hf_access_token` secret to the job and read it from the environment; the tutorial's container makes unauthenticated Hugging Face requests, so a gated model fails at training time without this. See [[Training SDK|secrets in training]].

TRL's `SFTTrainer` consumes chat-format datasets (a `messages` column) directly. For other shapes, apply a formatting function; the [TRL SFT docs](https://huggingface.co/docs/trl/sft_trainer) cover the options.

## Load weights and data through BDN

The tutorial's `train.py` downloads the base model inside the container, on billed GPU time, on every job. The better pattern is to mount weights and large datasets through [[Storage and data ingestion|BDN]]: declare a [[Training SDK|`WeightsSource`]] on the job, and the files are on local disk before your start commands run. BDN mirrors each source once and caches it, so re-runs skip the download entirely.

Add `WeightsSource` to the `truss_train` imports in `config.py` and declare the mounts:

```python config.py theme={"system"}
training_job = TrainingJob(
    image=Image(base_image=BASE_IMAGE),
    compute=training_compute,
    runtime=training_runtime,
    weights=[
        WeightsSource(
            source="hf://Qwen/Qwen3-4B",
            mount_location="/app/models/Qwen/Qwen3-4B",
        ),
        WeightsSource(
            source="s3://my-bucket/training-data",
            mount_location="/app/data",
        ),
    ],
)
```

Then load from the mount paths instead of remote IDs:

```python train.py theme={"system"}
model = AutoModelForCausalLM.from_pretrained("/app/models/Qwen/Qwen3-4B", ...)
dataset = load_dataset("json", data_files="/app/data/train.jsonl", split="train")
```

BDN supports Hugging Face, S3, GCS, R2, and HTTPS sources; private sources authenticate through a per-source `auth` block. See [[Storage and data ingestion|storage and data ingestion]] for the full configuration.

## Adjust the training config

The tutorial caps the run at 50 steps so it finishes fast. For a real run, train on the full dataset and checkpoint less often. Keep the tutorial's other settings (`learning_rate`, `bf16`, `max_length`); these are the fields that change:

```python theme={"system"}
training_args = SFTConfig(
    num_train_epochs=1,          # remove max_steps=50; epochs take over
    save_steps=500,              # checkpoint cadence; each one syncs to Baseten
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    output_dir=os.getenv("BT_CHECKPOINT_DIR", "./checkpoints"),
)
```

Keep `output_dir` on `$BT_CHECKPOINT_DIR`: that's the directory Baseten syncs and deploys from. And every checkpoint you save is uploaded, so pick a `save_steps` cadence you'd actually resume or deploy from; frequent saves on a large model cost sync time and storage.

If the job hits GPU out-of-memory, lower `per_device_train_batch_size` and raise `gradient_accumulation_steps` to hold the effective batch size, or move up a GPU tier.

## Scale the hardware

Hardware lives in `config.py`, not in your training code. A bigger base model needs more GPUs:

```python theme={"system"}
training_compute = Compute(
    accelerator=AcceleratorSpec(accelerator="H100", count=4),
)
```

For workloads beyond one machine, set `node_count` and Baseten handles the InfiniBand networking and orchestration; see [[Multinode training|multi-node training]].

## Iterate faster on re-runs

Your second submission shouldn't re-download the base model. The tutorial's config already enables the [[Cache|training cache]] (`CacheConfig(enabled=True)`); keep it on, and cache model downloads and preprocessed data under the cache directory so subsequent jobs skip them.

To debug a live job instead of resubmitting, [[SSH access (Training)|SSH into the running container]] or attach [[VS Code and Cursor remote tunnels|VS Code or Cursor]].

## Next steps

* Browse the [ML Cookbook](https://github.com/basetenlabs/ml-cookbook) for complete recipes: Axolotl, DPO, RL with VeRL, and multi-node FSDP.
* [[Serve your trained model|Deploy your checkpoints]] when training finishes.

---
Part of [[Training Hub]]
