---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/deployments/deactivate/deactivates-a-chain-deployment
---

> Deactivates a chain deployment and returns the deactivation status.

## OpenAPI

````yaml post /v1/chains/{chain_id}/deployments/{chain_deployment_id}/deactivate
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
  /v1/chains/{chain_id}/deployments/{chain_deployment_id}/deactivate:
    parameters:
      - $ref: '#/components/parameters/chain_id'
      - $ref: '#/components/parameters/chain_deployment_id'
    post:
      summary: Deactivates a chain deployment
      description: Deactivates a chain deployment and returns the deactivation status.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeactivateResponseV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request POST \

            --url
            https://api.baseten.co/v1/chains/{chain_id}/deployments/{chain_deployment_id}/deactivate
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/chains/{chain_id}/deployments/{chain_deployment_id}/deactivate"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "POST",
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
    DeactivateResponseV1:
      description: The response to a request to deactivate a deployment.
      properties:
        success:
          default: true
          description: Whether the deployment was successfully deactivated
          title: Success
          type: boolean
      title: DeactivateResponseV1
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
