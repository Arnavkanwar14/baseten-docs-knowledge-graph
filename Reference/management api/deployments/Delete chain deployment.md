---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/deployments/deletes-a-chain-deployment-by-id
---

## OpenAPI

````yaml delete /v1/chains/{chain_id}/deployments/{chain_deployment_id}
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
  /v1/chains/{chain_id}/deployments/{chain_deployment_id}:
    parameters:
      - $ref: '#/components/parameters/chain_id'
      - $ref: '#/components/parameters/chain_deployment_id'
    delete:
      summary: Deletes a chain deployment by ID
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChainDeploymentTombstoneV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request DELETE \

            --url
            https://api.baseten.co/v1/chains/{chain_id}/deployments/{chain_deployment_id}
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/chains/{chain_id}/deployments/{chain_deployment_id}"

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
    chain_deployment_id:
      schema:
        type: string
      name: chain_deployment_id
      in: path
      required: true
  schemas:
    ChainDeploymentTombstoneV1:
      description: A chain deployment tombstone.
      properties:
        id:
          description: Unique identifier of the chain deployment
          title: Id
          type: string
        deleted:
          description: Whether the chain deployment was deleted
          title: Deleted
          type: boolean
        chain_id:
          description: Unique identifier of the chain
          title: Chain Id
          type: string
      required:
        - id
        - deleted
        - chain_id
      title: ChainDeploymentTombstoneV1
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
