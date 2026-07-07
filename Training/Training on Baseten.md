---
tags: [baseten, training]
source: https://docs.baseten.co/training/overview
---

> Train models on managed GPUs with Truss Train or Loops and deploy any checkpoint to production inference.

Baseten trains models on managed GPUs and deploys the resulting checkpoints to production inference on the same platform. There are two ways to train: **Truss Train**, where you bring your own container and training code, and **[[Loops]]**, a Tinker-compatible SDK for LoRA fine-tuning and RL on a curated set of base models.

## Choose your path

* **Coming from Tinker**: Loops is a Tinker-compatible backend for your existing scripts. `import tinker` works with one install change, and the [[Tinker compatibility]] page lists exactly what differs. Start with the [[Loops|Loops overview]].
* **Already training elsewhere**: Your Axolotl config, TRL script, or custom loop runs unchanged in a container. Baseten provisions the GPUs, syncs checkpoints as your job saves them, and deploys any checkpoint as a production endpoint. That's Truss Train, documented in this section.

If you match both or neither, the paths differ in who drives. With Truss Train, you hand Baseten a program: a batch job that runs to completion on hardware you declare. With Loops, your program calls Baseten: each training step is an API call to a live trainer, and a paired sampler serves the latest weights throughout. Loops covers LoRA fine-tuning and RL on a [[Supported base models|curated model list]] and is in early access; [request access](https://www.baseten.co/talk-to-us/loops-signup/) for your workspace. Truss Train runs any training code and is available to every workspace today.

|                | Truss Train                                       | [[Loops]]                                                                               |
| -------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Training code  | Any container image                               | Tinker-compatible Python (`import tinker`)                                                             |
| Models         | Any                                               | [[Supported base models]] only                                                  |
| Hardware       | You declare GPUs in a Truss config                | Baseten picks GPUs for the base model                                                                  |
| Inference path | Deploy any synced checkpoint with one CLI command | Sampler serves new weights live during training; deploy checkpoints when ready                         |
| Lifecycle      | Job runs to completion and exits                  | Session stays live until you run [[Loops CLI reference|`truss loops deactivate`]] |
| Availability   | All workspaces                                    | Early access                                                                                           |
| Documentation  | This section                                      | [[Loops|Loops docs]]                                                                          |

The rest of this page covers Truss Train.

## How Truss Train works

Baseten stores your checkpoints while the job runs and deploys any of them as a production endpoint. You don't download weights, re-upload them, or manage separate serving infrastructure. The core workflow is two commands:

```bash theme={"system"}
# Train your model
truss train push config.py

# Deploy from the checkpoint
truss train deploy_checkpoints --job-id <job_id>
```

From job submission to a served model:

1. **Define your job**: Declare compute, container image, runtime, and checkpointing in a Python config file.
2. **Submit it**: [[Training CLI reference|`truss train push`]] packages your code and starts the job on H100 or H200 GPUs, single-node or multi-node.
3. **Watch checkpoints sync**: Baseten stores each checkpoint your job saves.
4. **Deploy a checkpoint**: [[Training CLI reference|`truss train deploy_checkpoints`]] turns any synced checkpoint into a production endpoint.

## Supported frameworks

Truss Train is framework-agnostic: if it runs in a container, it runs here.

| Framework | Best for                                         | Example                                                                                                                |
| --------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| Axolotl   | Configuration-driven fine-tuning with LoRA/QLoRA | [oss-gpt-20b-axolotl](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/oss-gpt-20b-axolotl)               |
| TRL       | SFT, DPO, and GRPO with Hugging Face             | [oss-gpt-20b-lora-trl](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/oss-gpt-20b-lora-trl)             |
| TRL       | LoRA DPO fine-tuning                             | [qwen3-8b-lora-dpo-trl](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/qwen3-8b-lora-dpo-trl)           |
| VeRL      | Reinforcement learning with custom rewards       | [qwen3-8b-lora-verl](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/qwen3-8b-lora-verl)                 |
| MS-Swift  | Long-context and multilingual training           | [qwen3-30b-mswift-multinode](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/qwen3-30b-mswift-multinode) |

Browse the [ML Cookbook](https://github.com/basetenlabs/ml-cookbook) for more examples including multi-node training with FSDP and DeepSpeed.

## Key features

### Checkpoint management

Checkpoints sync automatically to Baseten storage during training. You can:

* **Deploy** any checkpoint as a production endpoint with [[Serve your trained model|`truss train deploy_checkpoints`]].
* **Download** checkpoints for local evaluation and analysis.
* **Resume** from any checkpoint if a job fails or you want to train further.

Learn more about [[Checkpoints|checkpointing]].

### BDN weight and data loading

Load model weights and training data through [[Storage and data ingestion|Baseten Delivery Network (BDN)]]. Mount weights from Hugging Face, S3, GCS, R2, or any HTTPS URL directly into your training container with no download code needed. BDN mirrors weights before compute is provisioned, then caches them for faster mounting on subsequent jobs.

See [[Storage and data ingestion|storage and data ingestion]] for setup details.

### Persistent caching

Speed up training iterations by caching models, datasets, and preprocessed data between jobs. The cache persists across training runs, so you don't re-download 70B models every time.

See the [[Cache|training cache]] guide for configuration options.

### Multi-node training

Scale training across multiple GPU nodes with InfiniBand networking. Baseten handles node orchestration, communication setup, and environment variables. You set `node_count` in your configuration.

Learn more about [[Multinode training|multi-node training]].

### Remote access

Connect to running training containers to debug, inspect state, and iterate without resubmitting. Baseten offers two options:

* **[[SSH access (Training)|SSH]]**: Connect from any OpenSSH client for terminal sessions and file transfer with `scp` or `sftp`.
* **[[VS Code and Cursor remote tunnels|VS Code & Cursor]]**: Connect from VS Code or Cursor Remote Tunnels for a full IDE experience.

See the [[Remote access|Remote access overview]] to choose between them.

## Next steps

  - **[[Get started (Training)|Get started]]**
    Run your first training job and deploy the result.
  

  - **[[Loops]]**
    Tinker-compatible SFT and async RL with checkpoint deploys to inference.
  

  - **[ML Cookbook](https://github.com/basetenlabs/ml-cookbook)**
    Production-ready examples for frameworks and models.
  

## Reference

* [[Training CLI reference|CLI reference]]
* [[Training SDK|SDK reference]]
* [[Overview (Training Api)|API reference]]

---
Part of [[Training Hub]]
