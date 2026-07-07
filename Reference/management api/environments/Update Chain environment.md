---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/environments/update-a-chain-environments-settings
---

> Update a chain environment's settings and returns the chain environment.

## OpenAPI

````yaml patch /v1/chains/{chain_id}/environments/{env_name}
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
  /v1/chains/{chain_id}/environments/{env_name}:
    parameters:
      - $ref: '#/components/parameters/chain_id'
      - $ref: '#/components/parameters/env_name'
    patch:
      summary: Update a chain environment's settings
      description: Update a chain environment's settings and returns the chain environment.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateChainEnvironmentRequestV1'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdateChainEnvironmentResponseV1'
      x-codeSamples:
        - lang: bash
          source: >-
            curl --request PATCH \

            --url
            https://api.baseten.co/v1/chains/{chain_id}/environments/{env_name}
            \

            --header "Authorization: Bearer $BASETEN_API_KEY" \

            --data '{
              "promotion_settings": {
                "promotion_cleanup_strategy": null,
                "ramp_up_duration_seconds": 600,
                "ramp_up_while_promoting": true,
                "redeploy_on_promotion": null,
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
            "https://api.baseten.co/v1/chains/{chain_id}/environments/{env_name}"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "PATCH",
                url,
                headers=headers,
                json={'promotion_settings': {'promotion_cleanup_strategy': None, 'ramp_up_duration_seconds': 600, 'ramp_up_while_promoting': True, 'redeploy_on_promotion': None, 'rolling_deploy': None, 'rolling_deploy_config': None}}
            )

            print(response.text)
components:
  parameters:
    chain_id:
      schema:
        type: string
      name: chain_id
      in: path
      required: true
    env_name:
      schema:
        type: string
      name: env_name
      in: path
      required: true
  schemas:
    UpdateChainEnvironmentRequestV1:
      description: A request to update a chain environment.
      properties:
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
              redeploy_on_promotion: null
              rolling_deploy: null
              rolling_deploy_config: null
      title: UpdateChainEnvironmentRequestV1
      type: object
    UpdateChainEnvironmentResponseV1:
      description: A response to update a chain environment.
      properties:
        ok:
          description: Whether the update was successful
          title: Ok
          type: boolean
      required:
        - ok
      title: UpdateChainEnvironmentResponseV1
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
