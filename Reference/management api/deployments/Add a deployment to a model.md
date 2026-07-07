---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/deployments/adds-a-deployment-to-a-model
---

## OpenAPI

````yaml post /v1/models/{model_id}/deployments
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
  /v1/models/{model_id}/deployments:
    parameters:
      - $ref: '#/components/parameters/model_id'
    post:
      summary: Adds a new deployment to a model
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateModelDeploymentRequestV1'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreatedModelDeploymentV1'
      x-codeSamples:
        - lang: bash
          source: |-
            curl --request POST \
            --url https://api.baseten.co/v1/models/{model_id}/deployments \
            --header "Authorization: Bearer $BASETEN_API_KEY" \
            --data '{
              "source": null
            }'
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/models/{model_id}/deployments"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "POST",
                url,
                headers=headers,
                json={'source': None}
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
  schemas:
    CreateModelDeploymentRequestV1:
      description: |-
        Body for adding a deployment to an existing model via
        `POST /v1/models/{model_id}/deployments`.
      properties:
        source:
          description: Where the new deployment is created from.
          discriminator:
            mapping:
              model_archive:
                $ref: '#/components/schemas/DeploymentArchiveSourceV1'
            propertyName: kind
          oneOf:
            - $ref: '#/components/schemas/DeploymentArchiveSourceV1'
          title: Source
      required:
        - source
      title: CreateModelDeploymentRequestV1
      type: object
    CreatedModelDeploymentV1:
      description: A newly created deployment and its model.
      properties:
        model:
          $ref: '#/components/schemas/ModelV1'
          description: >-
            The model the deployment belongs to. May have been created by this
            call.
        deployment:
          $ref: '#/components/schemas/DeploymentV1'
          description: The newly created deployment.
      required:
        - model
        - deployment
      title: CreatedModelDeploymentV1
      type: object
    DeploymentArchiveSourceV1:
      description: |-
        Add a deployment from an archive previously uploaded via the credentials
        issued by `POST /v1/prepare_model_upload`.
      properties:
        kind:
          const: model_archive
          default: model_archive
          title: Kind
          type: string
        deployment:
          $ref: '#/components/schemas/DeploymentArchivePayloadV1'
          description: Deployment-level configuration.
        s3_key:
          description: >-
            S3 key of the uploaded archive, from the credentials returned by
            `POST /v1/prepare_model_upload`.
          title: S3 Key
          type: string
      required:
        - deployment
        - s3_key
      title: DeploymentArchiveSourceV1
      type: object
    ModelV1:
      description: A model.
      properties:
        id:
          description: Unique identifier of the model
          title: Id
          type: string
        created_at:
          description: Time the model was created in ISO 8601 format
          format: date-time
          title: Created At
          type: string
        name:
          description: Name of the model
          title: Name
          type: string
        deployments_count:
          description: Number of deployments of the model
          title: Deployments Count
          type: integer
        production_deployment_id:
          anyOf:
            - type: string
            - type: 'null'
          description: Unique identifier of the production deployment of the model
          title: Production Deployment Id
        development_deployment_id:
          anyOf:
            - type: string
            - type: 'null'
          description: Unique identifier of the development deployment of the model
          title: Development Deployment Id
        instance_type_name:
          description: Name of the instance type for the production deployment of the model
          title: Instance Type Name
          type: string
        team_name:
          description: Name of the team associated with the model.
          title: Team Name
          type: string
      required:
        - id
        - created_at
        - name
        - deployments_count
        - production_deployment_id
        - development_deployment_id
        - instance_type_name
        - team_name
      title: ModelV1
      type: object
    DeploymentV1:
      description: A deployment of a model.
      properties:
        id:
          description: Unique identifier of the deployment
          title: Id
          type: string
        created_at:
          description: Time the deployment was created in ISO 8601 format
          format: date-time
          title: Created At
          type: string
        name:
          description: Name of the deployment
          title: Name
          type: string
        model_id:
          description: Unique identifier of the model
          title: Model Id
          type: string
        is_production:
          description: Whether the deployment is the production deployment of the model
          title: Is Production
          type: boolean
        is_development:
          description: Whether the deployment is the development deployment of the model
          title: Is Development
          type: boolean
        status:
          $ref: '#/components/schemas/DeploymentStatusV1'
          description: Status of the deployment
        active_replica_count:
          description: Number of active replicas
          title: Active Replica Count
          type: integer
        autoscaling_settings:
          anyOf:
            - $ref: '#/components/schemas/AutoscalingSettingsV1'
            - type: 'null'
          description: >-
            Autoscaling settings for the deployment. If null, the model has not
            finished deploying
        instance_type_name:
          anyOf:
            - type: string
            - type: 'null'
          description: Name of the instance type the model deployment is running on
          title: Instance Type Name
        environment:
          anyOf:
            - type: string
            - type: 'null'
          description: The environment associated with the deployment
          title: Environment
        labels:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          default: null
          description: User-provided key-value labels for the deployment
          title: Labels
      required:
        - id
        - created_at
        - name
        - model_id
        - is_production
        - is_development
        - status
        - active_replica_count
        - autoscaling_settings
        - instance_type_name
        - environment
      title: DeploymentV1
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
    DeploymentStatusV1:
      description: The status of a deployment.
      enum:
        - BUILDING
        - DEPLOYING
        - DEPLOY_FAILED
        - LOADING_MODEL
        - ACTIVE
        - UNHEALTHY
        - BUILD_FAILED
        - BUILD_STOPPED
        - DEACTIVATING
        - INACTIVE
        - FAILED
        - UPDATING
        - SCALED_TO_ZERO
        - WAKING_UP
      title: DeploymentStatusV1
      type: string
    AutoscalingSettingsV1:
      description: Autoscaling settings for a deployment.
      properties:
        min_replica:
          description: Minimum number of replicas
          title: Min Replica
          type: integer
        max_replica:
          description: Maximum number of replicas
          title: Max Replica
          type: integer
        autoscaling_window:
          anyOf:
            - type: integer
            - type: 'null'
          description: Timeframe of traffic considered for autoscaling decisions
          title: Autoscaling Window
        scale_down_delay:
          anyOf:
            - type: integer
            - type: 'null'
          description: Waiting period before scaling down any active replica
          title: Scale Down Delay
        concurrency_target:
          description: Number of requests per replica before scaling up
          title: Concurrency Target
          type: integer
        target_utilization_percentage:
          anyOf:
            - type: integer
            - type: 'null'
          description: Target utilization percentage for scaling up/down.
          title: Target Utilization Percentage
        target_in_flight_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: >-
            Target number of in-flight tokens for autoscaling decisions. Early
            access only.
          title: Target In Flight Tokens
        max_scale_down_rate:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: >-
            Maximum percentage of replicas that can be removed per autoscaling
            window (1–50). E.g. 20 means at most 20% of replicas are removed per
            window.
          title: Max Scale Down Rate
      required:
        - min_replica
        - max_replica
        - autoscaling_window
        - scale_down_delay
        - concurrency_target
        - target_utilization_percentage
      title: AutoscalingSettingsV1
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
