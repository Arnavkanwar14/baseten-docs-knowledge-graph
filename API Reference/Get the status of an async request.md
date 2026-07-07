---
tags: [baseten, api-reference]
source: https://docs.baseten.co/api-reference/get-the-status-of-an-async-request
---

> Returns the current status of an async model or chain request. Rate limited to 20 requests per second.

## OpenAPI

````yaml /reference/inference-api/inference-api-spec.json get /async_request/{request_id}
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
  /async_request/{request_id}:
    get:
      tags: []
      summary: Get the status of an async request.
      description: >-
        Returns the current status of an async model or chain request. Rate
        limited to 20 requests per second.
      operationId: getAsyncRequestStatus
      parameters:
        - $ref: '#/components/parameters/request_id'
      responses:
        '200':
          $ref: '#/components/responses/GetAsyncRequestStatusOutput'
        '401':
          $ref: '#/components/responses/Error'
        '429':
          $ref: '#/components/responses/Error'
components:
  parameters:
    request_id:
      name: request_id
      in: path
      required: true
      schema:
        type: string
      description: The ID of the async request.
  responses:
    GetAsyncRequestStatusOutput:
      description: Current status of an async request.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/AsyncRequestStatusResponse'
    Error:
      description: Error response.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  schemas:
    AsyncRequestStatusResponse:
      type: object
      required:
        - request_id
        - deployment_id
        - status
        - webhook_status
        - created_at
        - status_at
        - errors
      properties:
        request_id:
          type: string
          description: The ID of the async request.
        model_id:
          type: string
          description: >-
            The ID of the model that executed the request. Present for model
            requests.
        chain_id:
          type: string
          description: >-
            The ID of the chain that executed the request. Present for chain
            requests.
        deployment_id:
          type: string
          description: The ID of the deployment that executed the request.
        status:
          type: string
          enum:
            - QUEUED
            - IN_PROGRESS
            - SUCCEEDED
            - FAILED
            - EXPIRED
            - CANCELED
            - WEBHOOK_FAILED
          description: The status of the async request.
        webhook_status:
          type: string
          enum:
            - PENDING
            - SUCCEEDED
            - FAILED
            - CANCELED
            - NO_WEBHOOK_PROVIDED
          description: The status of sending the prediction result to the provided webhook.
        created_at:
          type: string
          description: The time in UTC at which the async request was created.
        status_at:
          type: string
          description: >-
            The time in UTC at which the async request's status was last
            updated.
        errors:
          type: array
          default: []
          items:
            $ref: '#/components/schemas/AsyncRequestError'
          description: >-
            Errors that occurred while processing the async request. Empty if no
            errors occurred.
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
    AsyncRequestError:
      type: object
      required:
        - code
        - message
      properties:
        code:
          type: string
          enum:
            - MODEL_PREDICT_ERROR
            - MODEL_PREDICT_TIMEOUT
            - MODEL_NOT_READY
            - MODEL_DOES_NOT_EXIST
            - MODEL_UNAVAILABLE
            - MODEL_INVALID_INPUT
            - ASYNC_REQUEST_NOT_SUPPORTED
            - INTERNAL_SERVER_ERROR
          description: The type of error that occurred.
        message:
          type: string
          description: Details of the error.
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
Part of [[API Reference Hub]]
