---
tags: [baseten, api-reference, non-regional]
source: https://docs.baseten.co/api-reference/non-regional/asynchronously-call-a-named-environment-of-a-model
---

## OpenAPI

````yaml /reference/inference-api/inference-api-spec.json post /environments/{env_name}/async_predict
openapi: 3.1.0
info:
  title: Baseten inference API
  version: 1.0.0
  description: >-
    API for invoking models and chains deployed on Baseten. Model endpoints use
    the `model-{model_id}` subdomain; chain endpoints use the `chain-{chain_id}`
    subdomain. All other path and query semantics are identical across both.

    For regional environments, the environment name is embedded in the hostname
    (e.g. `model-{model_id}-{env_name}.api.baseten.co`) and the path is bare
    (e.g. `/predict` instead of `/environments/{env_name}/predict`). See the
    "Regional" tagged endpoints. Path-based routes (`/production/*`,
    `/development/*`, `/environments/*`, `/deployment/*`) are not available on
    regional hostnames.
servers:
  - url: https://model-{model_id}.api.baseten.co
    description: Deployed model endpoints
    variables:
      model_id:
        description: The model's alphanumeric ID, found in your model dashboard.
        default: '{model_id}'
  - url: https://chain-{chain_id}.api.baseten.co
    description: Deployed chain endpoints
    variables:
      chain_id:
        description: The chain's alphanumeric ID, found in your chain dashboard.
        default: '{chain_id}'
  - url: https://model-{model_id}-{env_name}.api.baseten.co
    description: Regional model endpoints
    variables:
      model_id:
        description: The model's alphanumeric ID.
        default: '{model_id}'
      env_name:
        description: The regional environment name (e.g. `prod-us`).
        default: '{env_name}'
  - url: https://chain-{chain_id}-{env_name}.api.baseten.co
    description: Regional chain endpoints
    variables:
      chain_id:
        description: The chain's alphanumeric ID.
        default: '{chain_id}'
      env_name:
        description: The regional environment name (e.g. `prod-us`).
        default: '{env_name}'
security:
  - BearerAuth: []
tags:
  - name: Non-Regional
    description: >-
      Endpoints that use path-based routing (e.g. `/production/predict`,
      `/environments/{env_name}/predict`). Only available on standard hostnames
      (`model-{model_id}.api.baseten.co`), not regional hostnames.
  - name: Regional
    description: >-
      Endpoints that use bare paths (e.g. `/predict`, `/wake`). Only available
      on regional hostnames (`model-{model_id}-{env_name}.api.baseten.co`),
      where the environment is determined by the hostname.
paths:
  /environments/{env_name}/async_predict:
    post:
      tags:
        - Non-Regional
      summary: Asynchronously call a named environment of a model.
      operationId: asyncPredict
      parameters:
        - $ref: '#/components/parameters/env_name'
      requestBody:
        $ref: '#/components/requestBodies/AsyncPredictInput'
      responses:
        '201':
          $ref: '#/components/responses/AsyncPredictOutput'
        '400':
          $ref: '#/components/responses/Error'
        '401':
          $ref: '#/components/responses/Error'
        '413':
          $ref: '#/components/responses/Error'
        '429':
          $ref: '#/components/responses/Error'
        '503':
          $ref: '#/components/responses/Error'
components:
  parameters:
    env_name:
      name: env_name
      in: path
      required: true
      schema:
        type: string
      description: The name of the environment (e.g. `production`, `staging`).
  requestBodies:
    AsyncPredictInput:
      required: true
      description: There is a 256 KiB size limit on async predict request payloads.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/AsyncPredictRequest'
  responses:
    AsyncPredictOutput:
      description: Async predict request enqueued.
      content:
        application/json:
          schema:
            type: object
            required:
              - request_id
            properties:
              request_id:
                type: string
                description: The ID of the async request.
    Error:
      description: Error response.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  schemas:
    AsyncPredictRequest:
      type: object
      required:
        - model_input
      properties:
        model_input:
          type: object
          description: JSON-serializable model input.
        webhook_endpoint:
          type: string
          format: uri
          description: >-
            HTTPS URL to receive the prediction result via webhook. Both HTTP/2
            and HTTP/1.1 are supported. If omitted, the model must save outputs
            so they can be accessed later.
        priority:
          type: integer
          minimum: 0
          maximum: 2
          default: 0
          description: Priority of the request. Lower values are higher priority.
        max_time_in_queue_seconds:
          type: integer
          minimum: 10
          maximum: 259200
          default: 600
          description: >-
            Maximum time in seconds a request will spend in the queue before
            expiring. Must be between 10 seconds and 72 hours.
        inference_retry_config:
          $ref: '#/components/schemas/InferenceRetryConfig'
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: Human-readable error message.
        error_code:
          type: string
          description: Machine-readable error code.
          enum:
            - timeout
            - client_error
            - model_unavailable
            - model_not_ready
            - model_does_not_exist
            - rate_limited
            - payload_too_large
            - unauthorized
            - application_error
            - internal_baseten_error
        detail:
          type: string
          description: Additional error details, if available.
    InferenceRetryConfig:
      type: object
      description: Exponential backoff parameters for retrying predict requests.
      properties:
        max_attempts:
          type: integer
          minimum: 1
          maximum: 10
          default: 3
          description: Number of predict request attempts.
        initial_delay_ms:
          type: integer
          minimum: 0
          maximum: 10000
          default: 1000
          description: Minimum time between retries in milliseconds.
        max_delay_ms:
          type: integer
          minimum: 0
          maximum: 60000
          default: 5000
          description: Maximum time between retries in milliseconds.
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Pass your Baseten API key. Clients automatically send `Authorization:
        Bearer <key>`. Direct callers can also use `Authorization: Api-Key
        <key>`; both schemes are accepted.

````

---
Part of [[Non Regional (API Reference)]]
