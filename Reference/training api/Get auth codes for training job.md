---
tags: [baseten, reference, training-api]
source: https://docs.baseten.co/reference/training-api/get-auth-codes-for-training-job
---

> Get authentication codes for all nodes of a training job's interactive sessions.

## OpenAPI

````yaml get /v1/training_projects/{training_project_id}/jobs/{training_job_id}/auth_codes
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
  /v1/training_projects/{training_project_id}/jobs/{training_job_id}/auth_codes:
    parameters:
      - $ref: '#/components/parameters/training_project_id'
      - $ref: '#/components/parameters/training_job_id'
    get:
      summary: Get auth codes for a training job.
      description: >-
        Get authentication codes for all nodes of a training job's interactive
        sessions.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetAuthCodesResponseV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request GET \

            --url
            https://api.baseten.co/v1/training_projects/{training_project_id}/jobs/{training_job_id}/auth_codes
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/training_projects/{training_project_id}/jobs/{training_job_id}/auth_codes"

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
    training_project_id:
      schema:
        type: string
      name: training_project_id
      in: path
      required: true
    training_job_id:
      schema:
        type: string
      name: training_job_id
      in: path
      required: true
  schemas:
    GetAuthCodesResponseV1:
      description: >-
        Response containing auth codes for all nodes of a training job's
        interactive sessions.
      properties:
        auth_codes:
          description: >-
            List of auth codes for each node that has an active interactive
            session.
          items:
            $ref: '#/components/schemas/AuthCodeV1'
          title: Auth Codes
          type: array
      required:
        - auth_codes
      title: GetAuthCodesResponseV1
      type: object
    AuthCodeV1:
      description: Authentication code for a training job interactive session node.
      properties:
        session_id:
          description: Unique identifier of the interactive session.
          title: Session Id
          type: string
        replica_id:
          description: >-
            Replica identifier in gXXrY format (e.g., 'g00r0' for group 0,
            replica 0).
          title: Replica Id
          type: string
        auth_code:
          description: The device authentication code (e.g., '4F64-C0D9').
          title: Auth Code
          type: string
        auth_url:
          description: >-
            URL where the user should enter the auth code (e.g.,
            'https://github.com/login/device').
          title: Auth Url
          type: string
        generated_at:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          default: null
          description: When the auth code was generated, in ISO 8601 format.
          title: Generated At
        tunnel_name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: The name of the tunnel node.
          title: Tunnel Name
        expires_at:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          default: null
          description: When the session expires, in ISO 8601 format.
          title: Expires At
        working_directory:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: The working directory of the session.
          title: Working Directory
      required:
        - session_id
        - replica_id
        - auth_code
        - auth_url
      title: AuthCodeV1
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
Part of [[Training Api (Reference)]]
