---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/users/list-users
---

> Returns the workspace's members. Only actual joined members are returned; service accounts, invited users, and pending join requests are excluded.

## OpenAPI

````yaml get /v1/users
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
  /v1/users:
    get:
      summary: Lists users in the workspace
      description: >-
        Returns the workspace's members. Only actual joined members are
        returned; service accounts, invited users, and pending join requests are
        excluded.
      parameters:
        - name: cursor
          in: query
          required: false
          description: >-
            Opaque cursor returned by a previous page. Omit to fetch the first
            page.
          schema:
            anyOf:
              - type: string
              - type: 'null'
            default: null
            title: Cursor
        - name: limit
          in: query
          required: false
          description: Maximum number of items to return.
          schema:
            default: 100
            maximum: 1000
            minimum: 1
            title: Limit
            type: integer
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UsersResponseV1'
      x-codeSamples:
        - lang: bash
          source: |
            curl --request GET \
            --url https://api.baseten.co/v1/users \
            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/users"

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
    UsersResponseV1:
      description: A page of users in the caller's workspace.
      properties:
        items:
          description: Items in this page.
          items:
            $ref: '#/components/schemas/UserInfoV1'
          title: Items
          type: array
        pagination:
          $ref: '#/components/schemas/PaginationResponseV1'
          description: Pagination metadata for the page.
      required:
        - items
        - pagination
      title: UsersResponseV1
      type: object
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
