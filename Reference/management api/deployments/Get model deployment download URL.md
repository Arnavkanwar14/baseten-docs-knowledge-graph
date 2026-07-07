---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/deployments/get-deployment-download-url
---

> Gets a presigned URL to download the truss tar file for a deployment.

## OpenAPI

````yaml get /v1/models/{model_id}/deployments/{deployment_id}/download
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
  /v1/models/{model_id}/deployments/{deployment_id}/download:
    parameters:
      - $ref: '#/components/parameters/model_id'
      - $ref: '#/components/parameters/deployment_id'
    get:
      summary: Gets a presigned download URL for a deployment's truss
      description: Gets a presigned URL to download the truss tar file for a deployment.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DownloadDeploymentResponseV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request GET \

            --url
            https://api.baseten.co/v1/models/{model_id}/deployments/{deployment_id}/download
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/models/{model_id}/deployments/{deployment_id}/download"

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
    DownloadDeploymentResponseV1:
      description: The response to a request to download a deployment's truss.
      properties:
        download_url:
          description: Presigned URL to download the truss tar file
          title: Download Url
          type: string
      required:
        - download_url
      title: DownloadDeploymentResponseV1
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
