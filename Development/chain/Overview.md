---
tags: [baseten, development, chain]
source: https://docs.baseten.co/development/chain/overview
---

Chains is a framework for building robust, performant multi-step and multi-model
inference pipelines and deploying them to production. It addresses the common
challenges of managing latency, cost and dependencies for complex workflows,
while leveraging Truss' existing battle-tested performance, reliability and
developer toolkit.

<video autoPlay muted loop playsInline className="w-full aspect-video" src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/animation.mp4?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=79e3b77431748c2b54674fcb2ab94133" data-path="development/chain/images/animation.mp4" />

## User guides

Guides focus on specific features and use cases. Also refer to
[[Your first Chain|getting started]] and
[[Concepts (Chain)|general concepts]].

  - **[[Architecture and design|Design]]**
    How to structure your Chainlets, concurrency, file structure
  

  - **[[Local development|Local Dev]]**
    Iterating, Debugging, Testing, Mocking
  

  - **[[Deploy]]**
    Deploy your Chain on Baseten
  

  - **[[Invocation]]**
    Call your deployed Chain
  

  - **[[Watch]]**
    Live-patch deployed code
  

  - **[[Subclassing]]**
    Modularize and re-use Chainlet implementations
  

  - **[[Streaming]]**
    Streaming outputs, reducing latency, SSEs
  

  - **[[Binary IO]]**
    Performant serialization of numeric data
  

  - **[[Error handling|Error Propagation]]**
    Understanding and handling Chains errors
  

  - **[[Truss integration|Truss Integration]]**
    Integrate deployed Truss models with stubs
  

## From model to system

Some models are actually pipelines (for example, invoking a LLM involves sequentially
tokenizing the input, predicting the next token, and then decoding the predicted
tokens). These pipelines generally make sense to bundle together in a monolithic
deployment because they have the same dependencies, require the same compute
resources, and have a robust ecosystem of tooling to improve efficiency and
performance in a single deployment.
Many other pipelines and systems do not share these properties. Some examples
include:

* Running multiple different models in sequence.
* Chunking/partitioning a set of files and concatenating/organizing results.
* Pulling inputs from or saving outputs to a database or vector store.

Each step in these workflows has different hardware requirements, software
dependencies, and scaling needs so it doesn't make sense to bundle them in a
monolithic deployment. That's where Chains comes in.

## Principles behind Chains

Chains exists to help you build multi-step, multi-model pipelines. The
abstractions that Chains introduces are based on six opinionated principles:
three for architecture and three for developer experience.

**Architecture principles**

  
    Each step in the pipeline can set its own hardware requirements and
    software dependencies, separating GPU and CPU workloads.
  

  
    Each component has independent autoscaling parameters for targeted
    resource allocation, removing bottlenecks from your pipelines.
  

  
    Components specify a single public interface for flexible-but-safe
    composition and are reusable between projects
  

**Developer experience principles**

  
    Eliminate entire taxonomies of bugs by writing typed Python code and
    validating inputs, outputs, module initializations, function signatures,
    and even remote server configurations.
  

  
    Seamless local testing and cloud deployments: test Chains locally with
    support for mocking the output of any step and simplify your cloud
    deployment loops by separating large model deployments from quick
    updates to glue code.
  

  
    Use Chains to orchestrate existing model deployments, like pre-packaged
    models from Baseten’s model library, alongside new model pipelines built
    entirely within Chains.
  

## Hello World with Chains

Here's a simple Chain that says "hello" to each person in a list of provided
names:

```python hello_chain/hello.py theme={"system"}
import asyncio
import truss_chains as chains

# This Chainlet does the work.
class SayHello(chains.ChainletBase):

    async def run_remote(self, name: str) -> str:
        return f"Hello, {name}"

# This Chainlet orchestrates the work.
@chains.mark_entrypoint
class HelloAll(chains.ChainletBase):

    def __init__(self, say_hello_chainlet=chains.depends(SayHello)) -> None:
        self._say_hello = say_hello_chainlet

    async def run_remote(self, names: list[str]) -> str:
        tasks = []
        for name in names:
            tasks.append(asyncio.create_task(
                self._say_hello.run_remote(name)))

        return "\n".join(await asyncio.gather(*tasks))
```

This is a toy example, but it shows how Chains can be used to separate
preprocessing steps like chunking from workload execution steps. If SayHello
were an LLM instead of a simple string template, we could do a much more complex
action for each person on the list.

## What to build with Chains

  
    Connect to vector databases and augment LLM results with additional
    context information without introducing overhead to the model inference
    step.

    Try it yourself: [[Build a RAG pipeline with Chains|RAG Chain]].
  

  
    Transcribe large audio files by splitting them into smaller chunks and
    processing them in parallel. We've used this approach to process 10-hour
    files in minutes.

    Try it yourself: [[Transcribe audio with Chains|Audio Transcription Chain]].
  

  
    Build powerful experiences with optimal scaling in each step like:

    * AI phone calling (transcription + LLM + speech synthesis)
    * Multi-step image generation (SDXL + LoRAs + ControlNets)
    * Multimodal chat (LLM + vision + document parsing + audio)

    Since each stage runs on its hardware with independent auto-scaling,
    you can achieve better hardware utilization and save costs.
  

Get started by
[[Your first Chain|building and deploying your first chain]].

---
Part of [[Chain (Development)]]
