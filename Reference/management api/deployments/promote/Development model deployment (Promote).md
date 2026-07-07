---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/deployments/promote/promotes-a-development-deployment-to-production
---

> Creates a new production deployment from the development deployment, the currently building deployment is returned.

## OpenAPI

````yaml post /v1/models/{model_id}/deployments/development/promote
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
  /v1/models/{model_id}/deployments/development/promote:
    parameters:
      - $ref: '#/components/parameters/model_id'
    post:
      summary: Promotes a development deployment to production
      description: >-
        Creates a new production deployment from the development deployment, the
        currently building deployment is returned.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PromoteRequestV1'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeploymentV1'
      x-codeSamples:
        - lang: bash
          source: >-
            curl --request POST \

            --url
            https://api.baseten.co/v1/models/{model_id}/deployments/development/promote
            \

            --header "Authorization: Bearer $BASETEN_API_KEY" \

            --data '{
              "scale_down_previous_production": true,
              "preserve_env_instance_type": true
            }'
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/models/{model_id}/deployments/development/promote"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "POST",
                url,
                headers=headers,
                json={'scale_down_previous_production': True, 'preserve_env_instance_type': True}
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
    PromoteRequestV1:
      description: A request to promote a deployment to production.
      properties:
        scale_down_previous_production:
          default: true
          description: >-
            Whether to scale down the previous production deployment after
            promoting
          examples:
            - true
          title: Scale Down Previous Production
          type: boolean
        preserve_env_instance_type:
          default: true
          description: >-
            Whether to use the promoting deployment's instance type or preserve
            target environment's instance type
          examples:
            - true
          title: Preserve Env Instance Type
          type: boolean
      title: PromoteRequestV1
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
