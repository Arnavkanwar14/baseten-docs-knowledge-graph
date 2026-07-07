---
tags: [baseten, reference, loops-api]
source: https://docs.baseten.co/reference/loops-api/deployments/list-deployments
---

> List Loops deployments. Defaults to the caller's own; pass ?scope=org to list every deployment in the caller's organization. Returns every deployment regardless of status; clients filter terminal states.

## OpenAPI

````yaml get /v1/loops/deployments
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
  /v1/loops/deployments:
    get:
      summary: List Loops deployments.
      description: >-
        List Loops deployments. Defaults to the caller's own; pass ?scope=org to
        list every deployment in the caller's organization. Returns every
        deployment regardless of status; clients filter terminal states.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListLoopsDeploymentsResponseV1'
      x-codeSamples:
        - lang: bash
          source: |
            curl --request GET \
            --url https://api.baseten.co/v1/loops/deployments \
            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/loops/deployments"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "GET",
                url,
                headers=headers,
                json={}
            )

            print(response.text)
components:
  schemas:
    ListLoopsDeploymentsResponseV1:
      description: >-
        Response for ``GET /v1/loops/deployments``.

        Defaults to the caller's own; pass ``?scope=org`` to list every
        deployment in

        the caller's organization. Returns every deployment regardless of
        status;

        clients filter terminal states.
      properties:
        deployments:
          description: Active Loops deployments.
          items:
            $ref: '#/components/schemas/LoopsDeploymentV1'
          title: Deployments
          type: array
      required:
        - deployments
      title: ListLoopsDeploymentsResponseV1
      type: object
    LoopsDeploymentV1:
      description: |-
        A Loops deployment — the long-lived run + sampler pair owned by a user.

        The deployment's current sampler is included inline. The full list of
        samplers visible to the caller (across all deployments) lives at
        ``GET /v1/loops/samplers``.
      properties:
        id:
          description: The Loops deployment ID.
          title: Id
          type: string
        base_model:
          description: The HuggingFace base model the deployment is fine-tuning.
          title: Base Model
          type: string
        base_url:
          description: The run's base URL.
          title: Base Url
          type: string
        status:
          $ref: '#/components/schemas/LoopsDeploymentStatusV1'
          description: Latest deployment status.
        user:
          $ref: '#/components/schemas/UserV1'
          description: The user who owns the Loops deployment.
        sampler:
          anyOf:
            - $ref: '#/components/schemas/LoopsSamplerV1'
            - type: 'null'
          default: null
          description: The sampler bound to this deployment.
      required:
        - id
        - base_model
        - base_url
        - status
        - user
      title: LoopsDeploymentV1
      type: object
    LoopsDeploymentStatusV1:
      description: Latest deployment status for a Loops deployment.
      properties:
        name:
          $ref: '#/components/schemas/Name'
          description: Latest status of the Loops deployment.
      required:
        - name
      title: LoopsDeploymentStatusV1
      type: object
    UserV1:
      description: A user.
      properties:
        email:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Email of the user.
          title: Email
      title: UserV1
      type: object
    LoopsSamplerV1:
      properties:
        id:
          title: Id
          type: string
        base_url:
          title: Base Url
          type: string
        base_model:
          description: The HuggingFace base model the sampler is serving.
          title: Base Model
          type: string
        created_at:
          description: Time the sampler was created in ISO 8601 format
          format: date-time
          title: Created At
          type: string
        model_id:
          description: Hashid of the underlying Baseten model.
          title: Model Id
          type: string
        deployment_id:
          description: Hashid of the specific model deployment (version).
          title: Deployment Id
          type: string
        status:
          $ref: '#/components/schemas/LoopsSamplerStatusV1'
          description: The sampler's current status.
      required:
        - id
        - base_url
        - base_model
        - created_at
        - model_id
        - deployment_id
        - status
      title: LoopsSamplerV1
      type: object
    Name:
      enum:
        - CREATED
        - DEPLOYING
        - RUNNING
        - SCALED_TO_ZERO
        - FAILED
        - STOPPED
      title: LoopsDeploymentStatus
      type: string
    LoopsSamplerStatusV1:
      description: The current status of a Loops sampler.
      properties:
        name:
          $ref: '#/components/schemas/DeploymentStatusV1'
          description: The current status of the Loops sampler.
      required:
        - name
      title: LoopsSamplerStatusV1
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
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Send `Authorization: Bearer <api_key>`. The legacy `Authorization:
        Api-Key <api_key>` scheme is also accepted.

````

---
Part of [[Loops Api (Reference)]]
