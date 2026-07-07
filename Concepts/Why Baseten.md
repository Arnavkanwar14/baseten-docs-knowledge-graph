---
tags: [baseten, concepts]
source: https://docs.baseten.co/concepts/whybaseten
---

> Production training and inference on dedicated infrastructure, for teams that have outgrown shared API endpoints.

Baseten runs production-grade training and inference for AI teams that have outgrown shared API endpoints. Bring an open-source model, fine-tune one on dedicated H100 or H200 GPUs, or train from scratch. Deploy the result with one command and serve it on inference engines tuned for your model's architecture.

If you want to use a popular open-source model like DeepSeek, Qwen, or GLM, you can [[Model APIs|point the OpenAI SDK at Model APIs]] and skip deployment entirely. For everything else, the rest of this page covers what you get when you run your own model on Baseten.

## Production inference

Inference is the core of your product. When it fails, your application stops working. Baseten is built for mission-critical workloads with [high availability](https://status.baseten.co/), low latency, and performance at any scale.

### Engines built for your model architecture

An engine is the optimization runtime that compiles and serves your model. Baseten writes the engine layer so you don't have to: each engine handles quantization, tensor parallelism, KV cache management, and batching for a specific class of model.

Pick an engine based on your model's architecture:

* **[[Overview (Engine Builder Llm)|Engine-Builder-LLM]]:** Dense text-generation models compiled with TensorRT-LLM. Use for most open-source LLMs.
* **[[Overview (Bis Llm)|BIS-LLM]]:** Mixture-of-experts models like DeepSeek R1 and Qwen3 MoE, with KV-aware routing and distributed inference.
* **[[Overview (Bei)|BEI]]:** Embedding, reranking, and classification models with up to 1,400 client embeddings per second.

Select the engine in your `config.yaml`, or let Baseten pick one based on your model architecture. See the [engine selection guide](/engines) for Baseten's engines, or run a different inference server like vLLM or SGLang as a [[Custom Docker containers|custom Docker container]].

### Multi-cloud Capacity Management

GPUs are scarce, and any single cloud can run out of them in any given region. [[How Baseten works|Multi-cloud Capacity Management (MCM)]] is Baseten's control plane for provisioning capacity across clouds and regions. Deployments run active-active so a regional outage or capacity crunch doesn't take your endpoint offline.

For the mechanics, see [[How Baseten works]].

## Deployment modes

Baseten's training and inference stack runs the same way regardless of where the GPUs sit. Pick the mode that matches your data residency and operational posture.

### Baseten Cloud

Fully managed, multi-cloud inference and training. The fastest path to production, with horizontal scale and global latency optimization. Baseten runs the infrastructure so you can focus on your models.

### Self-hosted

The full Baseten stack inside your own VPC. Use this when you have strict data security, privacy, or sovereignty requirements. You keep full control over your data and networking while still getting Baseten's autoscaling and performance optimizations.

### Hybrid

Run core workloads in your VPC and burst to Baseten Cloud on demand. Combines strict compliance with elastic flex capacity.

> **Note:**
  [Talk to us](https://www.baseten.co/talk-to-us/) to set up a self-hosted or hybrid deployment.

## Training and customization

You can train models on Baseten too. Run a fine-tune or a from-scratch pre-train on dedicated H100 or H200 GPUs with Axolotl, TRL, VeRL, Megatron, or your own training code. Checkpoints sync to durable storage as training progresses, so a job failure doesn't cost you a run.

When training completes, [[Serve your trained model|`truss train deploy_checkpoints`]] deploys the checkpoint as an inference endpoint in one command. The same engines, autoscaling, and observability that serve fresh deployments also serve your trained model. No separate platform, no glue code between training and serving.

### Loops

[[Loops]] is Baseten's training SDK for workflows that don't fit a single batch job. It supports long-sequence training, async reinforcement learning, and one-click checkpoint deploys to the Baseten inference stack. Use Loops when you're iterating on a sampler-and-trainer loop or running RL against your own environment.

See [[Training on Baseten|Training overview]] for the full lifecycle and [[Loops|Loops overview]] for the SDK.

## Operate in production

Keep models healthy at scale with built-in observability, autoscaling, and secrets management.

* **[[Logs|Observability]]:** Real-time logs, metrics, and request traces for every deployment. Export to Datadog, Prometheus, Grafana, or New Relic, or read it all through Baseten's own dashboards.
* **[[Autoscaling]]:** Per-deployment concurrency targets, min and max replicas, scale-to-zero, and bounded scale-down delay.
* **[[Secrets (Organization)|Secrets and API keys]]:** Encrypted secret storage scoped to your workspace. Reference secrets in your `config.yaml` without checking them into a repo.
* **Compliance posture:** [SOC 2 Type II](https://www.baseten.co/blog/soc-2-type-2) and [HIPAA](https://www.baseten.co/blog/baseten-announces-hipaa-compliance), plus [[Regional environments|regional environments]] for data-residency requirements like GDPR.

## Serve models to your own customers

Baseten lets you serve models running on the platform to your own customers through [[Baseten Frontier Gateway|Frontier Gateway]]. The gateway sits between your customers and your dedicated deployment. Represent each customer (or plan, or project) as a group, mint API keys scoped to that group, set rate and usage limits that inherit through the tree, and receive usage events as billing webhooks. Calls hit your branded domain, not Baseten's.

> **Note:**
  Frontier Gateway is enabled for your workspace by a Baseten engineer. To turn it on, [talk to us](https://www.baseten.co/talk-to-us/).

## Next steps

  - **[[How Baseten works]]**
    The mechanics behind training, deployment, request routing, and autoscaling.
  

  - **[[Quickstart (Basics)|Quickstart]]**
    Make your first inference call in under two minutes.

---
Part of [[Concepts Hub]]
