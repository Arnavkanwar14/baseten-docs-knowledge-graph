---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/deployments/retry/retries-a-deployment
---

> Retries a failed deployment and returns the retry status and updated deployment.

## OpenAPI

````yaml post /v1/models/{model_id}/deployments/{deployment_id}/retry
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
  /v1/models/{model_id}/deployments/{deployment_id}/retry:
    parameters:
      - $ref: '#/components/parameters/model_id'
      - $ref: '#/components/parameters/deployment_id'
    post:
      summary: Retries a failed deployment
      description: >-
        Retries a failed deployment and returns the retry status and updated
        deployment.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RetryDeploymentResponseV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request POST \

            --url
            https://api.baseten.co/v1/models/{model_id}/deployments/{deployment_id}/retry
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/models/{model_id}/deployments/{deployment_id}/retry"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "POST",
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
    deployment_id:
      schema:
        type: string
      name: deployment_id
      in: path
      required: true
  schemas:
    RetryDeploymentResponseV1:
      description: The response to a request to retry a deployment.
      properties:
        retried:
          description: Whether the retry was successfully initiated
          title: Retried
          type: boolean
        reason:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: >-
            Explanation of the result. Provided when retried is false to explain
            why retry was not possible.
          title: Reason
        deployment:
          $ref: '#/components/schemas/DeploymentV1'
          description: The deployment that was retried
      required:
        - retried
        - deployment
      title: RetryDeploymentResponseV1
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
