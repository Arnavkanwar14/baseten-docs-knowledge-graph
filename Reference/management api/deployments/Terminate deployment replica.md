---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/deployments/terminates-deployment-replica
---

> Terminates a deployment replica and returns the termination status.

## OpenAPI

````yaml delete /v1/models/{model_id}/deployments/{deployment_id}/replicas/{replica_id}
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
  /v1/models/{model_id}/deployments/{deployment_id}/replicas/{replica_id}:
    parameters:
      - $ref: '#/components/parameters/model_id'
      - $ref: '#/components/parameters/deployment_id'
      - $ref: '#/components/parameters/replica_id'
    delete:
      summary: Terminates a replica in a deployment
      description: Terminates a deployment replica and returns the termination status.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TerminateReplicaResponseV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request DELETE \

            --url
            https://api.baseten.co/v1/models/{model_id}/deployments/{deployment_id}/replicas/{replica_id}
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/models/{model_id}/deployments/{deployment_id}/replicas/{replica_id}"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "DELETE",
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
    replica_id:
      schema:
        type: string
      name: replica_id
      in: path
      required: true
  schemas:
    TerminateReplicaResponseV1:
      description: The response to a request to terminate a replica in a deployment.
      properties:
        success:
          default: true
          description: Whether the replica was successfully terminated
          title: Success
          type: boolean
      title: TerminateReplicaResponseV1
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
