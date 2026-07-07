---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/users/get-the-current-user
---

> Returns info about the user making the request.

## OpenAPI

````yaml get /v1/users/me
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
  /v1/users/me:
    get:
      summary: Gets the authenticated user
      description: Returns info about the user making the request.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserInfoV1'
      x-codeSamples:
        - lang: bash
          source: |
            curl --request GET \
            --url https://api.baseten.co/v1/users/me \
            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/users/me"

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
    UserInfoV1:
      description: A Baseten user.
      properties:
        user_id:
          description: Unique identifier for the user
          title: User Id
          type: string
        email:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Email address of the user
          title: Email
        name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Display name of the user
          title: Name
        workspace_name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Name of the user's workspace
          title: Workspace Name
      required:
        - user_id
      title: UserInfoV1
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
