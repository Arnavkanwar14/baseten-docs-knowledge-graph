---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/deployments/deletes-a-models-deployment-by-id
---

> Deletes a model's deployment by ID and returns the tombstone of the deployment.

## OpenAPI

````yaml delete /v1/models/{model_id}/deployments/{deployment_id}
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
  /v1/models/{model_id}/deployments/{deployment_id}:
    parameters:
      - $ref: '#/components/parameters/model_id'
      - $ref: '#/components/parameters/deployment_id'
    delete:
      summary: Deletes a model's deployment by ID
      description: >-
        Deletes a model's deployment by ID and returns the tombstone of the
        deployment.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeploymentTombstoneV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request DELETE \

            --url
            https://api.baseten.co/v1/models/{model_id}/deployments/{deployment_id}
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/models/{model_id}/deployments/{deployment_id}"

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
    deployment_id:
      schema:
        type: string
      name: deployment_id
      in: path
      required: true
  schemas:
    DeploymentTombstoneV1:
      description: A model deployment tombstone.
      properties:
        id:
          description: Unique identifier of the deployment
          title: Id
          type: string
        deleted:
          description: Whether the deployment was deleted
          title: Deleted
          type: boolean
        model_id:
          description: Unique identifier of the model
          title: Model Id
          type: string
      required:
        - id
        - deleted
        - model_id
      title: DeploymentTombstoneV1
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
