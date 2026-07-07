---
tags: [baseten, reference, training-api]
source: https://docs.baseten.co/reference/training-api/get-training-job-metrics
---

> Get the metrics for a training job.

## OpenAPI

````yaml get /v1/training_projects/{training_project_id}/jobs/{training_job_id}/metrics
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
  /v1/training_projects/{training_project_id}/jobs/{training_job_id}/metrics:
    parameters:
      - $ref: '#/components/parameters/training_project_id'
      - $ref: '#/components/parameters/training_job_id'
    get:
      summary: Get the metrics for a training job.
      description: Get the metrics for a training job.
      parameters:
        - name: end_epoch_millis
          in: query
          required: false
          description: Epoch millis timestamp to end fetching metrics
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            default: null
            title: End Epoch Millis
        - name: start_epoch_millis
          in: query
          required: false
          description: Epoch millis timestamp to start fetching metrics.
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            default: null
            title: Start Epoch Millis
        - name: step_seconds
          in: query
          required: false
          description: >-
            Resolution of the returned series, in seconds. When omitted, a step
            is derived from the time range so large windows return fewer points.
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            default: null
            title: Step Seconds
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetTrainingJobMetricsResponseV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request GET \

            --url
            https://api.baseten.co/v1/training_projects/{training_project_id}/jobs/{training_job_id}/metrics
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/training_projects/{training_project_id}/jobs/{training_job_id}/metrics"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "GET",
                url,
                headers=headers,
                json={}
            )

            print(response.text)
components:
  parameters:
    training_project_id:
      schema:
        type: string
      name: training_project_id
      in: path
      required: true
    training_job_id:
      schema:
        type: string
      name: training_job_id
      in: path
      required: true
  schemas:
    GetTrainingJobMetricsResponseV1:
      description: >-
        A response to fetch training job metrics. The outer list for each metric
        represents that metric across time.
      properties:
        gpu_memory_usage_bytes:
          additionalProperties:
            items:
              $ref: '#/components/schemas/TrainingJobMetricV1'
            type: array
          description: >-
            A map of GPU rank to memory usage for the training job. For
            multinode jobs, this is the memory usage of the leader unless
            specified otherwise.
          title: Gpu Memory Usage Bytes
          type: object
        gpu_utilization:
          additionalProperties:
            items:
              $ref: '#/components/schemas/TrainingJobMetricV1'
            type: array
          description: >-
            A map of GPU rank to fractional GPU utilization. For multinode jobs,
            this is the GPU utilization of the leader unless specified
            otherwise.
          title: Gpu Utilization
          type: object
        cpu_usage:
          description: >-
            The CPU usage measured in cores. For multinode jobs, this is the CPU
            usage of the leader unless specified otherwise.
          items:
            $ref: '#/components/schemas/TrainingJobMetricV1'
          title: Cpu Usage
          type: array
        cpu_memory_usage_bytes:
          description: >-
            The CPU memory usage for the training job. For multinode jobs, this
            is the CPU memory usage of the leader unless specified otherwise.
          items:
            $ref: '#/components/schemas/TrainingJobMetricV1'
          title: Cpu Memory Usage Bytes
          type: array
        ephemeral_storage:
          $ref: '#/components/schemas/StorageMetricsV1'
          description: >-
            The storage usage for the ephemeral storage. For multinode jobs,
            this is the ephemeral storage usage of the leader unless specified
            otherwise.
        training_job:
          $ref: '#/components/schemas/TrainingJobV1'
          description: The training job.
        cache:
          anyOf:
            - $ref: '#/components/schemas/StorageMetricsV1'
            - type: 'null'
          description: The storage usage for the read-write cache.
        per_node_metrics:
          description: The metrics for each node in the training job.
          items:
            $ref: '#/components/schemas/TrainingJobNodeMetricsV1'
          title: Per Node Metrics
          type: array
      required:
        - gpu_memory_usage_bytes
        - gpu_utilization
        - cpu_usage
        - cpu_memory_usage_bytes
        - ephemeral_storage
        - training_job
        - cache
        - per_node_metrics
      title: GetTrainingJobMetricsResponseV1
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
    TrainingJobV1:
      properties:
        id:
          description: Unique identifier of the training job.
          title: Id
          type: string
        created_at:
          description: Time the job was created in ISO 8601 format.
          format: date-time
          title: Created At
          type: string
        current_status:
          description: Current status of the training job.
          title: Current Status
          type: string
        error_message:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Error message if the training job failed.
          title: Error Message
        instance_type:
          $ref: '#/components/schemas/InstanceTypeV1'
          description: Instance type of the training job.
        updated_at:
          description: Time the job was updated in ISO 8601 format.
          format: date-time
          title: Updated At
          type: string
        training_project_id:
          description: ID of the training project.
          title: Training Project Id
          type: string
        training_project:
          $ref: '#/components/schemas/TrainingProjectSummaryV1'
          description: Summary of the training project.
        name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Name of the training job.
          examples:
            - gpt-oss-job
          title: Name
        checkpoint_sync_status:
          anyOf:
            - $ref: '#/components/schemas/CheckpointSyncStatus'
            - type: 'null'
          default: null
          description: Checkpoint sync status of the training job.
        priority:
          default: 0
          description: >-
            Queue priority. Higher values are dequeued first. NULL is treated as
            0.
          title: Priority
          type: integer
        availability_model:
          $ref: '#/components/schemas/V1AvailabilityModel'
          default: dedicated
          description: >-
            Capacity guarantee for the job. 'dedicated' is non-preemptible
            on-demand capacity; 'spot' is interruptible.
        user:
          anyOf:
            - $ref: '#/components/schemas/UserV1'
            - type: 'null'
          default: null
          description: The user who created the training job.
      required:
        - id
        - created_at
        - current_status
        - instance_type
        - updated_at
        - training_project_id
        - training_project
      title: TrainingJobV1
      type: object
    TrainingJobNodeMetricsV1:
      description: A set of metrics for a training job node.
      properties:
        node_id:
          description: The name of the node.
          title: Node Id
          type: string
        metrics:
          $ref: '#/components/schemas/TrainingJobMetricsV1'
          description: The metrics for the node.
      required:
        - node_id
        - metrics
      title: TrainingJobNodeMetricsV1
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
    TrainingProjectSummaryV1:
      description: A summary of a training project.
      properties:
        id:
          description: Unique identifier of the training project.
          title: Id
          type: string
        name:
          description: Name of the training project.
          title: Name
          type: string
      required:
        - id
        - name
      title: TrainingProjectSummaryV1
      type: object
    CheckpointSyncStatus:
      description: Lifecycle state for the checkpoint uploader.
      enum:
        - SYNCING
        - COMPLETED
      title: CheckpointSyncStatus
      type: string
    V1AvailabilityModel:
      description: >-
        Capacity guarantee under which a training job is scheduled.

        ``DEDICATED`` is on-demand capacity that is not preempted (the default).
        ``SPOT`` is

        interruptible capacity that may be preempted; the user is responsible
        for checkpointing

        their own progress. A managed/resumable model where the platform handles

        checkpoint/resume on its own is intentionally not defined yet; it is
        planned for a

        future milestone.
      enum:
        - dedicated
        - spot
      title: V1AvailabilityModel
      type: string
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
    TrainingJobMetricsV1:
      properties:
        gpu_memory_usage_bytes:
          additionalProperties:
            items:
              $ref: '#/components/schemas/TrainingJobMetricV1'
            type: array
          description: >-
            A map of GPU rank to memory usage for the training job. For
            multinode jobs, this is the memory usage of the leader unless
            specified otherwise.
          title: Gpu Memory Usage Bytes
          type: object
        gpu_utilization:
          additionalProperties:
            items:
              $ref: '#/components/schemas/TrainingJobMetricV1'
            type: array
          description: >-
            A map of GPU rank to fractional GPU utilization. For multinode jobs,
            this is the GPU utilization of the leader unless specified
            otherwise.
          title: Gpu Utilization
          type: object
        cpu_usage:
          description: >-
            The CPU usage measured in cores. For multinode jobs, this is the CPU
            usage of the leader unless specified otherwise.
          items:
            $ref: '#/components/schemas/TrainingJobMetricV1'
          title: Cpu Usage
          type: array
        cpu_memory_usage_bytes:
          description: >-
            The CPU memory usage for the training job. For multinode jobs, this
            is the CPU memory usage of the leader unless specified otherwise.
          items:
            $ref: '#/components/schemas/TrainingJobMetricV1'
          title: Cpu Memory Usage Bytes
          type: array
        ephemeral_storage:
          $ref: '#/components/schemas/StorageMetricsV1'
          description: >-
            The storage usage for the ephemeral storage. For multinode jobs,
            this is the ephemeral storage usage of the leader unless specified
            otherwise.
      required:
        - gpu_memory_usage_bytes
        - gpu_utilization
        - cpu_usage
        - cpu_memory_usage_bytes
        - ephemeral_storage
      title: TrainingJobMetricsV1
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
Part of [[Training Api (Reference)]]
