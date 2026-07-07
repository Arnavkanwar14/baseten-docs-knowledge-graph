---
tags: [baseten, reference, loops-api]
source: https://docs.baseten.co/reference/loops-api/samplers/create-a-sampler
---

> Creates a standalone Loops sampler not linked to a run.

## OpenAPI

````yaml post /v1/loops/samplers
openapi: 3.1.0
info:
  description: REST API for management of Baseten resources
  title: Baseten management API
  version: 1.0.0
servers:
  - url: https://api.baseten.co
security:
  - BearerAuth: []
paths:
  /v1/loops/samplers:
    post:
      summary: Create a Loops sampler.
      description: Creates a standalone Loops sampler not linked to a run.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateLoopsSamplerRequestV1'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateLoopsSamplerResponseV1'
      x-codeSamples:
        - lang: bash
          source: |-
            curl --request POST \
            --url https://api.baseten.co/v1/loops/samplers \
            --header "Authorization: Bearer $BASETEN_API_KEY" \
            --data '{
              "session_id": null,
              "base_model": null,
              "max_seq_length": null,
              "model_path": "bt://loops:k4q95w5/sampler_weights/step-100",
              "reuse_from_session_id": null
            }'
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/loops/samplers"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "POST",
                url,
                headers=headers,
                json={'session_id': None, 'base_model': None, 'max_seq_length': None, 'model_path': 'bt://loops:k4q95w5/sampler_weights/step-100', 'reuse_from_session_id': None}
            )

            print(response.text)
components:
  schemas:
    CreateLoopsSamplerRequestV1:
      properties:
        session_id:
          description: ID of the Loops session this sampler belongs to.
          title: Session Id
          type: string
        base_model:
          description: Base model ID for standalone samplers (e.g., for baselines).
          title: Base Model
          type: string
        max_seq_length:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: >-
            Maximum prompt length (in tokens) the sampler must handle. Set this
            to the longest prompt you plan to send. Omit to use the default for
            the base model.
          title: Max Seq Length
        model_path:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: >-
            Optional bt:// URI of an existing sampler-target checkpoint to load
            weights from on startup. Form:
            bt://loops:<run_id>/sampler_weights/<checkpoint_name>.
          examples:
            - bt://loops:k4q95w5/sampler_weights/step-100
          title: Model Path
        reuse_from_session_id:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: >-
            Optional Loops session ID whose deployment should be reused for this
            sampler. Same best-effort semantics as the run endpoint.
          title: Reuse From Session Id
      required:
        - session_id
        - base_model
      title: CreateLoopsSamplerRequestV1
      type: object
    CreateLoopsSamplerResponseV1:
      properties:
        sampler:
          $ref: '#/components/schemas/LoopsSamplerV1'
      required:
        - sampler
      title: CreateLoopsSamplerResponseV1
      type: object
    LoopsSamplerV1:
      properties:
        id:
          title: Id
          type: string
        base_url:
          title: Base Url
          type: string
        base_model:
          description: The HuggingFace base model the sampler is serving.
          title: Base Model
          type: string
        created_at:
          description: Time the sampler was created in ISO 8601 format
          format: date-time
          title: Created At
          type: string
        model_id:
          description: Hashid of the underlying Baseten model.
          title: Model Id
          type: string
        deployment_id:
          description: Hashid of the specific model deployment (version).
          title: Deployment Id
          type: string
        status:
          $ref: '#/components/schemas/LoopsSamplerStatusV1'
          description: The sampler's current status.
      required:
        - id
        - base_url
        - base_model
        - created_at
        - model_id
        - deployment_id
        - status
      title: LoopsSamplerV1
      type: object
    LoopsSamplerStatusV1:
      description: The current status of a Loops sampler.
      properties:
        name:
          $ref: '#/components/schemas/DeploymentStatusV1'
          description: The current status of the Loops sampler.
      required:
        - name
      title: LoopsSamplerStatusV1
      type: object
    DeploymentStatusV1:
      description: The status of a deployment.
      enum:
        - BUILDING
        - DEPLOYING
        - DEPLOY_FAILED
        - LOADING_MODEL
        - ACTIVE
        - UNHEALTHY
        - BUILD_FAILED
        - BUILD_STOPPED
        - DEACTIVATING
        - INACTIVE
        - FAILED
        - UPDATING
        - SCALED_TO_ZERO
        - WAKING_UP
      title: DeploymentStatusV1
      type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Send `Authorization: Bearer <api_key>`. The legacy `Authorization:
        Api-Key <api_key>` scheme is also accepted.

````

---
Part of [[Loops Api (Reference)]]
