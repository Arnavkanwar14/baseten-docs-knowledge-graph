---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/deployments/autoscaling/update-a-chainlet-environments-autoscaling-settings
---

> Updates a chainlet environment's autoscaling settings and returns the updated chainlet environment settings.

## OpenAPI

````yaml patch /v1/chains/{chain_id}/environments/{env_name}/chainlet_settings/autoscaling_settings
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
  /v1/chains/{chain_id}/environments/{env_name}/chainlet_settings/autoscaling_settings:
    parameters:
      - $ref: '#/components/parameters/chain_id'
      - $ref: '#/components/parameters/env_name'
    patch:
      summary: Update a chainlet environment's autoscaling settings
      description: >-
        Updates a chainlet environment's autoscaling settings and returns the
        updated chainlet environment settings.
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/UpdateChainletEnvironmentAutoscalingSettingsRequestV1
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
            https://api.baseten.co/v1/chains/{chain_id}/environments/{env_name}/chainlet_settings/autoscaling_settings
            \

            --header "Authorization: Bearer $BASETEN_API_KEY" \

            --data '{
              "updates": [
                {
                  "autoscaling_settings": {
                    "autoscaling_window": 800,
                    "concurrency_target": 4,
                    "max_replica": 3,
                    "max_scale_down_rate": null,
                    "min_replica": 2,
                    "scale_down_delay": 63,
                    "target_in_flight_tokens": null,
                    "target_utilization_percentage": null
                  },
                  "chainlet_name": "HelloWorld"
                }
              ]
            }'
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/chains/{chain_id}/environments/{env_name}/chainlet_settings/autoscaling_settings"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "PATCH",
                url,
                headers=headers,
                json={'updates': [{'autoscaling_settings': {'autoscaling_window': 800, 'concurrency_target': 4, 'max_replica': 3, 'max_scale_down_rate': None, 'min_replica': 2, 'scale_down_delay': 63, 'target_in_flight_tokens': None, 'target_utilization_percentage': None}, 'chainlet_name': 'HelloWorld'}]}
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
    UpdateChainletEnvironmentAutoscalingSettingsRequestV1:
      description: >-
        A request to update the autoscaling settings for a multiple chainlets in
        an environment.

        If a chainlet name doesn't exist, an error is returned.
      properties:
        updates:
          description: >-
            Mapping of chainlet name to the desired chainlet autoscaling
            settings. If the chainlet name doesn't exist, an error is returned.
          examples:
            - - autoscaling_settings:
                  autoscaling_window: 800
                  concurrency_target: 4
                  max_replica: 3
                  max_scale_down_rate: null
                  min_replica: 2
                  scale_down_delay: 63
                  target_in_flight_tokens: null
                  target_utilization_percentage: null
                chainlet_name: HelloWorld
            - - autoscaling_settings:
                  autoscaling_window: null
                  concurrency_target: null
                  max_replica: null
                  max_scale_down_rate: null
                  min_replica: 0
                  scale_down_delay: null
                  target_in_flight_tokens: null
                  target_utilization_percentage: null
                chainlet_name: HelloWorld
              - autoscaling_settings:
                  autoscaling_window: null
                  concurrency_target: null
                  max_replica: null
                  max_scale_down_rate: null
                  min_replica: 0
                  scale_down_delay: null
                  target_in_flight_tokens: null
                  target_utilization_percentage: null
                chainlet_name: RandInt
          items:
            $ref: >-
              #/components/schemas/ChainletEnvironmentAutoscalingSettingsUpdateV1
          title: Updates
          type: array
      required:
        - updates
      title: UpdateChainletEnvironmentAutoscalingSettingsRequestV1
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
    ChainletEnvironmentAutoscalingSettingsUpdateV1:
      description: The request to update the autoscaling settings for a chainlet.
      properties:
        chainlet_name:
          description: Name of the chainlet
          examples:
            - HelloWorld
          title: Chainlet Name
          type: string
        autoscaling_settings:
          $ref: '#/components/schemas/UpdateAutoscalingSettingsV1'
          description: Autoscaling settings for the chainlet
          examples:
            - autoscaling_window: 800
              concurrency_target: 3
              max_replica: 2
              max_scale_down_rate: null
              min_replica: 1
              scale_down_delay: 60
              target_in_flight_tokens: null
              target_utilization_percentage: null
      required:
        - chainlet_name
        - autoscaling_settings
      title: ChainletEnvironmentAutoscalingSettingsUpdateV1
      type: object
    UpdateAutoscalingSettingsStatusV1:
      description: The status of a request to update autoscaling settings.
      enum:
        - ACCEPTED
        - QUEUED
        - UNCHANGED
      title: UpdateAutoscalingSettingsStatusV1
      type: string
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
