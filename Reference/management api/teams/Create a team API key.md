---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/teams/creates-a-team-api-key
---

> Creates a team API key with the provided name and type. The API key is returned in the response.

## OpenAPI

````yaml post /v1/teams/{team_id}/api_keys
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
  /v1/teams/{team_id}/api_keys:
    parameters:
      - $ref: '#/components/parameters/team_id'
    post:
      summary: Creates a team API key
      description: >-
        Creates a team API key with the provided name and type. The API key is
        returned in the response.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateAPIKeyRequestV1'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/APIKeyV1'
      x-codeSamples:
        - lang: bash
          source: |-
            curl --request POST \
            --url https://api.baseten.co/v1/teams/{team_id}/api_keys \
            --header "Authorization: Bearer $BASETEN_API_KEY" \
            --data '{
              "name": "my-api-key",
              "type": "PERSONAL"
            }'
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/teams/{team_id}/api_keys"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "POST",
                url,
                headers=headers,
                json={'name': 'my-api-key', 'type': 'PERSONAL'}
            )

            print(response.text)
components:
  parameters:
    team_id:
      schema:
        type: string
      name: team_id
      in: path
      required: true
  schemas:
    CreateAPIKeyRequestV1:
      description: Request to create an API key.
      properties:
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
      required:
        - type
      title: CreateAPIKeyRequestV1
      type: object
    APIKeyV1:
      description: Represents an API key.
      properties:
        api_key:
          description: The API key string
          title: Api Key
          type: string
      required:
        - api_key
      title: APIKeyV1
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
