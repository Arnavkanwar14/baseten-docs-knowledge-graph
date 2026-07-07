---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/deployments/activate/activates-production-deployment
---

> Activates an inactive production deployment and returns the activation status.

## OpenAPI

````yaml post /v1/models/{model_id}/deployments/production/activate
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
  /v1/models/{model_id}/deployments/production/activate:
    parameters:
      - $ref: '#/components/parameters/model_id'
    post:
      summary: Activates a production deployment
      description: >-
        Activates an inactive production deployment and returns the activation
        status.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActivateResponseV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request POST \

            --url
            https://api.baseten.co/v1/models/{model_id}/deployments/production/activate
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/models/{model_id}/deployments/production/activate"

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
  schemas:
    ActivateResponseV1:
      description: The response to a request to activate a deployment.
      properties:
        success:
          default: true
          description: Whether the deployment was successfully activated
          title: Success
          type: boolean
      title: ActivateResponseV1
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
