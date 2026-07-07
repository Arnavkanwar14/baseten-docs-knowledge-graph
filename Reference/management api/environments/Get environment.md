---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/environments/get-an-environments-details
---

> Gets an environment's details and returns the environment.

## OpenAPI

````yaml get /v1/models/{model_id}/environments/{env_name}
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
  /v1/models/{model_id}/environments/{env_name}:
    parameters:
      - $ref: '#/components/parameters/model_id'
      - $ref: '#/components/parameters/env_name'
    get:
      summary: Get an environment's details
      description: Gets an environment's details and returns the environment.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EnvironmentV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request GET \

            --url
            https://api.baseten.co/v1/models/{model_id}/environments/{env_name}
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/models/{model_id}/environments/{env_name}"

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
    EnvironmentV1:
      description: Environment for oracles.
      properties:
        name:
          description: Name of the environment
          title: Name
          type: string
        created_at:
          description: Time the environment was created in ISO 8601 format
          format: date-time
          title: Created At
          type: string
        model_id:
          description: Unique identifier of the model
          title: Model Id
          type: string
        current_deployment:
          anyOf:
            - $ref: '#/components/schemas/DeploymentV1'
            - type: 'null'
          description: Current deployment of the environment
        candidate_deployment:
          anyOf:
            - $ref: '#/components/schemas/DeploymentV1'
            - type: 'null'
          default: null
          description: >-
            Candidate deployment being promoted to the environment, if a
            promotion is in progress
        in_progress_promotion:
          anyOf:
            - $ref: '#/components/schemas/InProgressPromotionV1'
            - type: 'null'
          default: null
          description: Details of the in-progress promotion, if any
        autoscaling_settings:
          $ref: '#/components/schemas/AutoscalingSettingsV1'
          description: Autoscaling settings for the environment
        promotion_settings:
          $ref: '#/components/schemas/PromotionSettingsV1'
          description: Promotion settings for the environment
        instance_type:
          $ref: '#/components/schemas/InstanceTypeV1'
          description: Instance type for the environment
      required:
        - name
        - created_at
        - model_id
        - current_deployment
        - autoscaling_settings
        - promotion_settings
        - instance_type
      title: EnvironmentV1
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
    InProgressPromotionV1:
      description: Details of an in-progress promotion.
      properties:
        status:
          $ref: '#/components/schemas/InProgressPromotionStatusV1'
          description: Status of the promotion
        percent_traffic_to_new_version:
          description: Percentage of traffic routed to the candidate deployment
          title: Percent Traffic To New Version
          type: integer
        error_message:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Error message if promotion failed
          title: Error Message
        rolling_deploy:
          anyOf:
            - type: boolean
            - type: 'null'
          default: null
          description: Whether this is a rolling deploy
          title: Rolling Deploy
      required:
        - status
        - percent_traffic_to_new_version
      title: InProgressPromotionV1
      type: object
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
    PromotionSettingsV1:
      description: Promotion settings for promoting chains and oracles
      properties:
        redeploy_on_promotion:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          description: >-
            Whether to deploy on all promotions. Enabling this flag allows model
            code to safely handle environment-specific logic. When a deployment
            is promoted, a new deployment will be created with a copy of the
            image.
          examples:
            - true
          title: Redeploy On Promotion
        rolling_deploy:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          description: Whether the environment should rely on rolling deploy orchestration.
          examples:
            - true
          title: Rolling Deploy
        promotion_cleanup_strategy:
          anyOf:
            - $ref: '#/components/schemas/PromotionCleanupStrategyV1'
            - type: 'null'
          default: SCALE_TO_ZERO
          description: The cleanup strategy to use after a promotion completes.
          examples:
            - SCALE_TO_ZERO
        rolling_deploy_config:
          anyOf:
            - $ref: '#/components/schemas/RollingDeployConfigV1'
            - type: 'null'
          default: null
          description: Rolling deploy configuration for promotions
        ramp_up_while_promoting:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          description: Whether to ramp up traffic while promoting
          examples:
            - true
          title: Ramp Up While Promoting
        ramp_up_duration_seconds:
          anyOf:
            - type: integer
            - type: 'null'
          default: 600
          description: Duration of the ramp up in seconds
          examples:
            - 600
          title: Ramp Up Duration Seconds
      title: PromotionSettingsV1
      type: object
    InstanceTypeV1:
      description: An instance type.
      properties:
        id:
          description: Identifier string for the instance type
          title: Id
          type: string
        name:
          description: Display name of the instance type
          title: Name
          type: string
        memory_limit_mib:
          description: Memory limit of the instance type in Mebibytes
          title: Memory Limit Mib
          type: integer
        millicpu_limit:
          description: CPU limit of the instance type in millicpu
          title: Millicpu Limit
          type: integer
        gpu_count:
          description: Number of GPUs on the instance type
          title: Gpu Count
          type: integer
        gpu_type:
          anyOf:
            - type: string
            - type: 'null'
          description: Type of GPU on the instance type
          title: Gpu Type
        gpu_memory_limit_mib:
          anyOf:
            - type: integer
            - type: 'null'
          description: Memory limit of the GPU on the instance type in Mebibytes
          title: Gpu Memory Limit Mib
      required:
        - id
        - name
        - memory_limit_mib
        - millicpu_limit
        - gpu_count
        - gpu_type
        - gpu_memory_limit_mib
      title: InstanceTypeV1
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
    InProgressPromotionStatusV1:
      enum:
        - RELEASING
        - RAMPING_UP
        - RAMPING_DOWN
        - PAUSED
        - SUCCEEDED
        - FAILED
        - CANCELED
      title: InProgressPromotionStatusV1
      type: string
    PromotionCleanupStrategyV1:
      description: The promotion cleanup strategy.
      enum:
        - KEEP
        - SCALE_TO_ZERO
        - DEACTIVATE
      title: PromotionCleanupStrategyV1
      type: string
    RollingDeployConfigV1:
      description: Rolling deploy config for promoting chains and oracles
      properties:
        rolling_deploy_strategy:
          $ref: '#/components/schemas/RollingDeployStrategyV1'
          default: REPLICA
          description: The rolling deploy strategy to use for promotions.
          examples:
            - REPLICA
        max_surge_percent:
          default: 10
          description: The maximum surge percentage for rolling deploys.
          examples:
            - 10
          title: Max Surge Percent
          type: integer
        max_unavailable_percent:
          default: 0
          description: The maximum unavailable percentage for rolling deploys.
          examples:
            - 10
          title: Max Unavailable Percent
          type: integer
        stabilization_time_seconds:
          default: 0
          description: The stabilization time in seconds for rolling deploys.
          examples:
            - 300
          title: Stabilization Time Seconds
          type: integer
        replica_overhead_percent:
          default: 0
          description: The replica overhead percentage for rolling deploys.
          examples:
            - 0
          title: Replica Overhead Percent
          type: integer
      title: RollingDeployConfigV1
      type: object
    RollingDeployStrategyV1:
      description: The rolling deploy strategy.
      enum:
        - REPLICA
      title: RollingDeployStrategyV1
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
