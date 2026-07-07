---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/environments/get-environment-logs
---

> Gets logs across all deployments that were active on the environment in the given time range, which defaults to the last 30 minutes. Pass `start_epoch_millis` to widen the window back to an earlier deployment's build/deploy time.

## OpenAPI

````yaml get /v1/models/{model_id}/environments/{env_name}/logs
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
  /v1/models/{model_id}/environments/{env_name}/logs:
    parameters:
      - $ref: '#/components/parameters/model_id'
      - $ref: '#/components/parameters/env_name'
    get:
      summary: Gets the logs for a model environment.
      description: >-
        Gets logs across all deployments that were active on the environment in
        the given time range, which defaults to the last 30 minutes. Pass
        `start_epoch_millis` to widen the window back to an earlier deployment's
        build/deploy time.
      parameters:
        - name: start_epoch_millis
          in: query
          required: false
          description: >-
            Epoch milliseconds at which to start fetching logs. Defaults to 30
            minutes before the end. The window from start to end must not exceed
            7 days.
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            default: null
            title: Start Epoch Millis
        - name: end_epoch_millis
          in: query
          required: false
          description: >-
            Epoch milliseconds at which to stop fetching logs. Defaults to the
            current time.
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            default: null
            title: End Epoch Millis
        - name: direction
          in: query
          required: false
          description: Sort order for logs
          schema:
            anyOf:
              - $ref: '#/components/schemas/SortOrderV1'
              - type: 'null'
            default: null
        - name: limit
          in: query
          required: false
          description: Limit of logs to fetch in a single request
          schema:
            anyOf:
              - maximum: 1000
                minimum: 1
                type: integer
              - type: 'null'
            default: 500
            title: Limit
        - name: min_level
          in: query
          required: false
          description: >-
            Minimum log severity to include. Omit to return all log lines,
            including lines that have no level. Any explicit value returns lines
            at or above that severity and drops lines without a level.
          schema:
            anyOf:
              - $ref: '#/components/schemas/LogLevelV1'
              - type: 'null'
            default: null
        - name: replica
          in: query
          required: false
          description: Only return logs emitted by this replica (5-char short ID).
          schema:
            anyOf:
              - maxLength: 256
                type: string
              - type: 'null'
            default: null
            title: Replica
        - name: request_id
          in: query
          required: false
          description: Only return logs tagged with this inference request ID.
          schema:
            anyOf:
              - maxLength: 256
                type: string
              - type: 'null'
            default: null
            title: Request Id
        - name: component
          in: query
          required: false
          description: Only return logs from this component.
          schema:
            anyOf:
              - maxLength: 256
                type: string
              - type: 'null'
            default: null
            title: Component
        - name: search_pattern
          in: query
          required: false
          description: >-
            RE2 regular expression matched against the log message. Prefer
            `includes` and `excludes` for plain substring matches.
          schema:
            anyOf:
              - maxLength: 256
                type: string
              - type: 'null'
            default: null
            title: Search Pattern
        - name: includes
          in: query
          required: false
          description: Case-sensitive substrings that must all appear in the log message.
          schema:
            items:
              type: string
            maxItems: 8
            title: Includes
            type: array
        - name: excludes
          in: query
          required: false
          description: >-
            Case-sensitive substrings; lines containing any of these are
            dropped.
          schema:
            items:
              type: string
            maxItems: 8
            title: Excludes
            type: array
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetLogsResponseV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request GET \

            --url
            https://api.baseten.co/v1/models/{model_id}/environments/{env_name}/logs
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/models/{model_id}/environments/{env_name}/logs"

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
    model_id:
      schema:
        type: string
      name: model_id
      in: path
      required: true
    env_name:
      schema:
        type: string
      name: env_name
      in: path
      required: true
  schemas:
    SortOrderV1:
      enum:
        - asc
        - desc
      title: SortOrderV1
      type: string
    LogLevelV1:
      description: A log severity level.
      enum:
        - DEBUG
        - INFO
        - WARNING
        - ERROR
      title: LogLevelV1
      type: string
    GetLogsResponseV1:
      description: A response to querying logs.
      properties:
        logs:
          description: Logs for a specific entity.
          items:
            $ref: '#/components/schemas/LogV1'
          title: Logs
          type: array
      required:
        - logs
      title: GetLogsResponseV1
      type: object
    LogV1:
      properties:
        timestamp:
          description: Epoch nanosecond timestamp of the log message.
          title: Timestamp
          type: string
        message:
          description: The contents of the log message.
          title: Message
          type: string
        replica:
          anyOf:
            - type: string
            - type: 'null'
          description: The replica the log line was emitted from.
          title: Replica
        request_id:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: The request ID associated with an inference request.
          title: Request Id
        level:
          anyOf:
            - $ref: '#/components/schemas/LogLevelV1'
            - type: 'null'
          default: null
          description: Severity of the log line, if one was detected. null when unknown.
      required:
        - timestamp
        - message
        - replica
      title: LogV1
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
