---
tags: [baseten, basics]
source: https://docs.baseten.co/quickstart
---

> Start running inference on Baseten.

Baseten provides inference endpoints you can call directly, with no infrastructure to manage.
Run popular open-source LLMs like DeepSeek V4 Pro, GLM 5.1, and Kimi K2.6 through APIs compatible with the OpenAI and Anthropic SDKs.
For the full list, see [[Model APIs|supported models]].

Set your base URL, set your API key, and send a request to an LLM hosted on Baseten.

## Set up your API key and SDK

Generate a [[API keys|personal API key]] from your [Baseten account](https://app.baseten.co/signup) and install a client SDK to call models.

  
    **Export your API key**

    ```bash theme={"system"}
    export BASETEN_API_KEY="paste-your-api-key-here"
    ```
  

  
    **Install a client SDK**

    
      ```bash Python theme={"system"}
      uv pip install openai
      ```

      ```bash JavaScript theme={"system"}
      npm install openai
      ```
    
  

## Run inference

Every Model API is compatible with the OpenAI SDK, with Anthropic SDK support in beta. Most also support [[Model APIs|tool calling, structured outputs, and more]].

Call a model using the OpenAI SDK. This example uses `zai-org/GLM-5`, but you can swap in any [[Model APIs|supported model]].

  
    Create a chat completion:

    ```python chat.py {5-6,10} theme={"system"}
    from openai import OpenAI
    import os

    client = OpenAI(
        base_url="https://inference.baseten.co/v1",
        api_key=os.environ["BASETEN_API_KEY"],
    )

    response = client.chat.completions.create(
        model="zai-org/GLM-5",
        messages=[
            {"role": "user", "content": "What is inference in machine learning?"}
        ],
    )

    print(response.choices[0].message.content)
    ```
  

  
    Create a chat completion:

    ```javascript chat.mjs {4-5,9} theme={"system"}
    import OpenAI from "openai";

    const client = new OpenAI({
        baseURL: "https://inference.baseten.co/v1",
        apiKey: process.env.BASETEN_API_KEY,
    });

    const response = await client.chat.completions.create({
        model: "zai-org/GLM-5",
        messages: [
            { role: "user", content: "What is inference in machine learning?" }
        ],
    });

    console.log(response.choices[0].message.content);
    ```
  

  
    ```bash theme={"system"}
    curl https://inference.baseten.co/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $BASETEN_API_KEY" \
      -d '{
        "model": "zai-org/GLM-5",
        "messages": [
          {"role": "user", "content": "What is inference in machine learning?"}
        ]
      }'
    ```
  

Success looks like this:

```output theme={"system"}
Inference in machine learning refers to the process of using a trained model
to make predictions or generate outputs from new input data...
```

## Stream the response

Streaming returns the response token by token as the model generates it, instead of waiting for the full reply. The first tokens appear immediately, which makes chat UIs and other interactive applications feel responsive.

  
    Set `stream=True` to receive tokens as they're generated:

    ```python stream.py {6} theme={"system"}
    stream = client.chat.completions.create(
        model="zai-org/GLM-5",
        messages=[
            {"role": "user", "content": "Write a haiku about machine learning."}
        ],
        stream=True,
    )

    for chunk in stream:
        if not chunk.choices:
            continue
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="")
    ```
  

  
    Set `stream: true` to receive tokens as they're generated:

    ```javascript stream.mjs {6} theme={"system"}
    const stream = await client.chat.completions.create({
        model: "zai-org/GLM-5",
        messages: [
            { role: "user", content: "Write a haiku about machine learning." }
        ],
        stream: true,
    });

    for await (const chunk of stream) {
        const content = chunk.choices[0]?.delta?.content;
        if (content) process.stdout.write(content);
    }
    ```
  

## Explore Model API features

  - **[[Structured outputs]]**
    Generate JSON that conforms to a schema you define.
  

  - **[[Function calling|Tool calling]]**
    Let the model invoke functions and use the results in its response.
  

  - **[[Reasoning]]**
    Enable extended thinking for multi-step problem solving.
  

## Next steps

  - **[[Baseten overview|Platform overview]]**
    Deploy models, run multi-step pipelines, train and fine-tune. See everything Baseten offers.
  

  - **[[Build your model|Deploy your first model]]**
    Go beyond Model APIs with a config-only Truss deployment on dedicated GPUs.

---
Part of [[Basics Hub]]
