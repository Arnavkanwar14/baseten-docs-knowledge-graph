---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/models/prepare-model-upload
---

## OpenAPI

````yaml post /v1/prepare_model_upload
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
  /v1/prepare_model_upload:
    post:
      summary: Validates a model push payload and issues upload credentials
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PrepareModelUploadRequestV1'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrepareModelUploadResponseV1'
      x-codeSamples:
        - lang: bash
          source: |-
            curl --request POST \
            --url https://api.baseten.co/v1/prepare_model_upload \
            --header "Authorization: Bearer $BASETEN_API_KEY" \
            --data '{
              "deployment": {
                "config": null,
                "raw_config": null,
                "user_env": null,
                "environment_name": null,
                "deploy_timeout_minutes": null,
                "deployment_name": null,
                "labels": null
              },
              "name": null,
              "team_id": null,
              "model_id": null
            }'
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/prepare_model_upload"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "POST",
                url,
                headers=headers,
                json={'deployment': {'config': None, 'raw_config': None, 'user_env': None, 'environment_name': None, 'deploy_timeout_minutes': None, 'deployment_name': None, 'labels': None}, 'name': None, 'team_id': None, 'model_id': None}
            )

            print(response.text)
components:
  schemas:
    PrepareModelUploadRequestV1:
      description: |-
        Body for `POST /v1/prepare_model_upload`.

        Validates the same payload the commit endpoint will validate, and on
        `dry_run=false` issues STS upload credentials. Exactly one of `name` or
        `model_id` is required: `name` validates the new-model path (`POST
        /v1/models`); `model_id` validates the add-deployment path (`POST
        /v1/models/{model_id}/deployments`).
      properties:
        deployment:
          $ref: '#/components/schemas/DeploymentArchivePayloadV1'
          description: Deployment-level payload, identical to the payload sent at commit.
        name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: >-
            Set to validate a new-model push. Exactly one of `name` or
            `model_id` is required.
          title: Name
        team_id:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: >-
            Team the new model will belong to. Only valid when `name` is set;
            defaults to the organization's default team when omitted. Must not
            be set when `model_id` is set (the existing model already has a
            team).
          title: Team Id
        model_id:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: >-
            Set to validate an add-deployment push to an existing model. Exactly
            one of `name` or `model_id` is required.
          title: Model Id
        dry_run:
          default: false
          description: >-
            If true, validate the payload only and do not issue upload
            credentials. The response sets `creds`, `s3_bucket`, and `s3_key` to
            `null`.
          title: Dry Run
          type: boolean
      required:
        - deployment
      title: PrepareModelUploadRequestV1
      type: object
    PrepareModelUploadResponseV1:
      description: >-
        Response from `POST /v1/prepare_model_upload`.

        On success with `dry_run=false`, returns STS upload credentials. On
        success

        with `dry_run=true`, `creds`, `s3_bucket`, and `s3_key` are `null` and
        only

        validation has run.
      properties:
        creds:
          anyOf:
            - $ref: '#/components/schemas/AWSCredentialsV1'
            - type: 'null'
          default: null
          description: STS credentials to upload the model archive.
        s3_bucket:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: S3 bucket the credentials are scoped to.
          title: S3 Bucket
        s3_key:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: >-
            S3 key the credentials are scoped to. Pass this to `POST /v1/models`
            (in the `model_archive` source) once the upload completes.
          title: S3 Key
        s3_region:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: AWS region the S3 bucket resides in.
          title: S3 Region
      title: PrepareModelUploadResponseV1
      type: object
    DeploymentArchivePayloadV1:
      description: >-
        Deployment-level fields for a model-archive push.

        Shared by every endpoint that creates a deployment from an uploaded
        archive:

        `POST /v1/prepare_model_upload`, the `model_archive` source on `POST

        /v1/models`, and `POST /v1/models/{model_id}/deployments`.
      properties:
        config:
          additionalProperties: true
          description: Parsed model config as a JSON object.
          title: Config
          type: object
        raw_config:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: >-
            Original config.yaml text, persisted as-is on the deployment.
            Best-effort: invalid raw configs are logged and dropped without
            failing the request.
          title: Raw Config
        user_env:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          default: null
          description: >-
            Client environment metadata (e.g. client version, Python version).
            Validated server-side.
          title: User Env
        environment_name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: >-
            Stable environment to push to (e.g. `production`). If unset, the
            deployment is created without environment selection. Caller must
            have push permission for the named environment.
          title: Environment Name
        preserve_env_instance_type:
          default: true
          description: >-
            Retain the target environment's current instance type rather than
            the one in `config`. Only meaningful when `environment_name` is set
            and that environment already exists.
          title: Preserve Env Instance Type
          type: boolean
        deploy_timeout_minutes:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: >-
            Deploy timeout in minutes; allowed range 10 to 1440. Server default
            applies if unset.
          title: Deploy Timeout Minutes
        deployment_name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Optional human-readable name for the deployment.
          title: Deployment Name
        labels:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          default: null
          description: User-provided key-value labels for the deployment.
          title: Labels
        is_development:
          default: false
          description: >-
            If true, push as a development deployment: the model's single
            mutable dev slot, created if absent and overwritten in place
            otherwise. The following fields must be left at their defaults:
            `environment_name`, `preserve_env_instance_type`, `deployment_name`.
          title: Is Development
          type: boolean
      required:
        - config
      title: DeploymentArchivePayloadV1
      type: object
    AWSCredentialsV1:
      description: AWS credentials
      properties:
        aws_access_key_id:
          description: The AWS access key ID
          title: Aws Access Key Id
          type: string
        aws_secret_access_key:
          description: The AWS secret access key
          title: Aws Secret Access Key
          type: string
        aws_session_token:
          description: The AWS session token
          title: Aws Session Token
          type: string
      required:
        - aws_access_key_id
        - aws_secret_access_key
        - aws_session_token
      title: AWSCredentialsV1
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
