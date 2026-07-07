---
tags: [baseten, reference, loops-api]
source: https://docs.baseten.co/reference/loops-api/server/get-capabilities
---

> Returns the list of models supported by the Loops server, including each model's maximum context length.

## OpenAPI

````yaml get /v1/loops/capabilities
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
  /v1/loops/capabilities:
    get:
      summary: Get Loops server capabilities.
      description: >-
        Returns the list of models supported by the Loops server, including each
        model's maximum context length.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetLoopsCapabilitiesResponseV1'
      x-codeSamples:
        - lang: bash
          source: |
            curl --request GET \
            --url https://api.baseten.co/v1/loops/capabilities \
            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/loops/capabilities"

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
    GetLoopsCapabilitiesResponseV1:
      description: Response for ``GET /v1/loops/capabilities``.
      properties:
        supported_models:
          description: List of models available on the server.
          items:
            $ref: '#/components/schemas/SupportedModelV1'
          title: Supported Models
          type: array
      required:
        - supported_models
      title: GetLoopsCapabilitiesResponseV1
      type: object
    SupportedModelV1:
      description: A model supported by the Loops server.
      properties:
        model_name:
          description: The name of the supported model.
          title: Model Name
          type: string
        max_context_length:
          description: The maximum context length (in tokens) supported by this model.
          title: Max Context Length
          type: integer
      required:
        - model_name
        - max_context_length
      title: SupportedModelV1
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
Part of [[Loops Api (Reference)]]
