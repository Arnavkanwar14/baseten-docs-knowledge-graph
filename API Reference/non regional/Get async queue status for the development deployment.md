---
tags: [baseten, api-reference, non-regional]
source: https://docs.baseten.co/api-reference/non-regional/get-async-queue-status-for-the-development-deployment
---

## OpenAPI

````yaml /reference/inference-api/inference-api-spec.json get /development/async_queue_status
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
  /development/async_queue_status:
    get:
      tags:
        - Non-Regional
      summary: Get async queue status for the development deployment.
      operationId: getAsyncQueueStatusDevelopment
      responses:
        '200':
          $ref: '#/components/responses/GetAsyncQueueStatusOutput'
        '401':
          $ref: '#/components/responses/Error'
        '429':
          $ref: '#/components/responses/Error'
components:
  responses:
    GetAsyncQueueStatusOutput:
      description: Async queue status for a deployment.
      content:
        application/json:
          schema:
            type: object
            required:
              - model_id
              - deployment_id
              - num_queued_requests
              - num_in_progress_requests
            properties:
              model_id:
                type: string
                description: The ID of the model.
              deployment_id:
                type: string
                description: The ID of the deployment.
              num_queued_requests:
                type: integer
                description: Number of requests with QUEUED status awaiting processing.
              num_in_progress_requests:
                type: integer
                description: Number of requests currently being processed by the model.
    Error:
      description: Error response.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  schemas:
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
