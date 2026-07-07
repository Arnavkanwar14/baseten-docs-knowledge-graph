---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/models/deletes-a-model-by-id
---

## OpenAPI

````yaml delete /v1/models/{model_id}
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
  /v1/models/{model_id}:
    parameters:
      - $ref: '#/components/parameters/model_id'
    delete:
      summary: Deletes a model by ID
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ModelTombstoneV1'
      x-codeSamples:
        - lang: bash
          source: |
            curl --request DELETE \
            --url https://api.baseten.co/v1/models/{model_id} \
            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/models/{model_id}"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "DELETE",
                url,
                headers=headers,
                json={}
            )

            print(response.text)
components:
  parameters:
    model_id:
      schema:
        type: string
      name: model_id
      in: path
      required: true
  schemas:
    ModelTombstoneV1:
      description: A model tombstone.
      properties:
        id:
          description: Unique identifier of the model
          title: Id
          type: string
        deleted:
          description: Whether the model was deleted
          title: Deleted
          type: boolean
      required:
        - id
        - deleted
      title: ModelTombstoneV1
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
Part of [[Management Api (Reference)]]
