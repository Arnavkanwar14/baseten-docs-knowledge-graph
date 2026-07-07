---
tags: [baseten, reference, loops-api]
source: https://docs.baseten.co/reference/loops-api/checkpoints/get-checkpoint-files
---

> Get presigned URLs for the files under a Loops checkpoint. Returns a paginated list.

## OpenAPI

````yaml get /v1/loops/checkpoints/{checkpoint_id}/files
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
  /v1/loops/checkpoints/{checkpoint_id}/files:
    parameters:
      - $ref: '#/components/parameters/checkpoint_id'
    get:
      summary: Get Loops checkpoint files.
      description: >-
        Get presigned URLs for the files under a Loops checkpoint. Returns a
        paginated list.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LoopsCheckpointFilesResponseV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request GET \

            --url
            https://api.baseten.co/v1/loops/checkpoints/{checkpoint_id}/files \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/loops/checkpoints/{checkpoint_id}/files"

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
    checkpoint_id:
      schema:
        type: string
      name: checkpoint_id
      in: path
      required: true
  schemas:
    LoopsCheckpointFilesResponseV1:
      description: Response with presigned URLs for files under a Loops checkpoint.
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
      title: LoopsCheckpointFilesResponseV1
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
Part of [[Loops Api (Reference)]]
