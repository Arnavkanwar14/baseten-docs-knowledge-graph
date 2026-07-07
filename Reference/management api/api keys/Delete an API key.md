---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/api-keys/delete-an-api-key
---

> Deletes an API key by prefix and returns info about the API key.

## OpenAPI

````yaml delete /v1/api_keys/{api_key_prefix}
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
  /v1/api_keys/{api_key_prefix}:
    parameters:
      - $ref: '#/components/parameters/api_key_prefix'
    delete:
      summary: Deletes an API key by prefix
      description: Deletes an API key by prefix and returns info about the API key.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/APIKeyTombstoneV1'
      x-codeSamples:
        - lang: bash
          source: |
            curl --request DELETE \
            --url https://api.baseten.co/v1/api_keys/{api_key_prefix} \
            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/api_keys/{api_key_prefix}"

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
    api_key_prefix:
      schema:
        type: string
      name: api_key_prefix
      in: path
      required: true
  schemas:
    APIKeyTombstoneV1:
      description: An API key tombstone.
      properties:
        prefix:
          description: Unique prefix of the API key
          title: Prefix
          type: string
      required:
        - prefix
      title: APIKeyTombstoneV1
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
