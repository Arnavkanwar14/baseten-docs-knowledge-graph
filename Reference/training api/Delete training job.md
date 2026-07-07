---
tags: [baseten, reference, training-api]
source: https://docs.baseten.co/reference/training-api/delete-training-job
---

> Deletes a training job. Stops it first if still running.

## OpenAPI

````yaml delete /v1/training_projects/{training_project_id}/jobs/{training_job_id}
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
  /v1/training_projects/{training_project_id}/jobs/{training_job_id}:
    parameters:
      - $ref: '#/components/parameters/training_project_id'
      - $ref: '#/components/parameters/training_job_id'
    delete:
      summary: Delete a training job.
      description: Deletes a training job. Stops it first if still running.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TrainingJobTombstoneV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request DELETE \

            --url
            https://api.baseten.co/v1/training_projects/{training_project_id}/jobs/{training_job_id}
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/training_projects/{training_project_id}/jobs/{training_job_id}"

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
    TrainingJobTombstoneV1:
      description: A training job tombstone.
      properties:
        id:
          description: Unique identifier of the training job
          title: Id
          type: string
        deleted:
          description: Whether the training job was deleted
          title: Deleted
          type: boolean
        training_project_id:
          description: Unique identifier of the training project
          title: Training Project Id
          type: string
      required:
        - id
        - deleted
        - training_project_id
      title: TrainingJobTombstoneV1
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
