---
tags: [baseten, reference, training-api]
source: https://docs.baseten.co/reference/training-api/get-training-project-cache-summary
---

> Get the cache summary for the most recent training job in the project.

## OpenAPI

````yaml get /v1/training_projects/{training_project_id}/cache/summary
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
  /v1/training_projects/{training_project_id}/cache/summary:
    parameters:
      - $ref: '#/components/parameters/training_project_id'
    get:
      summary: Get training project cache summary.
      description: Get the cache summary for the most recent training job in the project.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetCacheSummaryResponseV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request GET \

            --url
            https://api.baseten.co/v1/training_projects/{training_project_id}/cache/summary
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/training_projects/{training_project_id}/cache/summary"

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
  schemas:
    GetCacheSummaryResponseV1:
      description: Response for getting cache summary.
      properties:
        timestamp:
          description: Timestamp when the cache summary was captured
          title: Timestamp
          type: string
        project_id:
          description: Project ID associated with the cache
          title: Project Id
          type: string
        file_summaries:
          description: List of files in the cache
          items:
            $ref: '#/components/schemas/FileSummary'
          title: File Summaries
          type: array
      required:
        - timestamp
        - project_id
        - file_summaries
      title: GetCacheSummaryResponseV1
      type: object
    FileSummary:
      description: Information about a file in the cache.
      properties:
        path:
          description: Relative path of the file in the cache
          title: Path
          type: string
        size_bytes:
          description: Size of the file in bytes
          title: Size Bytes
          type: integer
        modified:
          description: Last modification time of the file
          title: Modified
          type: string
        file_type:
          description: Type of the file
          title: File Type
          type: string
        permissions:
          description: Permissions of the file
          title: Permissions
          type: string
      required:
        - path
        - size_bytes
        - modified
        - file_type
        - permissions
      title: FileSummary
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
