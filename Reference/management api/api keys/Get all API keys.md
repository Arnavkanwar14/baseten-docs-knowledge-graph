---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/api-keys/lists-the-users-api-keys
---

> Lists all API keys your account has access to.

  ```json 200 theme={"system"}
  {
    "name": "my-api-key", 
    "type": "PERSONAL"
  }
  ```

## OpenAPI

````yaml get /v1/api_keys
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
  /v1/api_keys:
    get:
      summary: Lists the user's API keys (metadata only, no plain text keys)
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/APIKeysV1'
      x-codeSamples:
        - lang: bash
          source: |
            curl --request GET \
            --url https://api.baseten.co/v1/api_keys \
            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/api_keys"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "GET",
                url,
                headers=headers,
                json={}
            )

            print(response.text)
components:
  schemas:
    APIKeysV1:
      description: A list of API keys.
      properties:
        keys:
          description: A list of API key information
          items:
            $ref: '#/components/schemas/APIKeyInfoV1'
          title: Keys
          type: array
      required:
        - keys
      title: APIKeysV1
      type: object
    APIKeyInfoV1:
      description: Represents the metadata of an API key.
      properties:
        prefix:
          description: The prefix of the API key
          title: Prefix
          type: string
        name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Optional name for the API key
          examples:
            - my-api-key
          title: Name
        type:
          $ref: '#/components/schemas/APIKeyCategory'
          description: Type of the API key.
          examples:
            - PERSONAL
            - WORKSPACE_EXPORT_METRICS
            - WORKSPACE_INVOKE
            - WORKSPACE_MANAGE_ALL
        model_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          default: null
          description: >-
            List of model IDs to scope the API key to, only present if type is
            'WORKSPACE_EXPORT_METRICS' or 'WORKSPACE_INVOKE'
          examples:
            - - aaaaaaaa
          title: Model Ids
        team_name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: The name of the team associated with the API key
          title: Team Name
      required:
        - prefix
        - type
      title: APIKeyInfoV1
      type: object
    APIKeyCategory:
      description: Enum representing the category of an API key.
      enum:
        - PERSONAL
        - WORKSPACE_MANAGE_ALL
        - WORKSPACE_EXPORT_METRICS
        - WORKSPACE_INVOKE
      title: APIKeyCategory
      type: string
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
