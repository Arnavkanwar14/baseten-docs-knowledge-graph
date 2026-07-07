---
tags: [baseten, reference, loops-api]
source: https://docs.baseten.co/reference/loops-api/sessions/create-a-session
---

> Creates a Loops session scoped to the calling org.

## OpenAPI

````yaml post /v1/loops/sessions
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
  /v1/loops/sessions:
    post:
      summary: Create a Loops session.
      description: Creates a Loops session scoped to the calling org.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateLoopsSessionResponseV1'
      x-codeSamples:
        - lang: bash
          source: |
            curl --request POST \
            --url https://api.baseten.co/v1/loops/sessions \
            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/loops/sessions"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "POST",
                url,
                headers=headers,
                json={}
            )

            print(response.text)
components:
  schemas:
    CreateLoopsSessionResponseV1:
      properties:
        session:
          $ref: '#/components/schemas/LoopsSessionV1'
      required:
        - session
      title: CreateLoopsSessionResponseV1
      type: object
    LoopsSessionV1:
      properties:
        id:
          title: Id
          type: string
      required:
        - id
      title: LoopsSessionV1
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
