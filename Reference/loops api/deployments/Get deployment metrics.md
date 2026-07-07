---
tags: [baseten, reference, loops-api]
source: https://docs.baseten.co/reference/loops-api/deployments/get-deployment-metrics
---

> Returns per-node GPU/CPU/memory utilization and Knative queue-proxy request rate / concurrency / latency for the trainer pods. The sampler half of a Loops deployment is an OracleVersion and uses the existing model-metrics endpoint.

## OpenAPI

````yaml post /v1/loops/deployments/{deployment_id}/metrics
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
  /v1/loops/deployments/{deployment_id}/metrics:
    parameters:
      - $ref: '#/components/parameters/deployment_id'
    post:
      summary: Get metrics for a Loops trainer deployment.
      description: >-
        Returns per-node GPU/CPU/memory utilization and Knative queue-proxy
        request rate / concurrency / latency for the trainer pods. The sampler
        half of a Loops deployment is an OracleVersion and uses the existing
        model-metrics endpoint.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GetLoopsDeploymentMetricsRequestV1'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetLoopsDeploymentMetricsResponseV1'
      x-codeSamples:
        - lang: bash
          source: >-
            curl --request POST \

            --url
            https://api.baseten.co/v1/loops/deployments/{deployment_id}/metrics
            \

            --header "Authorization: Bearer $BASETEN_API_KEY" \

            --data '{
              "end_epoch_millis": null,
              "start_epoch_millis": null,
              "step_seconds": null,
              "time_divisor_seconds": null
            }'
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/loops/deployments/{deployment_id}/metrics"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "POST",
                url,
                headers=headers,
                json={'end_epoch_millis': None, 'start_epoch_millis': None, 'step_seconds': None, 'time_divisor_seconds': None}
            )

            print(response.text)
components:
  parameters:
    deployment_id:
      schema:
        type: string
      name: deployment_id
      in: path
      required: true
  schemas:
    GetLoopsDeploymentMetricsRequestV1:
      description: Time-range request for trainer deployment metrics.
      properties:
        end_epoch_millis:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Epoch millis to end fetching metrics.
          title: End Epoch Millis
        start_epoch_millis:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Epoch millis to start fetching metrics.
          title: Start Epoch Millis
        step_seconds:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: >-
            Resolution of the returned series, in seconds. When omitted, a step
            is derived from the time range so large windows return fewer points.
          title: Step Seconds
        time_divisor_seconds:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: >-
            Unit of time for request-volume metrics, in seconds (e.g. 60 for
            requests/minute). Defaults to per-second.
          title: Time Divisor Seconds
      title: GetLoopsDeploymentMetricsRequestV1
      type: object
    GetLoopsDeploymentMetricsResponseV1:
      description: Response for ``POST /v1/loops/deployments/<id>/metrics``.
      properties:
        deployment_id:
          description: The trainer deployment ID.
          title: Deployment Id
          type: string
        metrics:
          $ref: '#/components/schemas/LoopsDeploymentMetricsV1'
          description: Metrics for the deployment.
      required:
        - deployment_id
        - metrics
      title: GetLoopsDeploymentMetricsResponseV1
      type: object
    LoopsDeploymentMetricsV1:
      description: |-
        Metrics for a trainer (Loops) deployment.

        Service-level fields summarize HTTP traffic into the trainer pods (the
        Knative queue-proxy is the source). Compute fields are the leader-pod
        aggregate; ``per_node_metrics`` carries the full multinode breakdown.
      properties:
        inference_volume:
          description: Number of inference requests per unit time (requests per second).
          items:
            $ref: '#/components/schemas/TrainingJobMetricV1'
          title: Inference Volume
          type: array
        concurrent_requests:
          description: >-
            Number of in-progress concurrent inference requests. Source: the
            queue-proxy ``revision_queue_depth`` gauge on ``http-usermetric``.
          items:
            $ref: '#/components/schemas/TrainingJobMetricV1'
          title: Concurrent Requests
          type: array
        response_time_stats:
          description: Percentiles of the response time distribution.
          items:
            $ref: '#/components/schemas/ResponseTimeDatapointV1'
          title: Response Time Stats
          type: array
        inference_volume_by_status:
          description: Request rate split by response code class.
          items:
            $ref: '#/components/schemas/InferenceVolumeByStatusDatapointV1'
          title: Inference Volume By Status
          type: array
        gpu_memory_usage_bytes:
          additionalProperties:
            items:
              $ref: '#/components/schemas/TrainingJobMetricV1'
            type: array
          description: Leader-pod GPU memory bytes per GPU rank.
          title: Gpu Memory Usage Bytes
          type: object
        gpu_utilization:
          additionalProperties:
            items:
              $ref: '#/components/schemas/TrainingJobMetricV1'
            type: array
          description: Leader-pod fractional GPU utilization per GPU rank.
          title: Gpu Utilization
          type: object
        cpu_usage:
          description: Leader-pod CPU usage in cores.
          items:
            $ref: '#/components/schemas/TrainingJobMetricV1'
          title: Cpu Usage
          type: array
        cpu_memory_usage_bytes:
          description: Leader-pod CPU memory usage bytes.
          items:
            $ref: '#/components/schemas/TrainingJobMetricV1'
          title: Cpu Memory Usage Bytes
          type: array
        ephemeral_storage:
          $ref: '#/components/schemas/StorageMetricsV1'
          description: Leader-pod ephemeral storage usage.
        per_node_metrics:
          description: Per-node compute breakdown for multinode trainer deployments.
          items:
            $ref: '#/components/schemas/LoopsDeploymentNodeMetricsV1'
          title: Per Node Metrics
          type: array
      required:
        - inference_volume
        - concurrent_requests
        - response_time_stats
        - inference_volume_by_status
        - gpu_memory_usage_bytes
        - gpu_utilization
        - cpu_usage
        - cpu_memory_usage_bytes
        - ephemeral_storage
        - per_node_metrics
      title: LoopsDeploymentMetricsV1
      type: object
    TrainingJobMetricV1:
      description: A metric for a training job.
      properties:
        value:
          description: The value of the metric.
          title: Value
          type: number
        timestamp:
          description: The timestamp of the metric in ISO 8601 format.
          format: date-time
          title: Timestamp
          type: string
      required:
        - value
        - timestamp
      title: TrainingJobMetricV1
      type: object
    ResponseTimeDatapointV1:
      description: >-
        Latency quantile datapoint.

        Values are reported in **milliseconds** to match the oracle/inference

        ``response_time_stats`` convention. Source histogram is the
        queue-proxy's

        ``revision_request_latencies_bucket`` whose bucket boundaries are in ms.
      properties:
        timestamp:
          description: ISO 8601 timestamp.
          format: date-time
          title: Timestamp
          type: string
        p50:
          anyOf:
            - type: number
            - type: 'null'
          default: null
          description: 50th percentile request latency (milliseconds).
          title: P50
        p95:
          anyOf:
            - type: number
            - type: 'null'
          default: null
          description: 95th percentile request latency (milliseconds).
          title: P95
        p99:
          anyOf:
            - type: number
            - type: 'null'
          default: null
          description: 99th percentile request latency (milliseconds).
          title: P99
      required:
        - timestamp
      title: ResponseTimeDatapointV1
      type: object
    InferenceVolumeByStatusDatapointV1:
      description: Request rate split by HTTP response code class.
      properties:
        timestamp:
          description: ISO 8601 timestamp.
          format: date-time
          title: Timestamp
          type: string
        status_2xx:
          description: 2xx requests per second.
          title: Status 2Xx
          type: number
        status_4xx:
          description: 4xx requests per second.
          title: Status 4Xx
          type: number
        status_5xx:
          description: 5xx requests per second.
          title: Status 5Xx
          type: number
      required:
        - timestamp
        - status_2xx
        - status_4xx
        - status_5xx
      title: InferenceVolumeByStatusDatapointV1
      type: object
    StorageMetricsV1:
      description: A metric for a training job.
      properties:
        usage_bytes:
          description: The number of bytes used on the storage entity.
          items:
            $ref: '#/components/schemas/TrainingJobMetricV1'
          title: Usage Bytes
          type: array
        utilization:
          description: The utilization of the storage entity as a decimal percentage.
          items:
            $ref: '#/components/schemas/TrainingJobMetricV1'
          title: Utilization
          type: array
      required:
        - usage_bytes
        - utilization
      title: StorageMetricsV1
      type: object
    LoopsDeploymentNodeMetricsV1:
      description: Per-node compute metrics for a multinode trainer deployment.
      properties:
        node_id:
          description: Identifier for the node.
          title: Node Id
          type: string
        gpu_memory_usage_bytes:
          additionalProperties:
            items:
              $ref: '#/components/schemas/TrainingJobMetricV1'
            type: array
          description: GPU memory usage bytes per GPU rank.
          title: Gpu Memory Usage Bytes
          type: object
        gpu_utilization:
          additionalProperties:
            items:
              $ref: '#/components/schemas/TrainingJobMetricV1'
            type: array
          description: Fractional GPU utilization per GPU rank.
          title: Gpu Utilization
          type: object
        cpu_usage:
          description: CPU usage in cores.
          items:
            $ref: '#/components/schemas/TrainingJobMetricV1'
          title: Cpu Usage
          type: array
        cpu_memory_usage_bytes:
          description: CPU memory usage bytes.
          items:
            $ref: '#/components/schemas/TrainingJobMetricV1'
          title: Cpu Memory Usage Bytes
          type: array
        ephemeral_storage:
          $ref: '#/components/schemas/StorageMetricsV1'
          description: Ephemeral storage usage.
      required:
        - node_id
        - gpu_memory_usage_bytes
        - gpu_utilization
        - cpu_usage
        - cpu_memory_usage_bytes
        - ephemeral_storage
      title: LoopsDeploymentNodeMetricsV1
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
