---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/teams/gets-a-team-by-id
---

> Returns a team the authenticated user has access to.

## OpenAPI

````yaml get /v1/teams/{team_id}
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
  /v1/teams/{team_id}:
    parameters:
      - $ref: '#/components/parameters/team_id'
    get:
      summary: Gets a team by ID
      description: Returns a team the authenticated user has access to.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TeamV1'
      x-codeSamples:
        - lang: bash
          source: |
            curl --request GET \
            --url https://api.baseten.co/v1/teams/{team_id} \
            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/teams/{team_id}"

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
    team_id:
      schema:
        type: string
      name: team_id
      in: path
      required: true
  schemas:
    TeamV1:
      description: A team.
      properties:
        id:
          description: Unique identifier of the team
          title: Id
          type: string
        name:
          description: Name of the team
          title: Name
          type: string
        default:
          type: boolean
          description: Whether this is the default team for the organization
          title: Default
        created_at:
          description: Time the team was created in ISO 8601 format
          format: date-time
          title: Created At
          type: string
      required:
        - id
        - name
        - default
        - created_at
      title: TeamV1
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
