---
tags: [baseten, reference, training-api]
source: https://docs.baseten.co/reference/training-api/get-training-job-checkpoint-files
---

> Get presigned URLs for all checkpoint files for a training job.

## OpenAPI

````yaml get /v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoint_files
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
  /v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoint_files:
    parameters:
      - $ref: '#/components/parameters/training_project_id'
      - $ref: '#/components/parameters/training_job_id'
    get:
      summary: Get training job checkpoint files.
      description: Get presigned URLs for all checkpoint files for a training job.
      parameters:
        - name: page_size
          in: query
          required: false
          description: Max files per page (default 1000).
          schema:
            default: 1000
            minimum: 1
            title: Page Size
            type: integer
        - name: page_token
          in: query
          required: false
          description: Offset into the file list (default 0).
          schema:
            default: 0
            minimum: 0
            title: Page Token
            type: integer
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetTrainingJobCheckpointFilesResponseV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request GET \

            --url
            https://api.baseten.co/v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoint_files
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoint_files"

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
    GetTrainingJobCheckpointFilesResponseV1:
      description: >-
        A response to fetch presigned URLs for checkpoint files of a training
        job.
      properties:
        presigned_urls:
          description: List of presigned URLs for checkpoint files.
          items:
            $ref: '#/components/schemas/CheckpointFile'
          title: Presigned Urls
          type: array
        next_page_token:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: >-
            Token to use for fetching the next page of results. None when there
            are no more results.
          title: Next Page Token
        total_count:
          description: Total number of checkpoint files available.
          title: Total Count
          type: integer
      required:
        - presigned_urls
        - total_count
      title: GetTrainingJobCheckpointFilesResponseV1
      type: object
    CheckpointFile:
      properties:
        url:
          title: Url
          type: string
        relative_file_name:
          title: Relative File Name
          type: string
        node_rank:
          title: Node Rank
          type: integer
        size_bytes:
          title: Size Bytes
          type: integer
        last_modified:
          title: Last Modified
          type: string
      required:
        - url
        - relative_file_name
        - node_rank
        - size_bytes
        - last_modified
      title: CheckpointFile
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
