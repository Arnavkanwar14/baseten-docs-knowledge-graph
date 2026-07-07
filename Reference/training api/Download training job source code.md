---
tags: [baseten, reference, training-api]
source: https://docs.baseten.co/reference/training-api/download-training-job
---

> Get the uploaded training job as a S3 Artifact

## OpenAPI

````yaml get /v1/training_projects/{training_project_id}/jobs/{training_job_id}/download
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
  /v1/training_projects/{training_project_id}/jobs/{training_job_id}/download:
    parameters:
      - $ref: '#/components/parameters/training_project_id'
      - $ref: '#/components/parameters/training_job_id'
    get:
      summary: Get the uploaded training job as a S3 Artifact
      description: Get the uploaded training job as a S3 Artifact
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DownloadTrainingJobResponseV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request GET \

            --url
            https://api.baseten.co/v1/training_projects/{training_project_id}/jobs/{training_job_id}/download
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/training_projects/{training_project_id}/jobs/{training_job_id}/download"

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
    training_project_id:
      schema:
        type: string
      name: training_project_id
      in: path
      required: true
    training_job_id:
      schema:
        type: string
      name: training_job_id
      in: path
      required: true
  schemas:
    DownloadTrainingJobResponseV1:
      description: A response that includes the artifacts for a training job
      properties:
        artifact_presigned_urls:
          description: Presigned URL's for the artifacts
          items:
            type: string
          title: Artifact Presigned Urls
          type: array
      required:
        - artifact_presigned_urls
      title: DownloadTrainingJobResponseV1
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
Part of [[Training Api (Reference)]]
