---
tags: [baseten, reference, loops-api]
source: https://docs.baseten.co/reference/loops-api/sessions/get-a-session
---

> Fetch a Loops session by ID.

## OpenAPI

````yaml get /v1/loops/sessions/{session_id}
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
  /v1/loops/sessions/{session_id}:
    parameters:
      - $ref: '#/components/parameters/session_id'
    get:
      summary: Get a Loops session.
      description: Fetch a Loops session by ID.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetLoopsSessionResponseV1'
      x-codeSamples:
        - lang: bash
          source: |
            curl --request GET \
            --url https://api.baseten.co/v1/loops/sessions/{session_id} \
            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/loops/sessions/{session_id}"

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
    session_id:
      schema:
        type: string
      name: session_id
      in: path
      required: true
  schemas:
    GetLoopsSessionResponseV1:
      description: Response for ``GET /v1/loops/sessions/<session_id>``.
      properties:
        session:
          $ref: '#/components/schemas/LoopsSessionV1'
          description: The Loops session.
      required:
        - session
      title: GetLoopsSessionResponseV1
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
