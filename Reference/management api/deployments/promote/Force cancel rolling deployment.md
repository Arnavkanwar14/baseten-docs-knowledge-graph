---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/deployments/promote/force-cancel-promotion
---

> Immediately cancels an in-progress rolling promotion and triggers rollback to the previous version.

## OpenAPI

````yaml post /v1/models/{model_id}/environments/{env_name}/force_cancel_promotion
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
  /v1/models/{model_id}/environments/{env_name}/force_cancel_promotion:
    parameters:
      - $ref: '#/components/parameters/model_id'
      - $ref: '#/components/parameters/env_name'
    post:
      summary: Force cancels a rolling promotion
      description: >-
        Immediately cancels an in-progress rolling promotion and triggers
        rollback to the previous version.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SignalPromotionResponseV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request POST \

            --url
            https://api.baseten.co/v1/models/{model_id}/environments/{env_name}/force_cancel_promotion
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/models/{model_id}/environments/{env_name}/force_cancel_promotion"

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
    env_name:
      schema:
        type: string
      name: env_name
      in: path
      required: true
  schemas:
    SignalPromotionResponseV1:
      description: The response to a request to signal a rolling promotion.
      properties:
        success:
          description: Whether the signal was successfully sent
          title: Success
          type: boolean
      required:
        - success
      title: SignalPromotionResponseV1
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
