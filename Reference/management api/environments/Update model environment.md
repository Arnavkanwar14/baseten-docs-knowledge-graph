---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/environments/update-an-environments-settings
---

> Asynchronously updates an environment's settings. Poll the GET endpoint for the applied state.

## OpenAPI

````yaml patch /v1/models/{model_id}/environments/{env_name}
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
    patch:
      summary: Update an environment's settings
      description: >-
        Asynchronously updates an environment's settings. Poll the GET endpoint
        for the applied state.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateEnvironmentRequestV1'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdateAutoscalingSettingsResponseV1'
      x-codeSamples:
        - lang: bash
          source: >-
            curl --request PATCH \

            --url
            https://api.baseten.co/v1/models/{model_id}/environments/{env_name}
            \

            --header "Authorization: Bearer $BASETEN_API_KEY" \

            --data '{
              "autoscaling_settings": {
                "autoscaling_window": 800,
                "concurrency_target": 3,
                "max_replica": 2,
                "max_scale_down_rate": null,
                "min_replica": 1,
                "scale_down_delay": 60,
                "target_in_flight_tokens": null,
                "target_utilization_percentage": null
              },
              "promotion_settings": {
                "promotion_cleanup_strategy": null,
                "ramp_up_duration_seconds": 600,
                "ramp_up_while_promoting": true,
                "redeploy_on_promotion": true,
                "rolling_deploy": null,
                "rolling_deploy_config": null
              }
            }'
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/models/{model_id}/environments/{env_name}"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "PATCH",
                url,
                headers=headers,
                json={'autoscaling_settings': {'autoscaling_window': 800, 'concurrency_target': 3, 'max_replica': 2, 'max_scale_down_rate': None, 'min_replica': 1, 'scale_down_delay': 60, 'target_in_flight_tokens': None, 'target_utilization_percentage': None}, 'promotion_settings': {'promotion_cleanup_strategy': None, 'ramp_up_duration_seconds': 600, 'ramp_up_while_promoting': True, 'redeploy_on_promotion': True, 'rolling_deploy': None, 'rolling_deploy_config': None}}
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
    UpdateEnvironmentRequestV1:
      additionalProperties: false
      description: A request to update an environment.
      properties:
        autoscaling_settings:
          anyOf:
            - $ref: '#/components/schemas/UpdateAutoscalingSettingsV1'
            - type: 'null'
          default: null
          description: Autoscaling settings for the environment
          examples:
            - autoscaling_window: 800
              concurrency_target: 3
              max_replica: 2
              max_scale_down_rate: null
              min_replica: 1
              scale_down_delay: 60
              target_in_flight_tokens: null
              target_utilization_percentage: null
        promotion_settings:
          anyOf:
            - $ref: '#/components/schemas/UpdatePromotionSettingsV1'
            - type: 'null'
          default: null
          description: Promotion settings for the environment
          examples:
            - promotion_cleanup_strategy: null
              ramp_up_duration_seconds: 600
              ramp_up_while_promoting: true
              redeploy_on_promotion: true
              rolling_deploy: null
              rolling_deploy_config: null
      title: UpdateEnvironmentRequestV1
      type: object
    UpdateAutoscalingSettingsResponseV1:
      description: The response to a request to update autoscaling settings.
      properties:
        status:
          $ref: '#/components/schemas/UpdateAutoscalingSettingsStatusV1'
          description: Status of the request to update autoscaling settings
        message:
          description: >-
            A message describing the status of the request to update autoscaling
            settings
          title: Message
          type: string
      required:
        - status
        - message
      title: UpdateAutoscalingSettingsResponseV1
      type: object
    UpdateAutoscalingSettingsV1:
      additionalProperties: false
      description: >-
        A request to update autoscaling settings for a deployment. All fields
        are optional, and we only update ones passed in.
      properties:
        min_replica:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Minimum number of replicas
          examples:
            - 0
          title: Min Replica
        max_replica:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Maximum number of replicas
          examples:
            - 7
          title: Max Replica
        autoscaling_window:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Timeframe of traffic considered for autoscaling decisions
          examples:
            - 600
          title: Autoscaling Window
        scale_down_delay:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Waiting period before scaling down any active replica
          examples:
            - 120
          title: Scale Down Delay
        concurrency_target:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Number of requests per replica before scaling up
          examples:
            - 2
          title: Concurrency Target
        target_utilization_percentage:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Target utilization percentage for scaling up/down.
          examples:
            - 70
          title: Target Utilization Percentage
        target_in_flight_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: >-
            Target number of in-flight tokens for autoscaling decisions. Early
            access only.
          examples:
            - 40000
          title: Target In Flight Tokens
        max_scale_down_rate:
          anyOf:
            - maximum: 50
              minimum: 1
              type: integer
            - type: 'null'
          default: null
          description: >-
            Maximum percentage of replicas that can be removed per autoscaling
            window (1–50). E.g. 20 means at most 20% of replicas are removed per
            window.
          examples:
            - 20
          title: Max Scale Down Rate
      title: UpdateAutoscalingSettingsV1
      type: object
    UpdatePromotionSettingsV1:
      description: Promotion settings for model promotion
      properties:
        redeploy_on_promotion:
          anyOf:
            - type: boolean
            - type: 'null'
          default: null
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
          default: null
          description: Whether the environment should rely on rolling deploy orchestration.
          examples:
            - true
          title: Rolling Deploy
        promotion_cleanup_strategy:
          anyOf:
            - $ref: '#/components/schemas/PromotionCleanupStrategyV1'
            - type: 'null'
          default: null
          description: The cleanup strategy to use after a promotion completes.
          examples:
            - SCALE_TO_ZERO
        rolling_deploy_config:
          anyOf:
            - $ref: '#/components/schemas/UpdateRollingDeployConfigV1'
            - type: 'null'
          default: null
          description: Rolling deploy configuration for promotions
        ramp_up_while_promoting:
          anyOf:
            - type: boolean
            - type: 'null'
          default: null
          description: Whether to ramp up traffic while promoting
          examples:
            - true
          title: Ramp Up While Promoting
        ramp_up_duration_seconds:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Duration of the ramp up in seconds
          examples:
            - 600
          title: Ramp Up Duration Seconds
      title: UpdatePromotionSettingsV1
      type: object
    UpdateAutoscalingSettingsStatusV1:
      description: The status of a request to update autoscaling settings.
      enum:
        - ACCEPTED
        - QUEUED
        - UNCHANGED
      title: UpdateAutoscalingSettingsStatusV1
      type: string
    PromotionCleanupStrategyV1:
      description: The promotion cleanup strategy.
      enum:
        - KEEP
        - SCALE_TO_ZERO
        - DEACTIVATE
      title: PromotionCleanupStrategyV1
      type: string
    UpdateRollingDeployConfigV1:
      description: Rolling deploy config for promoting chains and oracles
      properties:
        rolling_deploy_strategy:
          anyOf:
            - $ref: '#/components/schemas/RollingDeployStrategyV1'
            - type: 'null'
          default: null
          description: The rolling deploy strategy to use for promotions.
          examples:
            - REPLICA
        max_surge_percent:
          anyOf:
            - type: integer
            - type: 'null'
          default: 10
          description: The maximum surge percentage for rolling deploys.
          examples:
            - 10
          title: Max Surge Percent
        max_unavailable_percent:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: The maximum unavailable percentage for rolling deploys.
          examples:
            - 10
          title: Max Unavailable Percent
        stabilization_time_seconds:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: The stabilization time in seconds for rolling deploys.
          examples:
            - 300
          title: Stabilization Time Seconds
        replica_overhead_percent:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: The replica overhead percentage for rolling deploys.
          examples:
            - 0
          title: Replica Overhead Percent
      title: UpdateRollingDeployConfigV1
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
