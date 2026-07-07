---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/deployments/promote/promotes-a-chain-deployment-to-an-environment
---

> Promotes an existing chain deployment to an environment and returns the promoted chain deployment.

## OpenAPI

````yaml post /v1/chains/{chain_id}/environments/{env_name}/promote
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
  /v1/chains/{chain_id}/environments/{env_name}/promote:
    parameters:
      - $ref: '#/components/parameters/chain_id'
      - $ref: '#/components/parameters/env_name'
    post:
      summary: Promotes a chain deployment to an environment
      description: >-
        Promotes an existing chain deployment to an environment and returns the
        promoted chain deployment.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PromoteToChainEnvironmentRequestV1'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChainDeploymentV1'
      x-codeSamples:
        - lang: bash
          source: >-
            curl --request POST \

            --url
            https://api.baseten.co/v1/chains/{chain_id}/environments/{env_name}/promote
            \

            --header "Authorization: Bearer $BASETEN_API_KEY" \

            --data '{
              "scale_down_previous_deployment": true,
              "deployment_id": null
            }'
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/chains/{chain_id}/environments/{env_name}/promote"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "POST",
                url,
                headers=headers,
                json={'scale_down_previous_deployment': True, 'deployment_id': None}
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
    PromoteToChainEnvironmentRequestV1:
      description: A request to promote a deployment to a environment.
      properties:
        scale_down_previous_deployment:
          default: true
          description: Whether to scale down the previous deployment after promoting
          examples:
            - true
          title: Scale Down Previous Deployment
          type: boolean
        deployment_id:
          description: The id of the chain deployment to promote
          title: Deployment Id
          type: string
      required:
        - deployment_id
      title: PromoteToChainEnvironmentRequestV1
      type: object
    ChainDeploymentV1:
      description: A deployment of a chain.
      properties:
        id:
          description: Unique identifier of the chain deployment
          title: Id
          type: string
        created_at:
          description: Time the chain deployment was created in ISO 8601 format
          format: date-time
          title: Created At
          type: string
        chain_id:
          description: Unique identifier of the chain
          title: Chain Id
          type: string
        environment:
          anyOf:
            - type: string
            - type: 'null'
          description: Environment the chain deployment is deployed in
          title: Environment
        chainlets:
          description: Chainlets in the chain deployment
          items:
            $ref: '#/components/schemas/ChainletV1'
          title: Chainlets
          type: array
        status:
          $ref: '#/components/schemas/DeploymentStatusV1'
          description: Status of the chain deployment
      required:
        - id
        - created_at
        - chain_id
        - environment
        - chainlets
        - status
      title: ChainDeploymentV1
      type: object
    ChainletV1:
      description: A chainlet in a chain deployment.
      properties:
        id:
          description: Unique identifier of the chainlet
          title: Id
          type: string
        name:
          description: Name of the chainlet
          title: Name
          type: string
        autoscaling_settings:
          anyOf:
            - $ref: '#/components/schemas/AutoscalingSettingsV1'
            - type: 'null'
          description: >-
            Autoscaling settings for the chainlet. If null, it has not finished
            deploying
        instance_type_name:
          description: Name of the instance type the chainlet is deployed on
          title: Instance Type Name
          type: string
        active_replica_count:
          description: Number of active replicas
          title: Active Replica Count
          type: integer
        status:
          $ref: '#/components/schemas/DeploymentStatusV1'
          description: Status of the chainlet
      required:
        - id
        - name
        - autoscaling_settings
        - instance_type_name
        - active_replica_count
        - status
      title: ChainletV1
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
