---
tags: [baseten, reference, training-api]
source: https://docs.baseten.co/reference/training-api/get-training-job-queue-context
---

> Returns the (org, gpu_type) capacity pool the job was gated by, jobs that were holding GPU capacity in that pool when this job was submitted, and every TrainingJobStatus event in [submitted_at, released_at] for those jobs — useful for understanding why a job sat in PENDING. Caller must be an org admin and the job must belong to the caller's org.

## OpenAPI

````yaml get /v1/training/jobs/{training_job_id}/queue_context
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
  /v1/training/jobs/{training_job_id}/queue_context:
    parameters:
      - $ref: '#/components/parameters/training_job_id'
    get:
      summary: Reconstruct queue context for a training job.
      description: >-
        Returns the (org, gpu_type) capacity pool the job was gated by, jobs
        that were holding GPU capacity in that pool when this job was submitted,
        and every TrainingJobStatus event in [submitted_at, released_at] for
        those jobs — useful for understanding why a job sat in PENDING. Caller
        must be an org admin and the job must belong to the caller's org.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetTrainingJobQueueContextResponseV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request GET \

            --url
            https://api.baseten.co/v1/training/jobs/{training_job_id}/queue_context
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/training/jobs/{training_job_id}/queue_context"

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
    training_job_id:
      schema:
        type: string
      name: training_job_id
      in: path
      required: true
  schemas:
    GetTrainingJobQueueContextResponseV1:
      description: >-
        Read-only diagnostic for a training job's PENDING window.

        Returns the (org, gpu_type) capacity pool the job was gated by, jobs
        that

        were holding GPU capacity in that pool when this job was submitted, and

        every status event in [submitted_at, released_at] for those jobs (or up
        to

        "now" if the target is still PENDING).
      properties:
        target_job_id:
          description: Hashid of the target training job
          title: Target Job Id
          type: string
        target_job_name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Target job's name
          title: Target Job Name
        gpu_type:
          description: GPU type the target requested
          title: Gpu Type
          type: string
        requested_gpus:
          description: GPUs the target requested (gpu_count * effective_node_count)
          title: Requested Gpus
          type: integer
        submitted_at:
          description: When the job row was inserted (= API POST time)
          format: date-time
          title: Submitted At
          type: string
        released_at:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          default: null
          description: >-
            When the job's TRAINING_JOB_CREATED status was set, i.e. the moment
            it was released from PENDING. None if still PENDING.
          title: Released At
        pending_seconds:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: released_at - submitted_at in seconds. None if still PENDING.
          title: Pending Seconds
        org_capacity:
          anyOf:
            - $ref: '#/components/schemas/CapacityAtSubmitV1'
            - type: 'null'
          default: null
          description: Org-level cap for (org, gpu_type). None if no cap is configured.
        team_capacity:
          anyOf:
            - $ref: '#/components/schemas/CapacityAtSubmitV1'
            - type: 'null'
          default: null
          description: >-
            Team-level cap for (team, gpu_type). None if no team cap is
            configured.
        active_at_submit:
          description: >-
            Jobs in the same (org, gpu_type) pool that were holding capacity at
            submitted_at
          items:
            $ref: '#/components/schemas/ActiveJobAtSubmitV1'
          title: Active At Submit
          type: array
        pending_ahead_at_submit:
          description: >-
            PENDING jobs in the same (org, gpu_type) pool that were ahead of the
            target in dequeue FIFO order at submitted_at (priority DESC then
            created ASC). These also block the target's release.
          items:
            $ref: '#/components/schemas/PendingJobAheadAtSubmitV1'
          title: Pending Ahead At Submit
          type: array
        events:
          description: >-
            Every status event in [submitted_at, events_window_end] for the
            target job, every job in active_at_submit, and every job in
            pending_ahead_at_submit, oldest first.
          items:
            $ref: '#/components/schemas/QueueEventV1'
          title: Events
          type: array
        events_window_end:
          description: released_at if set, else 'now' (events ongoing)
          format: date-time
          title: Events Window End
          type: string
      required:
        - target_job_id
        - gpu_type
        - requested_gpus
        - submitted_at
        - active_at_submit
        - pending_ahead_at_submit
        - events
        - events_window_end
      title: GetTrainingJobQueueContextResponseV1
      type: object
    CapacityAtSubmitV1:
      description: >-
        A GPU capacity row as it stands now, with ``last_modified`` so callers

        can judge whether the value matches what the dequeue gate saw at submit

        time. Capacity rows are not historicized: edits overwrite in place.
        Compare

        ``last_modified`` against the response's ``submitted_at`` — if it's
        later,

        the value may have changed.
      properties:
        gpu_type:
          description: GPU type identifier (e.g. H100, A100-40GB)
          title: Gpu Type
          type: string
        max_gpus:
          description: Current max concurrent GPUs of this type
          title: Max Gpus
          type: integer
        min_gpus:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Current baseline GPU allocation, if configured
          title: Min Gpus
        last_modified:
          description: When the capacity row was last modified
          format: date-time
          title: Last Modified
          type: string
      required:
        - gpu_type
        - max_gpus
        - last_modified
      title: CapacityAtSubmitV1
      type: object
    ActiveJobAtSubmitV1:
      description: |-
        One other job in the same (org, gpu_type) pool that was holding GPU
        capacity at the moment the target was submitted.
      properties:
        training_job_id:
          description: Hashid of the other training job
          title: Training Job Id
          type: string
        training_job_name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Other job's name
          title: Training Job Name
        instance_type_name:
          description: Instance type of the other job
          title: Instance Type Name
          type: string
        total_gpus:
          description: gpu_count * effective_node_count
          title: Total Gpus
          type: integer
        workload_plane_name:
          description: Workload plane the other job was on
          title: Workload Plane Name
          type: string
        status_at_submit:
          description: Other job's status as of submitted_at (one of ACTIVE_STATES)
          title: Status At Submit
          type: string
        status_set_at:
          description: When that status was set
          format: date-time
          title: Status Set At
          type: string
      required:
        - training_job_id
        - instance_type_name
        - total_gpus
        - workload_plane_name
        - status_at_submit
        - status_set_at
      title: ActiveJobAtSubmitV1
      type: object
    PendingJobAheadAtSubmitV1:
      description: |-
        A PENDING job in the same (org, gpu_type) pool that was ahead of the
        target in dequeue FIFO order at submitted_at — higher priority, or same
        priority and earlier submission.
      properties:
        training_job_id:
          description: Hashid of the other training job
          title: Training Job Id
          type: string
        training_job_name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Other job's name
          title: Training Job Name
        instance_type_name:
          description: Instance type of the other job
          title: Instance Type Name
          type: string
        requested_gpus:
          description: gpu_count * effective_node_count
          title: Requested Gpus
          type: integer
        priority:
          description: Effective priority (NULL coalesced to 0)
          title: Priority
          type: integer
        submitted_at:
          description: The other job's submission time
          format: date-time
          title: Submitted At
          type: string
      required:
        - training_job_id
        - instance_type_name
        - requested_gpus
        - priority
        - submitted_at
      title: PendingJobAheadAtSubmitV1
      type: object
    QueueEventV1:
      description: A single ``TrainingJobStatus`` row inside the queue-context window.
      properties:
        training_job_id:
          description: Hashid of the training job this event is for
          title: Training Job Id
          type: string
        training_job_name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Job name
          title: Training Job Name
        status:
          description: TrainingJobStatus.Name value
          title: Status
          type: string
        created:
          description: When the status row was inserted
          format: date-time
          title: Created
          type: string
        event_message:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Human-readable event message from the status metadata
          title: Event Message
        exit_code:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Exit code from the status metadata, if any
          title: Exit Code
      required:
        - training_job_id
        - status
        - created
      title: QueueEventV1
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
