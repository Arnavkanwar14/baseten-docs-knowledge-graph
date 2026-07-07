---
tags: [baseten, reference, training-api]
source: https://docs.baseten.co/reference/training-api/get-training-project
---

> Get the details of an existing training project.

## OpenAPI

````yaml get /v1/training_projects/{training_project_id}
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
  /v1/training_projects/{training_project_id}:
    parameters:
      - $ref: '#/components/parameters/training_project_id'
    get:
      summary: Get a training project.
      description: Get the details of an existing training project.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetTrainingProjectResponseV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request GET \

            --url
            https://api.baseten.co/v1/training_projects/{training_project_id} \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/training_projects/{training_project_id}"

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
  schemas:
    GetTrainingProjectResponseV1:
      description: A response to getting a training project.
      properties:
        training_project:
          $ref: '#/components/schemas/TrainingProjectV1'
          description: The training project.
      required:
        - training_project
      title: GetTrainingProjectResponseV1
      type: object
    TrainingProjectV1:
      properties:
        id:
          description: Unique identifier of the training project
          title: Id
          type: string
        name:
          description: Name of the training project.
          title: Name
          type: string
        created_at:
          description: Time the training project was created in ISO 8601 format.
          format: date-time
          title: Created At
          type: string
        updated_at:
          description: Time the training project was updated in ISO 8601 format.
          format: date-time
          title: Updated At
          type: string
        team_name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Name of the team associated with the training project.
          title: Team Name
        latest_job:
          anyOf:
            - $ref: '#/components/schemas/TrainingJobV1'
            - type: 'null'
          description: Most recently created training job for the training project.
      required:
        - id
        - name
        - created_at
        - updated_at
        - latest_job
      title: TrainingProjectV1
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
