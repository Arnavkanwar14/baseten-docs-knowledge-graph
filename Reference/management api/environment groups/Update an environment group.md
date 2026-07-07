---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/environment-groups/update-an-environment-group
---

> Sets whether the environment is restricted and replaces the list of users granted manage access. Targets the team specified in the path, or the caller's organization default team when no team is specified.

## OpenAPI

````yaml patch /v1/environment_groups/{env_name}
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
  /v1/environment_groups/{env_name}:
    parameters:
      - $ref: '#/components/parameters/env_name'
    patch:
      summary: Updates an environment group's restriction settings
      description: >-
        Sets whether the environment is restricted and replaces the list of
        users granted manage access. Targets the team specified in the path, or
        the caller's organization default team when no team is specified.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateEnvironmentGroupRequestV1'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EnvironmentGroupV1'
      x-codeSamples:
        - lang: bash
          source: |-
            curl --request PATCH \
            --url https://api.baseten.co/v1/environment_groups/{env_name} \
            --header "Authorization: Bearer $BASETEN_API_KEY" \
            --data '{
              "manage_access": null
            }'
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/environment_groups/{env_name}"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "PATCH",
                url,
                headers=headers,
                json={'manage_access': None}
            )

            print(response.text)
components:
  parameters:
    env_name:
      schema:
        type: string
      name: env_name
      in: path
      required: true
  schemas:
    UpdateEnvironmentGroupRequestV1:
      description: A request to update an existing environment group.
      properties:
        manage_access:
          anyOf:
            - $ref: '#/components/schemas/UpdateEnvironmentGroupManageAccessV1'
            - type: 'null'
          default: null
          description: >-
            Manage-access settings to apply. Omit to leave manage access
            unchanged.
      title: UpdateEnvironmentGroupRequestV1
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
    UpdateEnvironmentGroupManageAccessV1:
      description: Manage-access settings to apply to an environment group.
      properties:
        is_restricted:
          description: Whether to restrict this environment to a specific set of users.
          title: Is Restricted
          type: boolean
        user_ids:
          description: >-
            IDs of users granted manage access while restricted. Only meaningful
            when is_restricted is true.
          items:
            type: string
          title: User Ids
          type: array
      required:
        - is_restricted
      title: UpdateEnvironmentGroupManageAccessV1
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
