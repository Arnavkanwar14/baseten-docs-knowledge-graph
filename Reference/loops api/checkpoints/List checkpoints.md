---
tags: [baseten, reference, loops-api]
source: https://docs.baseten.co/reference/loops-api/checkpoints/list-checkpoints
---

> List Loops checkpoints filtered by run id, base model, or bt:// URI. Provide exactly one filter.

## OpenAPI

````yaml get /v1/loops/checkpoints
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
  /v1/loops/checkpoints:
    get:
      summary: List Loops checkpoints.
      description: >-
        List Loops checkpoints filtered by run id, base model, or bt:// URI.
        Provide exactly one filter.
      parameters:
        - name: run_id
          in: query
          required: false
          description: Filter by run ID. Returns all checkpoints saved by the run.
          schema:
            anyOf:
              - type: string
              - type: 'null'
            default: null
            examples:
              - k4q95w5
            title: Run Id
        - name: base_model
          in: query
          required: false
          description: >-
            Filter by base model. Returns checkpoints across the caller's runs
            of this base model.
          schema:
            anyOf:
              - type: string
              - type: 'null'
            default: null
            examples:
              - Qwen/Qwen3-8B
            title: Base Model
        - name: checkpoint_path
          in: query
          required: false
          description: >-
            bt:// URI of a Loops checkpoint. Form:
            bt://loops:<run_id>/(weights|sampler_weights)/<checkpoint_name>.
          schema:
            anyOf:
              - type: string
              - type: 'null'
            default: null
            examples:
              - bt://loops:k4q95w5/sampler_weights/step-100
            title: Checkpoint Path
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListLoopsCheckpointsResponseV1'
      x-codeSamples:
        - lang: bash
          source: |
            curl --request GET \
            --url https://api.baseten.co/v1/loops/checkpoints \
            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/loops/checkpoints"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "GET",
                url,
                headers=headers,
                json={}
            )

            print(response.text)
components:
  schemas:
    ListLoopsCheckpointsResponseV1:
      description: Checkpoints matching the query filter.
      properties:
        checkpoints:
          description: Matching checkpoints.
          items:
            $ref: '#/components/schemas/LoopsCheckpointV1'
          title: Checkpoints
          type: array
      required:
        - checkpoints
      title: ListLoopsCheckpointsResponseV1
      type: object
    LoopsCheckpointV1:
      description: A checkpoint saved by a Loops run.
      properties:
        checkpoint_id:
          description: The ID of the checkpoint.
          title: Checkpoint Id
          type: string
        created_at:
          description: The timestamp of the checkpoint in ISO 8601 format.
          format: date-time
          title: Created At
          type: string
        checkpoint_type:
          description: The type of checkpoint.
          title: Checkpoint Type
          type: string
        base_model:
          anyOf:
            - type: string
            - type: 'null'
          description: The base model of the checkpoint.
          title: Base Model
        lora_adapter_config:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          description: The adapter config of the checkpoint.
          title: Lora Adapter Config
        size_bytes:
          description: The size of the checkpoint in bytes.
          title: Size Bytes
          type: integer
        sync_status:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: 'Sync state of the checkpoint: SYNCING or COMPLETE.'
          title: Sync Status
        id:
          description: The checkpoint ID.
          title: Id
          type: string
        run_id:
          description: The ID of the run that produced the checkpoint.
          title: Run Id
          type: string
        target:
          $ref: '#/components/schemas/TrainerCheckpointTarget'
          description: Whether this checkpoint is loadable by the sampler or by the run.
      required:
        - checkpoint_id
        - created_at
        - checkpoint_type
        - base_model
        - lora_adapter_config
        - size_bytes
        - id
        - run_id
        - target
      title: LoopsCheckpointV1
      type: object
    TrainerCheckpointTarget:
      description: >-
        Whether a TrainerServerCheckpoint is loadable by the sampler or the
        trainer.

        SAMPLER checkpoints are consumed by the sampling server for inference;

        TRAINER checkpoints capture full trainer state for resuming training.

        Mirrored in the bt:// URI as

        ``bt://loops:<trainer_id>/(sampler_weights|weights)/<name>``.
      enum:
        - sampler
        - trainer
      title: TrainerCheckpointTarget
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
