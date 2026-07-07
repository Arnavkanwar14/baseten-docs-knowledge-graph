---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/secrets/gets-all-secrets
---

## OpenAPI

````yaml get /v1/secrets
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
  /v1/secrets:
    get:
      summary: Gets all secrets (metadata only, no plain text keys)
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SecretsV1'
      x-codeSamples:
        - lang: bash
          source: |
            curl --request GET \
            --url https://api.baseten.co/v1/secrets \
            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/secrets"

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
    SecretsV1:
      description: A list of Baseten secrets.
      properties:
        secrets:
          items:
            $ref: '#/components/schemas/SecretV1'
          title: Secrets
          type: array
      required:
        - secrets
      title: SecretsV1
      type: object
    SecretV1:
      description: A Baseten secret. Note that we do not support retrieving secret values.
      properties:
        id:
          description: Stable identifier for the secret. Unchanged across rotation.
          examples:
            - 3kZ9xqd
          title: Id
          type: string
        created_at:
          description: Time the secret was created in ISO 8601 format
          format: date-time
          title: Created At
          type: string
        name:
          description: Name of the secret
          title: Name
          type: string
        team_name:
          description: Name of the team the secret belongs to
          title: Team Name
          type: string
      required:
        - id
        - created_at
        - name
        - team_name
      title: SecretV1
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
