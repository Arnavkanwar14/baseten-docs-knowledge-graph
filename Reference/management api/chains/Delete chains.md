---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/chains/deletes-a-chain-by-id
---

## OpenAPI

````yaml delete /v1/chains/{chain_id}
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
  /v1/chains/{chain_id}:
    parameters:
      - $ref: '#/components/parameters/chain_id'
    delete:
      summary: Deletes a chain by ID
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChainTombstoneV1'
      x-codeSamples:
        - lang: bash
          source: |
            curl --request DELETE \
            --url https://api.baseten.co/v1/chains/{chain_id} \
            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/chains/{chain_id}"

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
    chain_id:
      schema:
        type: string
      name: chain_id
      in: path
      required: true
  schemas:
    ChainTombstoneV1:
      description: A chain tombstone.
      properties:
        id:
          description: Unique identifier of the chain
          title: Id
          type: string
        deleted:
          description: Whether the chain was deleted
          title: Deleted
          type: boolean
      required:
        - id
        - deleted
      title: ChainTombstoneV1
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
