---
tags: [baseten, api-reference, non-regional]
source: https://docs.baseten.co/api-reference/non-regional/call-the-chain-deployment-associated-with-a-specified-environment
---

## OpenAPI

````yaml /reference/inference-api/inference-api-spec.json post /environments/{env_name}/run_remote
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
  /environments/{env_name}/run_remote:
    post:
      tags:
        - Non-Regional
      summary: Call the chain deployment associated with a specified environment.
      operationId: runRemote
      parameters:
        - $ref: '#/components/parameters/env_name'
      requestBody:
        $ref: '#/components/requestBodies/RunRemoteInput'
      responses:
        '200':
          $ref: '#/components/responses/RunRemoteOutput'
        '400':
          $ref: '#/components/responses/Error'
        '401':
          $ref: '#/components/responses/Error'
        '429':
          $ref: '#/components/responses/Error'
        '502':
          $ref: '#/components/responses/Error'
        '503':
          $ref: '#/components/responses/Error'
        '504':
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
    RunRemoteInput:
      required: true
      content:
        application/json:
          schema:
            description: JSON input matching the chain's `run_remote` method signature.
            type: object
  responses:
    RunRemoteOutput:
      description: Successful synchronous chain execution.
      content:
        application/json:
          schema:
            description: JSON-serializable output. The shape is defined by the chain.
            type: object
      headers:
        X-BASETEN-REQUEST-ID:
          $ref: '#/components/headers/X-BASETEN-REQUEST-ID'
    Error:
      description: Error response.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  headers:
    X-BASETEN-REQUEST-ID:
      schema:
        type: string
      description: Unique identifier for the request.
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
