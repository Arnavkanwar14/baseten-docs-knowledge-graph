---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/chains/gets-all-chains
---

## OpenAPI

````yaml get /v1/chains
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
  /v1/chains:
    get:
      summary: Gets all chains
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChainsV1'
      x-codeSamples:
        - lang: bash
          source: |
            curl --request GET \
            --url https://api.baseten.co/v1/chains \
            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/chains"

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
    ChainsV1:
      description: A list of chains.
      properties:
        chains:
          items:
            $ref: '#/components/schemas/ChainV1'
          title: Chains
          type: array
      required:
        - chains
      title: ChainsV1
      type: object
    ChainV1:
      description: A chain.
      properties:
        id:
          description: Unique identifier of the chain
          title: Id
          type: string
        created_at:
          description: Time the chain was created in ISO 8601 format
          format: date-time
          title: Created At
          type: string
        name:
          description: Name of the chain
          title: Name
          type: string
        deployments_count:
          description: Number of deployments of the chain
          title: Deployments Count
          type: integer
        team_name:
          description: Name of the team associated with the chain
          title: Team Name
          type: string
      required:
        - id
        - created_at
        - name
        - deployments_count
        - team_name
      title: ChainV1
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
