---
tags: [baseten, reference, loops-api]
source: https://docs.baseten.co/reference/loops-api/checkpoints/validate-a-checkpoint
---

> Whether the caller can manage and use this checkpoint.

## OpenAPI

````yaml post /v1/loops/checkpoints/validate
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
  /v1/loops/checkpoints/validate:
    post:
      summary: Validate a Loops checkpoint bt:// URI.
      description: Whether the caller can manage and use this checkpoint.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ValidateLoopsCheckpointRequestV1'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ValidateLoopsCheckpointResponseV1'
      x-codeSamples:
        - lang: bash
          source: |-
            curl --request POST \
            --url https://api.baseten.co/v1/loops/checkpoints/validate \
            --header "Authorization: Bearer $BASETEN_API_KEY" \
            --data '{
              "checkpoint_path": "bt://loops:k4q95w5/sampler_weights/step-100"
            }'
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/loops/checkpoints/validate"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "POST",
                url,
                headers=headers,
                json={'checkpoint_path': 'bt://loops:k4q95w5/sampler_weights/step-100'}
            )

            print(response.text)
components:
  schemas:
    ValidateLoopsCheckpointRequestV1:
      description: Request body for ``POST /v1/loops/checkpoints/validate``.
      properties:
        checkpoint_path:
          description: >-
            bt:// URI of a sampler checkpoint. Form:
            bt://loops:<run_id>/sampler_weights/<checkpoint_name>.
          examples:
            - bt://loops:k4q95w5/sampler_weights/step-100
          title: Checkpoint Path
          type: string
      required:
        - checkpoint_path
      title: ValidateLoopsCheckpointRequestV1
      type: object
    ValidateLoopsCheckpointResponseV1:
      description: |-
        Response for ``POST /v1/loops/checkpoints/validate``. Empty on success;
        inaccessible or malformed paths raise 400.
      properties: {}
      title: ValidateLoopsCheckpointResponseV1
      type: object
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
