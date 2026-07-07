---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/model-apis/gets-all-model-apis
---

> List Model APIs visible to the caller. By default returns the full catalog; pass `added_only=true` to restrict to Model APIs the workspace has added.

## OpenAPI

````yaml get /v1/model_apis
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
  /v1/model_apis:
    get:
      summary: List Model APIs.
      description: >-
        List Model APIs visible to the caller. By default returns the full
        catalog; pass `added_only=true` to restrict to Model APIs the workspace
        has added.
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
        - name: added_only
          in: query
          required: false
          description: >-
            When true, restrict the result to Model APIs the workspace has
            added. Defaults to the full visible catalog.
          schema:
            default: false
            title: Added Only
            type: boolean
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ModelAPIsResponseV1'
      x-codeSamples:
        - lang: bash
          source: |
            curl --request GET \
            --url https://api.baseten.co/v1/model_apis \
            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/model_apis"

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
    ModelAPIsResponseV1:
      description: Page of Model APIs visible to the caller.
      properties:
        items:
          description: Items in this page.
          items:
            $ref: '#/components/schemas/ModelAPIV1'
          title: Items
          type: array
        pagination:
          $ref: '#/components/schemas/PaginationResponseV1'
          description: Pagination metadata for the page.
      required:
        - items
        - pagination
      title: ModelAPIsResponseV1
      type: object
    ModelAPIV1:
      description: >-
        A Model API catalog row, optionally enriched with workspace-specific
        state.
      properties:
        name:
          description: >-
            Identifier of the Model API. Stable, URL-safe slug used as the
            public identifier.
          examples:
            - llama-3-3-70b-instruct
          title: Name
          type: string
        display_name:
          description: Human-readable name of the Model API.
          examples:
            - Llama 3.3 70B Instruct
          title: Display Name
          type: string
        description:
          description: Description of the Model API.
          title: Description
          type: string
        model_family:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Family the underlying model belongs to.
          examples:
            - META
            - DEEPSEEK
            - QWEN
          title: Model Family
        release_date:
          description: Date the Model API was made available.
          format: date
          title: Release Date
          type: string
        invoke_url:
          description: >-
            Base URL for invoking the Model API. OpenAI-shaped routes (e.g.
            /v1/chat/completions) live underneath this host.
          examples:
            - https://inference.baseten.co
          title: Invoke Url
          type: string
        context_length:
          description: The model's context window length, in tokens.
          examples:
            - 8192
          title: Context Length
          type: integer
        cost_per_million_input_tokens:
          anyOf:
            - type: number
            - pattern: ^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$
              type: string
          description: Cost per million input tokens, in dollars.
          examples:
            - '0.13'
          title: Cost Per Million Input Tokens
        cost_per_million_output_tokens:
          anyOf:
            - type: number
            - pattern: ^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$
              type: string
          description: Cost per million output tokens, in dollars.
          examples:
            - '0.50'
          title: Cost Per Million Output Tokens
        rate_limits:
          description: >-
            Rate limits in effect for the workspace. Workspace-specific
            overrides are returned when the workspace has added this Model API
            and configured them; otherwise the catalog default rate limits are
            returned.
          items:
            $ref: '#/components/schemas/RateLimitV1'
          title: Rate Limits
          type: array
        org_details:
          anyOf:
            - $ref: '#/components/schemas/ModelAPIOrgDetailsV1'
            - type: 'null'
          default: null
          description: >-
            Workspace-specific state. Null when the workspace has not added this
            Model API.
      required:
        - name
        - display_name
        - description
        - release_date
        - invoke_url
        - context_length
        - cost_per_million_input_tokens
        - cost_per_million_output_tokens
        - rate_limits
      title: ModelAPIV1
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
    RateLimitV1:
      properties:
        type:
          $ref: '#/components/schemas/LimitTypeV1'
          description: The type of the rate limit
          examples:
            - TOKEN
            - REQUEST
        unit:
          $ref: '#/components/schemas/RateLimitUnitV1'
          description: The unit of the rate limit
          examples:
            - SECOND
            - MINUTE
        threshold:
          description: The threshold for the rate limit
          examples:
            - 1000
            - 50000
          minimum: 0
          title: Threshold
          type: integer
      required:
        - type
        - unit
        - threshold
      title: RateLimitV1
      type: object
    ModelAPIOrgDetailsV1:
      description: Workspace-specific state for a Model API.
      properties:
        added_at:
          description: When the workspace first added this Model API.
          format: date-time
          title: Added At
          type: string
        last_used_at:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          default: null
          description: >-
            When the workspace last invoked this Model API. Null if the
            workspace has never invoked it.
          title: Last Used At
      required:
        - added_at
      title: ModelAPIOrgDetailsV1
      type: object
    LimitTypeV1:
      enum:
        - REQUEST
        - TOKEN
      title: LimitTypeV1
      type: string
    RateLimitUnitV1:
      enum:
        - SECOND
        - MINUTE
      title: RateLimitUnitV1
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
