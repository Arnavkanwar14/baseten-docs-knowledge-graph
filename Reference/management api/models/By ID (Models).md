---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/models/gets-a-model-by-id
---

## OpenAPI

````yaml get /v1/models/{model_id}
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
    get:
      summary: Gets a model by ID
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ModelV1'
      x-codeSamples:
        - lang: bash
          source: |
            curl --request GET \
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
                "GET",
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
    ModelV1:
      description: A model.
      properties:
        id:
          description: Unique identifier of the model
          title: Id
          type: string
        created_at:
          description: Time the model was created in ISO 8601 format
          format: date-time
          title: Created At
          type: string
        name:
          description: Name of the model
          title: Name
          type: string
        deployments_count:
          description: Number of deployments of the model
          title: Deployments Count
          type: integer
        production_deployment_id:
          anyOf:
            - type: string
            - type: 'null'
          description: Unique identifier of the production deployment of the model
          title: Production Deployment Id
        development_deployment_id:
          anyOf:
            - type: string
            - type: 'null'
          description: Unique identifier of the development deployment of the model
          title: Development Deployment Id
        instance_type_name:
          description: Name of the instance type for the production deployment of the model
          title: Instance Type Name
          type: string
        team_name:
          description: Name of the team associated with the model.
          title: Team Name
          type: string
      required:
        - id
        - created_at
        - name
        - deployments_count
        - production_deployment_id
        - development_deployment_id
        - instance_type_name
        - team_name
      title: ModelV1
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
