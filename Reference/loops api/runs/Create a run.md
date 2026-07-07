---
tags: [baseten, reference, loops-api]
source: https://docs.baseten.co/reference/loops-api/runs/create-a-run
---

> Creates a Loops run with an associated sampler in the given session.

## OpenAPI

````yaml post /v1/loops/runs
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
  /v1/loops/runs:
    post:
      summary: Create a Loops run.
      description: Creates a Loops run with an associated sampler in the given session.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateLoopsRunRequestV1'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateLoopsRunResponseV1'
      x-codeSamples:
        - lang: bash
          source: |-
            curl --request POST \
            --url https://api.baseten.co/v1/loops/runs \
            --header "Authorization: Bearer $BASETEN_API_KEY" \
            --data '{
              "session_id": null,
              "base_model": null,
              "name": null,
              "max_seq_len": null,
              "seed": null,
              "path": "bt://loops:k4q95w5/weights/step-100",
              "reuse_from_session_id": null
            }'
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/loops/runs"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "POST",
                url,
                headers=headers,
                json={'session_id': None, 'base_model': None, 'name': None, 'max_seq_len': None, 'seed': None, 'path': 'bt://loops:k4q95w5/weights/step-100', 'reuse_from_session_id': None}
            )

            print(response.text)
components:
  schemas:
    CreateLoopsRunRequestV1:
      properties:
        session_id:
          description: ID of the Loops session this run belongs to.
          title: Session Id
          type: string
        base_model:
          description: Base model ID (e.g. 'Qwen/Qwen3-8B').
          title: Base Model
          type: string
        name:
          anyOf:
            - maxLength: 255
              minLength: 1
              type: string
            - type: 'null'
          default: null
          description: >-
            Optional display name for the run. Defaults to the base model name
            when omitted.
          title: Name
        max_seq_len:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: >-
            Maximum prompt length (in tokens) the run must handle. Set this to
            the longest training example you plan to send. Defaults to the
            maximum supported by the model configuration.
          title: Max Seq Len
        lora_rank:
          default: 64
          description: LoRA rank.
          title: Lora Rank
          type: integer
        seed:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Random seed for reproducibility.
          title: Seed
        scale_down_delay_seconds:
          default: 3600
          description: >-
            Seconds of inactivity before the run scales to zero. Must be between
            1 and 3600 (1 hour). Defaults to 3600.
          exclusiveMinimum: 0
          maximum: 3600
          title: Scale Down Delay Seconds
          type: integer
        replicas:
          default: 1
          description: >-
            Number of data-parallel trainer replicas. Each replica is one full
            copy of the model's preset node group, so the trainer deployment
            runs (preset node_count * replicas) nodes (e.g. replicas=4 on a
            4-node preset → 16 nodes, 4 DP workers). Must be a positive integer.
            Defaults to 1.
          minimum: 1
          title: Replicas
          type: integer
        path:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: >-
            Optional bt:// URI of an existing checkpoint to load weights from on
            startup. Form: bt://loops:<run_id>/weights/<checkpoint_name>.
          examples:
            - bt://loops:k4q95w5/weights/step-100
          title: Path
        reuse_from_session_id:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: >-
            Optional Loops session ID whose trainer deployment should be reused
            for this run, sharing the infrastructure across sessions instead of
            provisioning fresh. The named session must belong to the same team.
            Reuse is best-effort: if the prior deployment is stopped, failed,
            its sampler is unhealthy, or this run requests replicas != 1, a new
            deployment is provisioned instead.
          title: Reuse From Session Id
      required:
        - session_id
        - base_model
      title: CreateLoopsRunRequestV1
      type: object
    CreateLoopsRunResponseV1:
      properties:
        run:
          $ref: '#/components/schemas/LoopsRunV1'
      required:
        - run
      title: CreateLoopsRunResponseV1
      type: object
    LoopsRunV1:
      properties:
        id:
          description: The run ID.
          title: Id
          type: string
        session_id:
          description: The session ID this run belongs to.
          title: Session Id
          type: string
        name:
          description: The run's display name.
          title: Name
          type: string
        base_model:
          description: The HuggingFace base model the run is fine-tuning.
          title: Base Model
          type: string
        base_url:
          description: The run's base URL.
          title: Base Url
          type: string
        created_at:
          description: Time the run was created in ISO 8601 format
          format: date-time
          title: Created At
          type: string
        sampler:
          $ref: '#/components/schemas/LoopsSamplerV1'
          description: The sampler bound to this run.
      required:
        - id
        - session_id
        - name
        - base_model
        - base_url
        - created_at
        - sampler
      title: LoopsRunV1
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
