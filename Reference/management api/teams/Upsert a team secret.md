---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/teams/upserts-a-team-secret
---

> Creates a new secret or updates an existing secret if one with the provided name already exists. The name and creation date of the created or updated secret is returned. This secret belongs to the specified team

## OpenAPI

````yaml post /v1/teams/{team_id}/secrets
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
  /v1/teams/{team_id}/secrets:
    parameters:
      - $ref: '#/components/parameters/team_id'
    post:
      summary: Upserts a secret in a team
      description: >-
        Creates a new secret or updates an existing secret if one with the
        provided name already exists. The name and creation date of the created
        or updated secret is returned. This secret belongs to the specified team
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpsertSecretRequestV1'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SecretV1'
      x-codeSamples:
        - lang: bash
          source: |-
            curl --request POST \
            --url https://api.baseten.co/v1/teams/{team_id}/secrets \
            --header "Authorization: Bearer $BASETEN_API_KEY" \
            --data '{
              "name": "my_secret",
              "value": "my_secret_value"
            }'
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/teams/{team_id}/secrets"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "POST",
                url,
                headers=headers,
                json={'name': 'my_secret', 'value': 'my_secret_value'}
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
    UpsertSecretRequestV1:
      description: A request to create or update a Baseten secret by name.
      properties:
        name:
          description: Name of the new or existing secret
          examples:
            - my_secret
          title: Name
          type: string
        value:
          description: Value of the secret
          examples:
            - my_secret_value
          title: Value
          type: string
      required:
        - name
        - value
      title: UpsertSecretRequestV1
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
