---
tags: [baseten, engines]
source: https://docs.baseten.co/engines/index
---

> Inference engines for embeddings, dense LLMs, MoE models, and Enterprise serving

export const EnginesSymbolLegend = () => > **Note:**
  Gated (🔒) features are enabled through Enterprise plans. <a href="mailto:support@baseten.co">Contact us</a> for more information.
;

Baseten engines optimize model inference for specific architectures using [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM). All engines mirror build artifacts to the [[Baseten Delivery Network]] automatically.

* **[[Overview (Bei)|BEI]]:** Embedding, reranking, and classification models on causal architectures with `FP8` and `FP4` quantization.
* **[[BEI-Bert]]:** Bidirectional BEI variant tuned for BERT-family encoders and cold-start-sensitive models under 4B parameters.
* **[[Overview (Engine Builder Llm)|Engine-Builder-LLM]]:** Dense text generation for Llama, Qwen, Mistral, and Gemma with lookahead decoding and multi-LoRA support.
* **[[Overview (Bis Llm)|BIS-LLM]]:** MoE and Enterprise serving with KV-aware routing, disaggregated prefill/decode, and Eagle/MTP speculation.

## Choose an engine

Pick the row below that matches what you're deploying. Cost, quality, and latency targets drive later choices (GPU, quantization, autoscaling) inside that engine.

* **Embedding, reranking, classification, or NER models:** use [[Overview (Bei)|BEI]] for decoder embedders (`Qwen3-Embedding`, `BAAI/bge`, `LlamaForSequenceClassification`) or [[BEI-Bert]] for BERT-family encoders (`BERT`, `ModernBERT`, `EuroBERT`, `XLM-RoBERTa`). NER lives on [[Named entity recognition|`BEI-Bert /predict_tokens`]].
* **Dense text-generation LLMs** (`Llama 3` or `4`, `Qwen 3` or `3.5`, `Mistral`, `Gemma`, `Phi`, `GPT-OSS-20B`): use [[Overview (Engine Builder Llm)|Engine-Builder-LLM]], with [[Speculative decoding|lookahead decoding]] and [[LoRA support|multi-LoRA]] available.
* **MoE models** (`GLM 5.x`, `Kimi K2.5` or `K2.6`, `DeepSeek V3`, `R1`, or `V4`, `MiniMax 2.5`, `Qwen3 MoE`, `GPT-OSS-120B`) **or workloads that need KV-cache-aware routing or disaggregated prefill/decode:** use [[Overview (Bis Llm)|BIS-LLM]]. Currently a co-engineering pilot.
* **Speech, image, video, or custom Python models:** ship a custom Truss. Browse [[Build with Baseten|model examples]] for Whisper, Orpheus, Flux, and other pre-built deployments, or see [[Build your model|build your first model]] for custom inference logic.

If your workload doesn't fit one of the rows above (custom architectures, hybrid pipelines, BIS-LLM pilot access, sizing for unusual traffic shapes), email [support@baseten.co](mailto:support@baseten.co) and an engineer will route you.

## Performance and operations

* [[Quantization guide]]: `FP8` and `FP4` trade-offs, GPU support, and per-engine options.
* [[Autoscaling engines]]: Token-based and request-based scaling for engine deployments.
* [[Deploy from cloud storage|Cloud storage deployment]]: Deploy engines from S3 or GCS instead of Hugging Face.
* [[Build with Baseten|Specialized model examples]]: Pre-built Truss examples for Whisper, Orpheus, Flux, and other dedicated deployments.

## Compare engines

| Feature                              | BIS-LLM | Engine-Builder-LLM | BEI | BEI-Bert | Notes                                                                            |
| ------------------------------------ | ------- | ------------------ | --- | -------- | -------------------------------------------------------------------------------- |
| **Quantization**                     | ✅       | ✅                  | ✅   | ❌        | BEI-Bert: `FP16`/`BF16` only.                                                    |
| **KV quantization**                  | ✅       | ✅                  | ⚠️  | ⚠️       | `FP8_KV`, `FP4_KV` supported.                                                    |
| **Lookahead decoding**               | ❌       | ✅                  | ❌   | ❌        | Engine-Builder-LLM (v1) only; BIS-LLM uses MTP/Eagle/N-gram speculation instead. |
| **Self-serviceable**                 | 🔒      | ✅                  | ✅   | ✅        | BIS-LLM requires Enterprise; other engines are self-serve.                       |
| **KV-routing**                       | 🔒      | ❌                  | ❌   | ❌        | BIS-LLM only.                                                                    |
| **Disaggregated serving**            | 🔒      | ❌                  | ❌   | ❌        | BIS-LLM Enterprise.                                                              |
| **Tool calling & structured output** | ✅       | ✅                  | ❌   | ❌        | Function calling support.                                                        |
| **Classification models**            | ❌       | ❌                  | ✅   | ✅        | Sequence classification.                                                         |
| **Embedding models**                 | ❌       | ❌                  | ✅   | ✅        | Embedding generation.                                                            |
| **Mixture-of-experts**               | ✅       | ⚠️ (Qwen3MoE only) | ❌   | ❌        | MoE models like `DeepSeek-R1`.                                                   |
| **MTP / Eagle / N-gram speculation** | 🔒      | ❌                  | ❌   | ❌        | v2 speculative decoding with `speculative_config`.                               |
| **HTTP request cancellation**        | ✅       | ⚠️                 | ✅   | ✅        | Engine-Builder-LLM: within the first 10ms only.                                  |
| **MultiModal Inputs**                | 🔒      | ❌                  | ⚠️  | ❌        | Selected architectures only.                                                     |

---
Part of [[Engines Hub]]
