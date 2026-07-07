---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/deployments/get-deployment-config
---

> Returns the deployment's config. `output_format` query param picks the shape: 'raw' (config.yaml text), 'parsed' (dict with defaults), or 'both' (default).

## OpenAPI

````yaml get /v1/models/{model_id}/deployments/{deployment_id}/config
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
  /v1/models/{model_id}/deployments/{deployment_id}/config:
    parameters:
      - $ref: '#/components/parameters/model_id'
      - $ref: '#/components/parameters/deployment_id'
    get:
      summary: Gets a deployment's config
      description: >-
        Returns the deployment's config. `output_format` query param picks the
        shape: 'raw' (config.yaml text), 'parsed' (dict with defaults), or
        'both' (default).
      parameters:
        - name: output_format
          in: query
          required: false
          description: >-
            'raw': verbatim config.yaml with comments — not available for
            deployments created before 2026-04-30. 'parsed': dict with
            server-side defaults applied — always available. 'both': both fields
            populated.
          schema:
            $ref: '#/components/schemas/DeploymentConfigOutputFormat'
            default: both
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeploymentConfigResponseV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request GET \

            --url
            https://api.baseten.co/v1/models/{model_id}/deployments/{deployment_id}/config
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/models/{model_id}/deployments/{deployment_id}/config"

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
    deployment_id:
      schema:
        type: string
      name: deployment_id
      in: path
      required: true
  schemas:
    DeploymentConfigOutputFormat:
      enum:
        - raw
        - parsed
        - both
      title: DeploymentConfigOutputFormat
      type: string
    DeploymentConfigResponseV1:
      description: The config of a deployment. Fields are populated per `output_format`.
      properties:
        config:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          default: null
          description: The parsed config of the deployment.
          title: Config
        raw_config:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: >-
            The original config.yaml text — preserves comments, ordering,
            formatting.
          title: Raw Config
      title: DeploymentConfigResponseV1
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
