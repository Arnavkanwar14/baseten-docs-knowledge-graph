---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/billing/gets-billing-usage-summary-for-a-date-range
---

> Returns billing usage data within the specified date range. Includes dedicated model serving, training, and model APIs usage. The date range must not exceed 31 days.

## OpenAPI

````yaml get /v1/billing/usage_summary
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
  /v1/billing/usage_summary:
    get:
      summary: Gets billing usage summary for a date range
      description: >-
        Returns billing usage data within the specified date range. Includes
        dedicated model serving, training, and model APIs usage. The date range
        must not exceed 31 days.
      parameters:
        - name: start_date
          in: query
          required: true
          description: 'Start date (ISO 8601, UTC). Earliest queryable: 2026-01-01.'
          schema:
            format: date-time
            title: Start Date
            type: string
        - name: end_date
          in: query
          required: true
          description: End date in ISO 8601 format (UTC). Date range cannot exceed 31 days.
          schema:
            format: date-time
            title: End Date
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UsageSummaryV1'
      x-codeSamples:
        - lang: bash
          source: |
            curl --request GET \
            --url https://api.baseten.co/v1/billing/usage_summary \
            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: |-
            import requests
            import os
            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
            url = "https://api.baseten.co/v1/billing/usage_summary"

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
    UsageSummaryV1:
      description: Billing usage summary for the requested date range.
      properties:
        dedicated_usage:
          anyOf:
            - $ref: '#/components/schemas/DedicatedUsageV1'
            - type: 'null'
          default: null
          description: Dedicated model serving usage
        training_usage:
          anyOf:
            - $ref: '#/components/schemas/TrainingUsageV1'
            - type: 'null'
          default: null
          description: Training usage
        model_apis_usage:
          anyOf:
            - $ref: '#/components/schemas/ModelApisUsageV1'
            - type: 'null'
          default: null
          description: Model APIs usage
      title: UsageSummaryV1
      type: object
    DedicatedUsageV1:
      properties:
        subtotal:
          anyOf:
            - type: number
            - pattern: ^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$
              type: string
          description: Subtotal cost in dollars after applying credits used
          title: Subtotal
        credits_used:
          anyOf:
            - type: number
            - pattern: ^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$
              type: string
          description: Credits applied in dollars
          title: Credits Used
        total:
          anyOf:
            - type: number
            - pattern: ^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$
              type: string
          description: Total cost in dollars
          title: Total
        minutes:
          description: Total minutes used
          title: Minutes
          type: integer
        breakdown:
          description: Per-deployment usage breakdown
          items:
            $ref: '#/components/schemas/DedicatedItemV1'
          title: Breakdown
          type: array
      required:
        - subtotal
        - credits_used
        - total
        - minutes
      title: DedicatedUsageV1
      type: object
    TrainingUsageV1:
      properties:
        subtotal:
          anyOf:
            - type: number
            - pattern: ^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$
              type: string
          description: Subtotal cost in dollars after applying credits used
          title: Subtotal
        credits_used:
          anyOf:
            - type: number
            - pattern: ^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$
              type: string
          description: Credits applied in dollars
          title: Credits Used
        total:
          anyOf:
            - type: number
            - pattern: ^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$
              type: string
          description: Total cost in dollars
          title: Total
        minutes:
          description: Total minutes used
          title: Minutes
          type: integer
        breakdown:
          description: Per-job usage breakdown
          items:
            $ref: '#/components/schemas/TrainingItemV1'
          title: Breakdown
          type: array
      required:
        - subtotal
        - credits_used
        - total
        - minutes
      title: TrainingUsageV1
      type: object
    ModelApisUsageV1:
      properties:
        subtotal:
          anyOf:
            - type: number
            - pattern: ^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$
              type: string
          description: Subtotal cost in dollars after applying credits used
          title: Subtotal
        credits_used:
          anyOf:
            - type: number
            - pattern: ^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$
              type: string
          description: Credits applied in dollars
          title: Credits Used
        total:
          anyOf:
            - type: number
            - pattern: ^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$
              type: string
          description: Total cost in dollars
          title: Total
        breakdown:
          description: Per-model usage breakdown
          items:
            $ref: '#/components/schemas/ModelApiItemV1'
          title: Breakdown
          type: array
      required:
        - subtotal
        - credits_used
        - total
      title: ModelApisUsageV1
      type: object
    DedicatedItemV1:
      properties:
        billable_resource:
          $ref: '#/components/schemas/BillableResourceV1'
          description: The model deployment resource
        subtotal:
          anyOf:
            - type: number
            - pattern: ^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$
              type: string
          description: Subtotal cost in dollars for this billable resource
          title: Subtotal
        minutes:
          description: Total minutes used for this billable resource
          title: Minutes
          type: integer
        inference_requests:
          description: Total inference requests for this billable resource
          title: Inference Requests
          type: integer
        daily:
          description: Daily usage breakdown
          items:
            $ref: '#/components/schemas/DailyDedicatedUsageV1'
          title: Daily
          type: array
      required:
        - billable_resource
        - subtotal
        - minutes
        - inference_requests
      title: DedicatedItemV1
      type: object
    TrainingItemV1:
      properties:
        billable_resource:
          $ref: '#/components/schemas/BillableResourceV1'
          description: The training job resource
        subtotal:
          anyOf:
            - type: number
            - pattern: ^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$
              type: string
          description: Subtotal cost in dollars for this billable resource
          title: Subtotal
        minutes:
          description: Total minutes used for this billable resource
          title: Minutes
          type: integer
        daily:
          description: Daily usage breakdown
          items:
            $ref: '#/components/schemas/DailyTrainingUsageV1'
          title: Daily
          type: array
      required:
        - billable_resource
        - subtotal
        - minutes
      title: TrainingItemV1
      type: object
    ModelApiItemV1:
      properties:
        model_name:
          description: Model name
          title: Model Name
          type: string
        model_family:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Model family (e.g., llama, mistral)
          title: Model Family
        subtotal:
          anyOf:
            - type: number
            - pattern: ^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$
              type: string
          description: Subtotal cost in dollars for this model
          title: Subtotal
        input_tokens:
          description: Total input tokens for this model
          title: Input Tokens
          type: integer
        output_tokens:
          description: Total output tokens for this model
          title: Output Tokens
          type: integer
        cached_input_tokens:
          description: Total cached input tokens for this model
          title: Cached Input Tokens
          type: integer
        daily:
          description: Daily usage breakdown
          items:
            $ref: '#/components/schemas/DailyModelApiUsageV1'
          title: Daily
          type: array
      required:
        - model_name
        - subtotal
        - input_tokens
        - output_tokens
        - cached_input_tokens
      title: ModelApiItemV1
      type: object
    BillableResourceV1:
      properties:
        id:
          description: Unique identifier of the resource
          title: Id
          type: string
        kind:
          $ref: '#/components/schemas/ResourceKind'
          description: Resource kind (MODEL_DEPLOYMENT, TRAINING_JOB, or CHAINLET)
        name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Name of the resource
          title: Name
        model_name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: >-
            Name of the parent resource (e.g., model name for model deployments,
            training project name for training jobs)
          title: Model Name
        is_deleted:
          description: Indicates if the resource has been deleted
          title: Is Deleted
          type: boolean
        instance_type:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Instance type used
          title: Instance Type
        environment_name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Environment name (e.g., 'production', 'staging')
          title: Environment Name
        chain_metadata:
          anyOf:
            - $ref: '#/components/schemas/ChainMetadataV1'
            - type: 'null'
          default: null
          description: Chain metadata if this is a chainlet deployment
      required:
        - id
        - kind
        - is_deleted
      title: BillableResourceV1
      type: object
    DailyDedicatedUsageV1:
      properties:
        date:
          description: Date of the usage
          format: date
          title: Date
          type: string
        subtotal:
          anyOf:
            - type: number
            - pattern: ^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$
              type: string
          description: Subtotal cost incurred on this date in dollars
          title: Subtotal
        minutes:
          description: Minutes used on this date
          title: Minutes
          type: integer
        inference_requests:
          description: Number of inference requests on this date
          title: Inference Requests
          type: integer
      required:
        - date
        - subtotal
        - minutes
        - inference_requests
      title: DailyDedicatedUsageV1
      type: object
    DailyTrainingUsageV1:
      properties:
        date:
          description: Date of the usage
          format: date
          title: Date
          type: string
        subtotal:
          anyOf:
            - type: number
            - pattern: ^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$
              type: string
          description: Subtotal cost incurred on this date in dollars
          title: Subtotal
        minutes:
          description: Minutes used on this date
          title: Minutes
          type: integer
      required:
        - date
        - subtotal
        - minutes
      title: DailyTrainingUsageV1
      type: object
    DailyModelApiUsageV1:
      properties:
        date:
          description: Date of the usage
          format: date
          title: Date
          type: string
        subtotal:
          anyOf:
            - type: number
            - pattern: ^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$
              type: string
          description: Subtotal cost incurred on this date in dollars
          title: Subtotal
        input_tokens:
          description: Number of input tokens on this date
          title: Input Tokens
          type: integer
        output_tokens:
          description: Number of output tokens on this date
          title: Output Tokens
          type: integer
        cached_input_tokens:
          description: Number of cached input tokens on this date
          title: Cached Input Tokens
          type: integer
      required:
        - date
        - subtotal
        - input_tokens
        - output_tokens
        - cached_input_tokens
      title: DailyModelApiUsageV1
      type: object
    ResourceKind:
      enum:
        - MODEL_DEPLOYMENT
        - TRAINING_JOB
        - CHAINLET
      title: ResourceKind
      type: string
    ChainMetadataV1:
      properties:
        chain_id:
          description: Unique identifier of the chain
          title: Chain Id
          type: string
        chain_name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Name of the chain
          title: Chain Name
        chain_deployment_id:
          description: Unique identifier of the chain deployment
          title: Chain Deployment Id
          type: string
      required:
        - chain_id
        - chain_deployment_id
      title: ChainMetadataV1
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
