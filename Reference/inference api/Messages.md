---
tags: [baseten, reference, inference-api]
source: https://docs.baseten.co/reference/inference-api/messages
---

> Create Anthropic Messages API requests against Baseten Model APIs.

> **Note:**
  Anthropic Messages API support is in **beta**. Behavior may change before general availability. For production workloads, use the [[Chat Completions|OpenAI Chat Completions API]].

> **Tip:**
  Download the [OpenAPI schema](/reference/inference-api/messages-openapi-spec.json) for code generation and client libraries.

[Model APIs](https://app.baseten.co/model-apis/create) accept requests in the [Anthropic Messages API](https://docs.anthropic.com/en/api/messages) format at `https://inference.baseten.co/v1/messages`.

## Call with the Anthropic SDK

The Anthropic SDK sends the API key as `x-api-key` by default. Baseten reads `Authorization`, so override `default_headers` when creating the client:

  
    ```python messages.py theme={"system"}
    import anthropic
    import os

    API_KEY = os.environ["BASETEN_API_KEY"]

    client = anthropic.Anthropic(
        base_url="https://inference.baseten.co",
        api_key=API_KEY,
        default_headers={"Authorization": f"Bearer {API_KEY}"},
    )

    response = client.messages.create(
        model="deepseek-ai/DeepSeek-V4-Pro",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Hello!"}
        ],
    )

    print(response.content[0].text)
    ```
  

  
    ```bash Request theme={"system"}
    curl https://inference.baseten.co/v1/messages \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $BASETEN_API_KEY" \
      -d '{
        "model": "deepseek-ai/DeepSeek-V4-Pro",
        "max_tokens": 1024,
        "messages": [
          {"role": "user", "content": "Hello!"}
        ]
      }'
    ```
  

## OpenAPI

````yaml reference/inference-api/messages-openapi-spec.json post /v1/messages
openapi: 3.1.0
info:
  title: Baseten Anthropic-Compatible Inference API
  version: 1.0.0
  description: >-
    Anthropic Messages API-compatible endpoint for Baseten Model APIs. Point the
    Anthropic SDK or any Messages API client at this endpoint to call supported
    models. Support is in beta; behavior may change before general availability.
servers:
  - url: https://inference.baseten.co
    description: Baseten Inference API.
security:
  - BearerAuth: []
paths:
  /v1/messages:
    post:
      tags:
        - Messages
      summary: Create a message
      description: >-
        Creates a response message for the provided conversation. Compatible
        with the Anthropic Messages API, so the Anthropic SDK works against this
        endpoint by changing `base_url` and overriding the default `x-api-key`
        header with `Authorization`. Support is in beta; behavior may change
        before general availability.
      operationId: createMessage
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MessagesRequest'
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MessagesResponse'
        '400':
          description: 'Bad request: invalid parameters.'
        '401':
          description: >-
            Unauthorized: invalid or missing API key. The Anthropic SDK's
            default `x-api-key` header is not accepted — pass `Authorization:
            Bearer <BASETEN_API_KEY>` or `Authorization: Api-Key
            <BASETEN_API_KEY>`.
        '404':
          description: Model not found or does not support the Messages API.
        '429':
          description: Rate limit exceeded.
        '500':
          description: Internal server error.
      x-codeSamples:
        - lang: python
          label: Python
          source: |-
            import anthropic
            import os

            API_KEY = os.environ["BASETEN_API_KEY"]

            client = anthropic.Anthropic(
                base_url="https://inference.baseten.co",
                api_key=API_KEY,
                default_headers={"Authorization": f"Bearer {API_KEY}"},
            )

            response = client.messages.create(
                model="deepseek-ai/DeepSeek-V4-Pro",
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": "Hello!"}
                ],
            )

            print(response.content[0].text)
        - lang: bash
          label: cURL
          source: |-
            curl https://inference.baseten.co/v1/messages \
              -H "Content-Type: application/json" \
              -H "Authorization: Bearer $BASETEN_API_KEY" \
              -d '{
                "model": "deepseek-ai/DeepSeek-V4-Pro",
                "max_tokens": 1024,
                "messages": [
                  {"role": "user", "content": "Hello!"}
                ]
              }'
components:
  schemas:
    MessagesRequest:
      additionalProperties: false
      type: object
      required:
        - model
        - messages
        - max_tokens
      title: MessagesRequest
      description: Request body for creating a message.
      properties:
        model:
          type: string
          title: Model
          description: >-
            The model slug to use. Find available models at [Model
            APIs](https://app.baseten.co/model-apis/create).
        messages:
          type: array
          title: Messages
          description: >-
            The conversation history as an ordered list of input messages.
            Alternating `user` and `assistant` roles are expected; the final
            message must be from the `user`.
          items:
            $ref: '#/components/schemas/InputMessage'
        max_tokens:
          type: integer
          minimum: 1
          title: Max Tokens
          description: >-
            The maximum number of tokens to generate in the response. Required
            by the Messages API. The response may be shorter if it finishes
            naturally or hits a stop sequence.
        system:
          anyOf:
            - type: string
            - type: array
              items:
                $ref: '#/components/schemas/TextBlock'
          title: System
          description: >-
            A system prompt that sets the model's behavior. Pass either a single
            string or an array of text content blocks.
        temperature:
          type: number
          minimum: 0
          maximum: 1
          default: 1
          title: Temperature
          description: >-
            Controls randomness. Lower values are more deterministic. Range: 0
            to 1.
        top_p:
          type: number
          exclusiveMinimum: 0
          maximum: 1
          title: Top P
          description: >-
            Nucleus sampling: only consider tokens with cumulative probability
            up to this value.
        top_k:
          type: integer
          minimum: 0
          title: Top K
          description: >-
            Limits token selection to the top K most probable tokens at each
            step.
        stop_sequences:
          type: array
          items:
            type: string
          title: Stop Sequences
          description: >-
            Custom text sequences that will stop generation. When a stop
            sequence is hit, `stop_reason` is `stop_sequence` and
            `stop_sequence` contains the matched string.
        stream:
          type: boolean
          default: false
          title: Stream
          description: >-
            If `true`, the response is streamed as server-sent events. Each
            event has a `type` such as `message_start`, `content_block_delta`,
            or `message_stop`.
        tools:
          type: array
          items:
            $ref: '#/components/schemas/ToolDefinition'
          title: Tools
          description: >-
            A list of tools the model may call. Each tool has a `name`,
            `description`, and `input_schema` (a JSON Schema object).
        tool_choice:
          $ref: '#/components/schemas/ToolChoice'
          description: Controls which tool (if any) the model must call.
        metadata:
          type: object
          title: Metadata
          description: >-
            An object describing metadata about the request. Supports `user_id`
            for abuse detection.
          properties:
            user_id:
              type: string
              description: An external identifier for the end user.
    MessagesResponse:
      additionalProperties: false
      type: object
      required:
        - id
        - type
        - role
        - content
        - model
        - stop_reason
        - usage
      title: MessagesResponse
      description: The message response returned by the model.
      properties:
        id:
          type: string
          description: A unique identifier for this message, such as `msg_abc123`.
        type:
          const: message
          type: string
          description: The object type, always `message`.
        role:
          const: assistant
          type: string
          description: The role of the generated message, always `assistant`.
        content:
          type: array
          items:
            anyOf:
              - $ref: '#/components/schemas/TextBlock'
              - $ref: '#/components/schemas/ToolUseBlock'
          description: >-
            An array of content blocks generated by the model. Text responses
            contain a single `text` block; responses that invoke tools contain
            `tool_use` blocks.
        model:
          type: string
          description: The model slug that produced the response.
        stop_reason:
          type: string
          enum:
            - end_turn
            - max_tokens
            - stop_sequence
            - tool_use
          description: >-
            Why the model stopped generating: `end_turn` (natural stop),
            `max_tokens` (hit the `max_tokens` limit), `stop_sequence` (matched
            a `stop_sequences` entry), or `tool_use` (model invoked a tool).
        stop_sequence:
          type: string
          nullable: true
          description: >-
            The stop sequence that was matched, if `stop_reason` is
            `stop_sequence`. Otherwise `null`.
        usage:
          $ref: '#/components/schemas/Usage'
          description: Token usage statistics for the request.
    InputMessage:
      additionalProperties: false
      type: object
      required:
        - role
        - content
      title: InputMessage
      description: A message in the conversation.
      properties:
        role:
          type: string
          enum:
            - user
            - assistant
          description: >-
            The role of the message author. System prompts are passed via the
            top-level `system` field, not as a message.
        content:
          anyOf:
            - type: string
            - type: array
              items:
                anyOf:
                  - $ref: '#/components/schemas/TextBlock'
                  - $ref: '#/components/schemas/ToolUseBlock'
                  - $ref: '#/components/schemas/ToolResultBlock'
          description: >-
            The message content. Pass a string for text-only messages or an
            array of content blocks for messages that include tool calls or tool
            results.
    TextBlock:
      additionalProperties: false
      type: object
      required:
        - type
        - text
      title: TextBlock
      description: A text content block.
      properties:
        type:
          const: text
          type: string
          description: The block type, always `text`.
        text:
          type: string
          description: The text content.
    ToolDefinition:
      additionalProperties: false
      type: object
      required:
        - name
        - input_schema
      title: ToolDefinition
      description: A tool the model can call.
      properties:
        name:
          type: string
          description: A unique name for the tool.
        description:
          type: string
          description: >-
            A description of what the tool does. The model uses this to decide
            when to call it.
        input_schema:
          type: object
          additionalProperties: true
          description: A JSON Schema object describing the tool's expected input.
    ToolChoice:
      oneOf:
        - type: object
          required:
            - type
          properties:
            type:
              const: auto
              type: string
              description: The model decides whether to call a tool.
            disable_parallel_tool_use:
              type: boolean
              default: false
              description: >-
                If `true`, restricts the model to calling at most one tool per
                response.
        - type: object
          required:
            - type
          properties:
            type:
              const: any
              type: string
              description: The model must call a tool but may pick which one.
        - type: object
          required:
            - type
            - name
          properties:
            type:
              const: tool
              type: string
              description: The model must call the named tool.
            name:
              type: string
              description: The exact name of the tool to call.
        - type: object
          required:
            - type
          properties:
            type:
              const: none
              type: string
              description: The model must not call any tool.
      title: ToolChoice
      description: Controls which tool (if any) the model calls.
    ToolUseBlock:
      additionalProperties: false
      type: object
      required:
        - type
        - id
        - name
        - input
      title: ToolUseBlock
      description: A tool use content block generated by the model.
      properties:
        type:
          const: tool_use
          type: string
          description: The block type, always `tool_use`.
        id:
          type: string
          description: >-
            A unique identifier for this tool call. Use this as `tool_use_id` in
            the matching tool result.
        name:
          type: string
          description: The name of the tool being called.
        input:
          type: object
          additionalProperties: true
          description: >-
            The arguments passed to the tool, matching the tool's
            `input_schema`.
    Usage:
      additionalProperties: true
      type: object
      title: Usage
      description: Token usage statistics.
      properties:
        input_tokens:
          type: integer
          description: The number of input tokens processed.
        output_tokens:
          type: integer
          description: The number of output tokens generated.
        cache_read_input_tokens:
          type: integer
          description: >-
            The number of input tokens served from cache. Counted as a subset of
            `input_tokens`, not in addition to it (unlike the Anthropic API,
            where `input_tokens` excludes cached tokens). Caching is automatic;
            no `cache_control` blocks are required and there is no
            `cache_creation_input_tokens` field. Some models omit this field.
    ToolResultBlock:
      additionalProperties: false
      type: object
      required:
        - type
        - tool_use_id
        - content
      title: ToolResultBlock
      description: >-
        A tool result content block supplied by the user in response to a tool
        call.
      properties:
        type:
          const: tool_result
          type: string
          description: The block type, always `tool_result`.
        tool_use_id:
          type: string
          description: The `id` of the `tool_use` block this result responds to.
        content:
          anyOf:
            - type: string
            - type: array
              items:
                $ref: '#/components/schemas/TextBlock'
          description: >-
            The tool's output. Pass a string for simple results or an array of
            text blocks for structured output.
        is_error:
          type: boolean
          default: false
          description: Set to `true` if the tool call raised an error.
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Pass your Baseten API key. Clients automatically send `Authorization:
        Bearer <key>`. Direct callers can also use `Authorization: Api-Key
        <key>`; both schemes are accepted. The Anthropic SDK's default
        `x-api-key` header is not accepted; override `default_headers` to send
        `Authorization` instead.

````

---
Part of [[Inference Api (Reference)]]
