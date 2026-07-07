---
tags: [baseten, reference, loops-api]
source: https://docs.baseten.co/reference/loops-api/deployments/deactivate-a-deployment
---

> Shut down a Loops deployment by ID. Saved checkpoints remain accessible. Resolving base_model -> deployment_id is the caller's responsibility — list deployments and pick the active one.

## OpenAPI

````yaml post /v1/loops/deployments/{deployment_id}/deactivate
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
  /v1/loops/deployments/{deployment_id}/deactivate:
    parameters:
      - $ref: '#/components/parameters/deployment_id'
    post:
      summary: Deactivate a Loops deployment.
      description: >-
        Shut down a Loops deployment by ID. Saved checkpoints remain accessible.
        Resolving base_model -> deployment_id is the caller's responsibility —
        list deployments and pick the active one.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeactivateLoopsDeploymentResponseV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request POST \

            --url
            https://api.baseten.co/v1/loops/deployments/{deployment_id}/deactivate
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/loops/deployments/{deployment_id}/deactivate"

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
    deployment_id:
      schema:
        type: string
      name: deployment_id
      in: path
      required: true
  schemas:
    DeactivateLoopsDeploymentResponseV1:
      description: Response for ``POST /v1/loops/deployments/<deployment_id>/deactivate``.
      properties:
        id:
          description: The deactivated Loops deployment ID.
          title: Id
          type: string
        base_model:
          description: The base model whose Loops deployment was deactivated.
          title: Base Model
          type: string
        user:
          $ref: '#/components/schemas/UserV1'
          description: The user who owned the Loops deployment.
      required:
        - id
        - base_model
        - user
      title: DeactivateLoopsDeploymentResponseV1
      type: object
    UserV1:
      description: A user.
      properties:
        email:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Email of the user.
          title: Email
      title: UserV1
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
