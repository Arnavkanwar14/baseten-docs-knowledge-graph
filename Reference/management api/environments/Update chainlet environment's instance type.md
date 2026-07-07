---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/environments/update-a-chainlet-environments-instance-type-settings
---

> Updates a chainlet environment's instance type settings. The chainlet environment setting must exist. When updated, a new chain deployment is created and deployed. It is promoted to the chain environment according to promotion settings on the environment.

## OpenAPI

````yaml post /v1/chains/{chain_id}/environments/{env_name}/chainlet_settings/instance_types/update
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
  /v1/chains/{chain_id}/environments/{env_name}/chainlet_settings/instance_types/update:
    parameters:
      - $ref: '#/components/parameters/chain_id'
      - $ref: '#/components/parameters/env_name'
    post:
      summary: Update a chainlet environment's instance type settings.
      description: >-
        Updates a chainlet environment's instance type settings. The chainlet
        environment setting must exist. When updated, a new chain deployment is
        created and deployed. It is promoted to the chain environment according
        to promotion settings on the environment.
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/UpdateChainletEnvironmentInstanceTypeRequestV1
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/UpdateChainletEnvironmentInstanceTypeResponseV1
      x-codeSamples:
        - lang: bash
          source: >-
            curl --request POST \

            --url
            https://api.baseten.co/v1/chains/{chain_id}/environments/{env_name}/chainlet_settings/instance_types/update
            \

            --header "Authorization: Bearer $BASETEN_API_KEY" \

            --data '{
              "updates": [
                {
                  "chainlet_name": "HelloWorld",
                  "instance_type_id": "1x4"
                },
                {
                  "chainlet_name": "RandInt",
                  "instance_type_id": "A10G:2x24x96"
                }
              ]
            }'
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/chains/{chain_id}/environments/{env_name}/chainlet_settings/instance_types/update"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "POST",
                url,
                headers=headers,
                json={'updates': [{'chainlet_name': 'HelloWorld', 'instance_type_id': '1x4'}, {'chainlet_name': 'RandInt', 'instance_type_id': 'A10G:2x24x96'}]}
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
    UpdateChainletEnvironmentInstanceTypeRequestV1:
      description: >-
        A request to update the instance types for chainlets in an environment.
        Multiples

        updates can be made in one request. The updates will be processed in
        batch and a new deployment

        will be created, deployed and promoted into the environment.
      properties:
        updates:
          description: >-
            Mapping of chainlet name to the desired chainlet instance type. If
            the chainlet name doesn't exist, an error is returned.
          examples:
            - - chainlet_name: HelloWorld
                instance_type_id: 1x4
              - chainlet_name: RandInt
                instance_type_id: A10G:2x24x96
          items:
            $ref: '#/components/schemas/ChainletEnvironmentInstanceTypeUpdateV1'
          title: Updates
          type: array
      required:
        - updates
      title: UpdateChainletEnvironmentInstanceTypeRequestV1
      type: object
    UpdateChainletEnvironmentInstanceTypeResponseV1:
      description: >-
        A response to update the environment settings for a chainlet. If
        updating the instance type

        resulted in a re-deployment, `requires_redeployment` will be True and
        the resulting deployment

        will be returned in the `chain_deployment` field.
      properties:
        requires_redeployment:
          description: >-
            Whether the resource update requires a re-deployment to update the
            instance type.
          title: Requires Redeployment
          type: boolean
        chain_deployment:
          anyOf:
            - $ref: '#/components/schemas/ChainDeploymentV1'
            - type: 'null'
          description: The chain deployment resulting from the resource update, if any.
        chainlet_environment_settings:
          description: The updated chainlet environment settings
          items:
            $ref: '#/components/schemas/ChainletEnvironmentSettingsV1'
          title: Chainlet Environment Settings
          type: array
      required:
        - requires_redeployment
        - chain_deployment
        - chainlet_environment_settings
      title: UpdateChainletEnvironmentInstanceTypeResponseV1
      type: object
    ChainletEnvironmentInstanceTypeUpdateV1:
      description: A request to update the environment settings for a chainlet.
      properties:
        chainlet_name:
          description: Name of the chainlet
          examples:
            - HelloWorld
          title: Chainlet Name
          type: string
        instance_type_id:
          description: Key of the instance type to use for the chainlet
          examples:
            - 1x4
            - 2x8
            - A10G:2x24x96
          title: Instance Type Id
          type: string
      required:
        - chainlet_name
        - instance_type_id
      title: ChainletEnvironmentInstanceTypeUpdateV1
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
    ChainletEnvironmentSettingsV1:
      description: Environment settings for a chainlet.
      properties:
        chainlet_name:
          description: Name of the chainlet
          title: Chainlet Name
          type: string
        autoscaling_settings:
          anyOf:
            - $ref: '#/components/schemas/AutoscalingSettingsV1'
            - type: 'null'
          description: >-
            Autoscaling settings for the chainlet. If null, it has not finished
            deploying
        instance_type:
          $ref: '#/components/schemas/InstanceTypeV1'
          description: Instance type for the chainlet
      required:
        - chainlet_name
        - autoscaling_settings
        - instance_type
      title: ChainletEnvironmentSettingsV1
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
