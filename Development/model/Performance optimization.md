---
tags: [baseten, development, model]
source: https://docs.baseten.co/development/model/performance-optimization
---

> Optimize model latency, throughput, and cost with Baseten engines

Model performance means optimizing every layer of your model serving infrastructure to balance four goals:

* **Latency**: How quickly does each user get output from the model?
* **Throughput**: How many requests can the deployment handle at once?
* **Cost**: How much does a standardized unit of work cost?
* **Quality**: Does your model consistently deliver high-quality output after optimization?

## Performance engines

Baseten provides three managed inference engines. Pick the one that matches your model architecture:

### [[Overview (Engine Builder Llm)|Engine-Builder-LLM]]: dense models

* **Best for**: Llama, Mistral, Qwen, and other causal language models.
* **Features**: TensorRT-LLM optimization, lookahead decoding, quantization.
* **Performance**: Tuned for low-latency, high-throughput dense LLM inference.

### [[Overview (Bis Llm)|BIS-LLM]]: MoE models

* **Best for**: DeepSeek, Mixtral, and other mixture-of-experts models.
* **Features**: V2 inference stack, expert routing, structured outputs.
* **Performance**: Tuned for large-scale MoE inference.

### [[Overview (Bei)|BEI]]: embedding models

* **Best for**: Sentence transformers, rerankers, classification models.
* **Features**: OpenAI-compatible API, optimized batching.
* **Performance**: Tuned for high-throughput embedding inference.

## Performance concepts

Detailed optimization guides live in the [[Quantization guide|performance concepts]] section:

* [[Quantization guide]]: FP8 and FP4 trade-offs and hardware requirements.
* [[Structured outputs]]: JSON schema validation and controlled generation.
* [[Function calling]]: tool use and function selection.
* [[Performance client]]: high-throughput client library.
* [[Deploy from cloud storage]]: GCS, S3, and Azure with Engine-Builder-LLM.
* [[Deploy with optimized inference engines|Deploy with inference engines]]: Baseten Training checkpoints with TRT-LLM.

## Quick performance wins

### Quantization

Reduce weight memory and improve throughput with post-training quantization:

```yaml config.yaml theme={"system"}
trt_llm:
  build:
    quantization_type: fp8  # FP8 weights, 16-bit KV cache
```

See the [[Quantization guide|quantization guide]] for all supported modes (`fp8`, `fp8_kv`, `fp4`, `fp4_kv`, `fp4_mlp_only`).

### Lookahead decoding

Accelerate inference for predictable content like code or JSON:

```yaml config.yaml theme={"system"}
trt_llm:
  build:
    speculator:
      speculative_decoding_mode: LOOKAHEAD_DECODING
      lookahead_windows_size: 3
```

### Performance client

Use the Rust-based client for high-throughput batched requests:

```bash Terminal theme={"system"}
uv pip install baseten-performance-client
```

## Where to start

1. **Choose your engine**: [Engine selection](/engines)
2. **Configure your model**: Engine-specific configuration guides
3. **Optimize performance**: [[Quantization guide|Performance concepts]]
4. **Deploy and monitor**: Use [[Performance client|performance client]] for maximum throughput

> **Tip:**
  Start with the default engine configuration, then apply quantization and other optimizations based on your specific performance requirements.

---
Part of [[Model (Development)]]
