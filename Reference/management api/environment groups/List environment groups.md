---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/environment-groups/list-environment-groups
---

> Lists the environment groups for the team specified in the path, or for the caller's organization default team when no team is specified.

## OpenAPI

````yaml get /v1/environment_groups
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
  /v1/environment_groups:
    get:
      summary: Lists environment groups
      description: >-
        Lists the environment groups for the team specified in the path, or for
        the caller's organization default team when no team is specified.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EnvironmentGroupsV1'
      x-codeSamples:
        - lang: bash
          source: |
            curl --request GET \
            --url https://api.baseten.co/v1/environment_groups \
            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/environment_groups"

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
    EnvironmentGroupsV1:
      description: A page of environment groups.
      properties:
        items:
          description: Items in this page.
          items:
            $ref: '#/components/schemas/EnvironmentGroupV1'
          title: Items
          type: array
        pagination:
          $ref: '#/components/schemas/PaginationResponseV1'
          description: Pagination metadata for the page.
      required:
        - items
        - pagination
      title: EnvironmentGroupsV1
      type: object
    EnvironmentGroupV1:
      description: >-
        A team-scoped grouping of same-named environments (e.g. "production",
        "staging").

        Restricting an environment group limits who can manage the environment
        of that name

        across every model and chain in the team.
      properties:
        name:
          description: >-
            Name of the environment group, matching the environment name it
            governs.
          examples:
            - staging
          title: Name
          type: string
        team_id:
          description: Unique identifier of the team the environment group belongs to.
          title: Team Id
          type: string
        team_name:
          description: Name of the team the environment group belongs to.
          title: Team Name
          type: string
        manage_access:
          $ref: '#/components/schemas/EnvironmentGroupManageAccessV1'
          description: Settings controlling who can manage this environment group.
      required:
        - name
        - team_id
        - team_name
        - manage_access
      title: EnvironmentGroupV1
      type: object
    PaginationResponseV1:
      properties:
        has_more:
          description: Whether more items exist after this page.
          title: Has More
          type: boolean
        cursor:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: >-
            Opaque cursor to pass into the next request. Null when there is no
            next page.
          title: Cursor
      required:
        - has_more
      title: PaginationResponseV1
      type: object
    EnvironmentGroupManageAccessV1:
      description: Who is allowed to manage an environment group.
      properties:
        is_restricted:
          description: Whether the environment is restricted to a specific set of users.
          title: Is Restricted
          type: boolean
        users:
          description: >-
            Users who can manage the environment while it is restricted,
            including organization and team admins who always have access. Empty
            when the environment is unrestricted.
          items:
            $ref: '#/components/schemas/EnvironmentGroupUserV1'
          title: Users
          type: array
      required:
        - is_restricted
      title: EnvironmentGroupManageAccessV1
      type: object
    EnvironmentGroupUserV1:
      description: A user referenced by an environment group's manage access.
      properties:
        user_id:
          description: Unique identifier for the user.
          title: User Id
          type: string
        email:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Email address of the user.
          title: Email
        name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Display name of the user.
          title: Name
      required:
        - user_id
      title: EnvironmentGroupUserV1
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
