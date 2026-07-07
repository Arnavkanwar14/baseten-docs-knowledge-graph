---
tags: [baseten, reference, training-api]
source: https://docs.baseten.co/reference/training-api/overview
---

> Programmatically manage Baseten Training resources.

The Training API manages training projects, jobs, and related resources through a RESTful interface. Use this API to:

* Monitor training job metrics and logs
* Manage training jobs
* Manage checkpoints and artifacts

## Authentication

All Training API requests require authentication with an API key:

```bash theme={"system"}
Authorization: Bearer $BASETEN_API_KEY
```

## Base URL

All Training API endpoints are relative to:

```text theme={"system"}
https://api.baseten.co/v1
```

## Available Endpoints

### Training Projects

| Method   | Endpoint                                                                                                               | Description                        |
| -------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| `GET`    | [[List training projects|`/training_projects`]]                                                  | List all training projects         |
| `GET`    | [[Get training project|`/training_projects/{training_project_id}`]]                             | Get a training project             |
| `POST`   | [[Create training project|`/training_projects`]]                                                | Create a training project          |
| `DELETE` | [[Delete training project|`/training_projects/{training_project_id}`]]                          | Delete a training project          |
| `GET`    | [[Get training project cache summary|`/training_projects/{training_project_id}/cache/summary`]] | Get training project cache summary |

### Training Jobs

The following endpoints use the relative base path: `/training_projects/{training_project_id}/jobs`

| Method   | Endpoint                                                                                              | Description                       |
| -------- | ----------------------------------------------------------------------------------------------------- | --------------------------------- |
| `POST`   | [[Create training job|`.../`]]                                                 | Create a training job             |
| `GET`    | [[List training jobs|`.../`]]                                                  | List all jobs in a project        |
| `GET`    | [[Get training job|`.../{training_job_id}`]]                                   | Get a specific training job       |
| `POST`   | [[Stop training job|`.../{training_job_id}/stop`]]                             | Stop a training job               |
| `DELETE` | [[Delete training job|`.../{training_job_id}`]]                                | Delete a training job             |
| `POST`   | [[Recreate training job|`.../{training_job_id}/recreate`]]                     | Recreate a training job           |
| `GET`    | [[Get training job logs|`.../{training_job_id}/logs`]]                         | Get training job logs             |
| `GET`    | [[Get training job metrics|`.../{training_job_id}/metrics`]]                   | Get training job metrics          |
| `GET`    | [[List training job checkpoints|`.../{training_job_id}/checkpoints`]]           | List job checkpoints              |
| `GET`    | [[Get training job checkpoint files|`.../{training_job_id}/checkpoint_files`]] | Get training job checkpoint files |
| `GET`    | [[Download training job source code|`.../{training_job_id}/download`]]                     | Download training job artifacts   |
| `GET`    | [[Get auth codes for training job|`.../{training_job_id}/auth_codes`]]         | Get auth codes for a training job |

Search endpoint:

| Method | Endpoint                                                                | Description                     |
| ------ | ----------------------------------------------------------------------- | ------------------------------- |
| `POST` | [[Search training jobs|`/training_jobs/search`]] | Search across all training jobs |

---
Part of [[Training Api (Reference)]]
