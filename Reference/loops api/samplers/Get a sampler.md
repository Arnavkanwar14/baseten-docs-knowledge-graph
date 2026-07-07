---
tags: [baseten, reference, loops-api]
source: https://docs.baseten.co/reference/loops-api/samplers/get-a-sampler
---

> Fetch a Loops sampler by ID.

## OpenAPI

````yaml get /v1/loops/samplers/{sampler_id}
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
  /v1/loops/samplers/{sampler_id}:
    parameters:
      - $ref: '#/components/parameters/sampler_id'
    get:
      summary: Get a Loops sampler.
      description: Fetch a Loops sampler by ID.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetLoopsSamplerResponseV1'
      x-codeSamples:
        - lang: bash
          source: |
            curl --request GET \
            --url https://api.baseten.co/v1/loops/samplers/{sampler_id} \
            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/loops/samplers/{sampler_id}"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "GET",
                url,
                headers=headers,
                json={}
            )

            print(response.text)
components:
  parameters:
    sampler_id:
      schema:
        type: string
      name: sampler_id
      in: path
      required: true
  schemas:
    GetLoopsSamplerResponseV1:
      description: Response for ``GET /v1/loops/samplers/<sampler_id>``.
      properties:
        sampler:
          $ref: '#/components/schemas/LoopsSamplerV1'
          description: The Loops sampler.
      required:
        - sampler
      title: GetLoopsSamplerResponseV1
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
