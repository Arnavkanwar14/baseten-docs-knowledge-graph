---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/deployments/deactivate/deactivates-a-deployment
---

> Deactivates a deployment and returns the deactivation status.

## OpenAPI

````yaml post /v1/models/{model_id}/deployments/{deployment_id}/deactivate
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
  /v1/models/{model_id}/deployments/{deployment_id}/deactivate:
    parameters:
      - $ref: '#/components/parameters/model_id'
      - $ref: '#/components/parameters/deployment_id'
    post:
      summary: Deactivates a deployment
      description: Deactivates a deployment and returns the deactivation status.
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
            https://api.baseten.co/v1/models/{model_id}/deployments/{deployment_id}/deactivate
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/models/{model_id}/deployments/{deployment_id}/deactivate"

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
    model_id:
      schema:
        type: string
      name: model_id
      in: path
      required: true
    deployment_id:
      schema:
        type: string
      name: deployment_id
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
