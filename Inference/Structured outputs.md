---
tags: [baseten, inference]
source: https://docs.baseten.co/inference/structured-outputs
---

> JSON schema validation and controlled text generation across all engines

Structured outputs let you generate text that conforms to specific JSON schemas, providing reliable data extraction and controlled text generation. [[Model APIs]] support structured outputs. For self-deployed models, Baseten engines like [[Overview (Bis Llm)|BIS-LLM]] and [[Overview (Engine Builder Llm)|Engine-Builder-LLM]] support them, as do other inference frameworks like [[Deploy LLMs with vLLM|vLLM]] and [[Deploy LLMs with SGLang|SGLang]].

## Quick start

Structured outputs require two components: a Pydantic schema defining your expected output format, and an API call that enforces that schema.

### Define a schema

Define a Pydantic model whose fields describe the output you want:

```python schema.py theme={"system"}
from pydantic import BaseModel

class Task(BaseModel):
    title: str
    priority: str  # "low", "medium", "high"
    due_date: str
    description: str
```

Each field requires a type annotation. The model's response will conform to these types exactly.

### Generate structured output

Pass the schema to the parse method and read the typed result. The code is the same on both surfaces; only the base URL and model name differ.

  
    Point the client at `https://inference.baseten.co/v1` and pass a model slug from the [[Model APIs|supported models table]]:

    ```python structured_output.py theme={"system"}
    import os
    from pydantic import BaseModel
    from openai import OpenAI

    class Task(BaseModel):
        title: str
        priority: str
        due_date: str
        description: str

    client = OpenAI(
        api_key=os.environ['BASETEN_API_KEY'],
        base_url="https://inference.baseten.co/v1"
    )

    response = client.beta.chat.completions.parse(
        model="moonshotai/Kimi-K2.6",
        messages=[
            {"role": "user", "content": "Create a task for: Review the quarterly report by next Friday"}
        ],
        response_format=Task
    )

    task = response.choices[0].message.parsed
    print(f"Task: {task.title}")
    print(f"Priority: {task.priority}")
    ```
  

  
    Point the client at your deployment's production endpoint; the `model` field is required by the SDK but ignored by the deployment:

    ```python structured_output.py theme={"system"}
    import os
    from pydantic import BaseModel
    from openai import OpenAI

    class Task(BaseModel):
        title: str
        priority: str
        due_date: str
        description: str

    client = OpenAI(
        api_key=os.environ['BASETEN_API_KEY'],
        base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync/v1"
    )

    response = client.beta.chat.completions.parse(
        model="not-required",
        messages=[
            {"role": "user", "content": "Create a task for: Review the quarterly report by next Friday"}
        ],
        response_format=Task
    )

    task = response.choices[0].message.parsed
    print(f"Task: {task.title}")
    print(f"Priority: {task.priority}")
    ```
  

Running either version prints the parsed fields:

```text Output theme={"system"}
Task: Review the quarterly report
Priority: high
```

Pass your Pydantic class to `response_format` and use `beta.chat.completions.parse` instead of the regular `create` method.

The response includes a `parsed` attribute with your data already converted to a `Task` object, so no JSON parsing is needed.

### Use with LangChain

Because Baseten exposes an OpenAI-compatible endpoint, you can use LangChain's `ChatOpenAI` with `with_structured_output` by pointing `base_url` at Baseten:

```python langchain_structured_output.py theme={"system"}
import os
from pydantic import BaseModel
from langchain_openai import ChatOpenAI

class Task(BaseModel):
    title: str
    priority: str
    due_date: str
    description: str

# Model APIs: use "https://inference.baseten.co/v1" and a model slug.
# Dedicated deployment: use your production sync endpoint; the model field is
# required by the SDK but ignored by the deployment.
llm = ChatOpenAI(
    api_key=os.environ["BASETEN_API_KEY"],
    base_url="https://inference.baseten.co/v1",
    model="moonshotai/Kimi-K2.6",
)

structured_llm = llm.with_structured_output(Task)
task = structured_llm.invoke("Create a task for: Review the quarterly report by next Friday")

print(f"Task: {task.title}")
print(f"Priority: {task.priority}")
```

See the [[Integrations|LangChain integration]] for other ways to use Baseten with LangChain.

## Engine support

Structured outputs are compatible with:

* **Engine-Builder-LLM**, except when Lookahead speculative decoding is configured.
* **BIS-LLM**, except in some configurations, such as when the overlap scheduler is enabled.

### Model support

All Engine-Builder-LLM and BIS-LLM models support structured outputs with no extra configuration.

## Best practices

### Schema design

* **Keep schemas simple**: two to three levels of nesting for best results.
* **Use basic types**: str, int, float, bool when possible.
* **Set defaults**: Provide reasonable default values for optional fields.
* **Descriptive names**: Use clear, descriptive field names.

### Prompt engineering

* **Low temperature**: Use 0.1 to 0.3 for consistent outputs.
* **Provide schema**: Dump the model schema and few-shot examples into context.
* **Provide context**: Give background for complex schemas.

## Related

* [[Overview (Engine Builder Llm)|Engine-Builder-LLM overview]]: Dense model documentation.
* [[Overview (Bis Llm)|BIS-LLM overview]]: MoE model documentation.
* [[Quantization guide]]: `FP8`/`FP4` trade-offs.

---
Part of [[Inference Hub]]
