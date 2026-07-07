---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/overview
---

> Manage models and deployments with the Baseten management API. It supports monitoring, CI/CD, and automation at both the model and workspace levels.

The full OpenAPI spec is available at [api.baseten.co/v1/spec](https://api.baseten.co/v1/spec) for generating API clients.

Management API requests are rate limited per API key. See [[Rate limits]] for the per-endpoint limits and how to handle `429` responses.

To deploy a model archive programmatically, see [[Create a model with the REST API]].

## Model endpoints

| Method | Endpoint                                                                            | Description                  |
| :----- | :---------------------------------------------------------------------------------- | :--------------------------- |
| `GET`  | [[All models|`/v1/models`]]                    | Get all models               |
| `GET`  | [[By ID (Models)|`/v1/models/{model_id}`]]      | Get models by ID             |
| `POST` | [[Prepare a model upload|`/v1/prepare_model_upload`]] | Prepare a model upload       |
| `POST` | [[Create a model from a source|`/v1/models`]]      | Create a model from a source |
| `DEL`  | [[Delete models|`/v1/models/{model_id}`]]   | Delete models                |

## Chain endpoints

| Method | Endpoint                                                                          | Description       |
| :----- | :-------------------------------------------------------------------------------- | :---------------- |
| `GET`  | [[All chains|`/v1/chains`]]                  | Get all Chains    |
| `GET`  | [[By ID|`/v1/chains/{chain_id}`]]    | Get a Chain by ID |
| `DEL`  | [[Delete chains|`/v1/chains/{chain_id}`]] | Delete Chains     |

## Deployment endpoints

  
    ### Activate a model deployment

    | Method | Endpoint                                                                                                                                                         | Description                 |
    | :----- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
    | `POST` | [[Activate environment deployment|`/v1/models/{model_id}/environments/{env_name}/activate`]] | **Activate** an environment |
    | `POST` | [[Development deployment|`/v1/models/{model_id}/deployments/development/activate`]]                    | **Activate** development    |
    | `POST` | [[Any deployment by ID|`/v1/models/{model_id}/deployments/{deployment_id}/activate`]]                            | **Activate** a deployment   |
    | `POST` | [[Activate production deployment|`/v1/models/{model_id}/deployments/production/activate`]]                        | **Activate** production     |

    ### Deactivate a model deployment

    | Method | Endpoint                                                                                                                                                               | Description                   |
    | :----- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------- |
    | `POST` | [[Deactivate environment deployment|`/v1/models/{model_id}/environments/{env_name}/deactivate`]] | **Deactivate** an environment |
    | `POST` | [[Development deployment (Deactivate)|`/v1/models/{model_id}/deployments/development/deactivate`]]                    | **Deactivate** development    |
    | `POST` | [[Any deployment by ID (Deactivate)|`/v1/models/{model_id}/deployments/{deployment_id}/deactivate`]]                            | **Deactivate** a deployment   |
    | `POST` | [[Deactivate production deployment|`/v1/models/{model_id}/deployments/production/deactivate`]]                        | **Deactivate** production     |

    ### Retry a model deployment

    | Method | Endpoint                                                                                                                              | Description            |
    | :----- | :------------------------------------------------------------------------------------------------------------------------------------ | :--------------------- |
    | `POST` | [[Development deployment (Retry)|`/v1/models/{model_id}/deployments/development/retry`]] | **Retry** development  |
    | `POST` | [[Any deployment by ID (Retry)|`/v1/models/{model_id}/deployments/{deployment_id}/retry`]]         | **Retry** a deployment |
    | `POST` | [[Production deployment|`/v1/models/{model_id}/deployments/production/retry`]]     | **Retry** production   |

    ### Promote a model deployment

    | Method | Endpoint                                                                                                                                                   | Description                              |
    | :----- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------- |
    | `POST` | [[Promote to model environment|`/v1/models/{model_id}/environments/{env_name}/promote`]]           | **Promote** to model **environment**     |
    | `POST` | [[Cancel model promotion|`/v1/models/{model_id}/environments/{env_name}/cancel_promotion`]]                         | **Cancel** a promotion to an environment |
    | `POST` | [[Development model deployment (Promote)|`/v1/models/{model_id}/deployments/development/promote`]]   | **Promote** development deployment       |
    | `POST` | [[Any model deployment by ID (Promote)|`/v1/models/{model_id}/deployments/{deployment_id}/promote`]]           | **Promote** any deployment               |
    | `POST` | [[Pause rolling deployment|`/v1/models/{model_id}/environments/{env_name}/pause_promotion`]]                           | **Pause** rolling deployment             |
    | `POST` | [[Resume rolling deployment|`/v1/models/{model_id}/environments/{env_name}/resume_promotion`]]                         | **Resume** rolling deployment            |
    | `POST` | [[Force cancel rolling deployment|`/v1/models/{model_id}/environments/{env_name}/force_cancel_promotion`]]             | **Force cancel** rolling deployment      |
    | `POST` | [[Force roll forward promotion|`/v1/models/{model_id}/environments/{env_name}/force_roll_forward_promotion`]] | **Force roll forward** promotion         |

    ### Autoscaling

    | Method  | Endpoint                                                                                                                                                       | Description                                     |
    | :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------- |
    | `PATCH` | [[Development model deployment|`.../deployments/development/autoscaling_settings`]] | Updates **development's autoscaling** settings  |
    | `PATCH` | [[Any model deployment by ID|`.../deployments/{deployment_id}/autoscaling_settings`]]         | Updates a **deployment's autoscaling** settings |
    | `PATCH` | [[Update production deployment autoscaling settings|`.../deployments/production/autoscaling_settings`]]      | Updates **production's autoscaling** settings   |

    ### Manage deployment endpoints

    | Method | Endpoint                                                                                                                                         | Description                       |
    | :----- | :----------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------- |
    | `POST` | [[Add a deployment to a model|`/v1/models/{model_id}/deployments`]]                                        | Add a deployment to a model       |
    | `GET`  | [[Get all model deployments|`/v1/models/{model_id}/deployments`]]                                     | Get all model deployments         |
    | `GET`  | [[Production model deployment|`/v1/models/{model_id}/deployments/production`]]                      | Production model deployment       |
    | `GET`  | [[Development model deployment (Deployments)|`/v1/models/{model_id}/deployments/development`]]                    | Development model deployment      |
    | `GET`  | [[Any model deployment by ID (Deployments)|`/v1/models/{model_id}/deployments/{deployment_id}`]]                      | Any model deployment by ID        |
    | `GET`  | [[Get model deployment logs|`/v1/models/{model_id}/deployments/{deployment_id}/logs`]]                            | Get model deployment logs         |
    | `GET`  | [[Get model deployment metrics|`/v1/models/{model_id}/deployments/{deployment_id}/metrics`]]                      | Get model deployment metrics      |
    | `GET`  | [[Get model deployment config|`/v1/models/{model_id}/deployments/{deployment_id}/config`]]                        | Get model deployment config       |
    | `GET`  | [[Get model deployment download URL|`/v1/models/{model_id}/deployments/{deployment_id}/download`]]                | Get model deployment download URL |
    | `DEL`  | [[Delete model deployments|`/v1/models/{model_id}/deployments/{deployment_id}`]]                   | Delete model deployments          |
    | `DEL`  | [[Terminate deployment replica|`/v1/models/{model_id}/deployments/{deployment_id}/replicas/{replica_id}`]] | Terminate deployment replica      |
  

  
    ### Deactivate a Chain deployment

    | Method | Endpoint                                                                                                                                                | Description                       |
    | :----- | :------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------- |
    | `POST` | [[Chain deployment|`/v1/chains/{chain_id}/deployments/{chain_deployment_id}/deactivate`]] | **Deactivate** a Chain deployment |

    ### Promote a Chain deployment

    | Method | Endpoint                                                                                                                                               | Description                  |
    | :----- | :----------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------- |
    | `POST` | [[Promote to chain environment|`/v1/chains/{chain_id}/environments/{env_name}/promote`]] | Promote to chain environment |

    ### Autoscaling

    | Method  | Endpoint                                                                                                                                              | Description                                            |
    | :------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------- |
    | `PATCH` | [[Update chainlet environment's autoscaling settings|`.../chainlet_settings/autoscaling_settings`]] | **Update chainlet** environment's autoscaling settings |

    ### Manage Chain deployments

    | Method | Endpoint                                                                                                                            | Description                  |
    | :----- | :---------------------------------------------------------------------------------------------------------------------------------- | :--------------------------- |
    | `GET`  | [[Get all chain deployments|`/v1/chains/{chain_id}/deployments`]]                             | Get all chain deployments    |
    | `GET`  | [[Any chain deployment by ID|`/v1/chains/{chain_id}/deployments/{chain_deployment_id}`]]    | Any chain deployment by ID   |
    | `DEL`  | [[Delete chain deployment|`/v1/chains/{chain_id}/deployments/{chain_deployment_id}`]] | **Delete** chain deployments |
  

## Environment endpoints

  
    | Method  | Endpoint                                                                                                                  | Description                |
    | :------ | :------------------------------------------------------------------------------------------------------------------------ | :------------------------- |
    | `POST`  | [[Create environment|`/v1/models/{model_id}/environments`]]                      | Create environment         |
    | `GET`   | [[Get all environments|`/v1/models/{model_id}/environments`]]                       | Get all environments       |
    | `GET`   | [[Get environment|`/v1/models/{model_id}/environments/{env_name}`]]     | Get an environment details |
    | `PATCH` | [[Update model environment|`/v1/models/{model_id}/environments/{env_name}`]] | Update model environment   |
  

  
    | Method  | Endpoint                                                                                                                                                                                | Description                                 |
    | :------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------ |
    | `POST`  | [[Create Chain environment|`/v1/chains/{chain_id}/environments`]]                                                                               | Create chain environment                    |
    | `GET`   | [[Get all Chain environments|`/v1/chains/{chain_id}/environments`]]                                                                               | Get all chain environments                  |
    | `GET`   | [[Get Chain environment|`/v1/chains/{chain_id}/environments/{env_name}`]]                                                              | Get a chain environment                     |
    | `PATCH` | [[Update Chain environment|`/v1/chains/{chain_id}/environments/{env_name}`]]                                                          | Update chain environment                    |
    | `POST`  | [[Update chainlet environment's instance type|`/v1/chains/{chain_id}/environments/{env_name}/chainlet_settings/instance_types/update`]] | Update chainlet environment's instance type |
  

## Instance type endpoints

| Method | Endpoint                                                                                         | Description              |
| :----- | :----------------------------------------------------------------------------------------------- | :----------------------- |
| `GET`  | [[All instance types|`/v1/instance_types`]]         | Get all instance types   |
| `GET`  | [[Instance type prices|`/v1/instance_type_prices`]] | Get instance type prices |

## Model API endpoints

| Method | Endpoint                                                                                           | Description             |
| :----- | :------------------------------------------------------------------------------------------------- | :---------------------- |
| `GET`  | [[All Model APIs|`/v1/model_apis`]]                       | List Model APIs         |
| `GET`  | [[By name|`/v1/model_apis/{model_api_name}`]] | Get a Model API by name |

## Team endpoints

| Method | Endpoint                                                       | Description   |
| :----- | :------------------------------------------------------------- | :------------ |
| `GET`  | [[List all teams|`/v1/teams`]] | Get all teams |

## Secret endpoints

| Method | Endpoint                                                                               | Description                    |
| :----- | :------------------------------------------------------------------------------------- | :----------------------------- |
| `GET`  | [[Get all secrets|`/v1/secrets`]]                    | Get all secrets                |
| `POST` | [[Upsert a secret|`/v1/secrets`]]                    | Create or update a secret      |
| `GET`  | [[Get all team secrets|`/v1/teams/{team_id}/secrets`]] | Get all team secrets           |
| `POST` | [[Upsert a team secret|`/v1/teams/{team_id}/secrets`]] | Create or update a team secret |

## API Key endpoints

| Method   | Endpoint                                                                                 | Description           |
| :------- | :--------------------------------------------------------------------------------------- | :-------------------- |
| `GET`    | [[Get all API keys|`/v1/api_keys`]]            | Get all API keys      |
| `POST`   | [[Create an API key (Api Keys)|`/v1/api_keys`]]                  | Create an API key     |
| `DELETE` | [[Delete an API key|`/v1/api_keys/{api_key_prefix}`]]  | Delete an API key     |
| `POST`   | [[Create a team API key|`/v1/teams/{team_id}/api_keys`]] | Create a team API key |

## Billing endpoints

| Method | Endpoint                                                                                                     | Description               |
| :----- | :----------------------------------------------------------------------------------------------------------- | :------------------------ |
| `GET`  | [[Get billing usage summary|`/v1/billing/usage_summary`]] | Get billing usage summary |

## Training endpoints

For a complete reference and request schemas, see the [[Overview (Training Api)|Training API overview]].

### Training projects

| Method   | Endpoint                                                                                                                  | Description                        |
| :------- | :------------------------------------------------------------------------------------------------------------------------ | :--------------------------------- |
| `GET`    | [[List training projects|`/v1/training_projects`]]                                                  | List all training projects         |
| `POST`   | [[Create training project|`/v1/training_projects`]]                                                | Create a training project          |
| `GET`    | [[Get training project|`/v1/training_projects/{training_project_id}`]]                             | Get a training project             |
| `DELETE` | [[Delete training project|`/v1/training_projects/{training_project_id}`]]                          | Delete a training project          |
| `POST`   | [[Create a team training project|`/v1/teams/{team_id}/training_projects`]]                | Create a team training project     |
| `GET`    | [[Get training project cache summary|`/v1/training_projects/{training_project_id}/cache/summary`]] | Get training project cache summary |

### Training jobs

| Method   | Endpoint                                                                                                                                           | Description                       |
| :------- | :------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------- |
| `POST`   | [[Create training job|`/v1/training_projects/{training_project_id}/jobs`]]                                                  | Create a training job             |
| `GET`    | [[List training jobs|`/v1/training_projects/{training_project_id}/jobs`]]                                                   | List all jobs in a project        |
| `GET`    | [[Get training job|`/v1/training_projects/{training_project_id}/jobs/{training_job_id}`]]                                   | Get a training job by ID          |
| `DELETE` | [[Delete training job|`/v1/training_projects/{training_project_id}/jobs/{training_job_id}`]]                                | Delete a training job             |
| `POST`   | [[Stop training job|`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/stop`]]                             | Stop a training job               |
| `POST`   | [[Recreate training job|`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/recreate`]]                     | Recreate a training job           |
| `GET`    | [[Get training job logs|`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/logs`]]                         | Get training job logs             |
| `GET`    | [[Get training job metrics|`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/metrics`]]                   | Get training job metrics          |
| `GET`    | [[List training job checkpoints|`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoints`]]           | List job checkpoints              |
| `GET`    | [[Get training job checkpoint files|`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoint_files`]] | Get checkpoint files              |
| `GET`    | [[Download training job source code|`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/download`]]                     | Download training job artifacts   |
| `GET`    | [[Get auth codes for training job|`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/auth_codes`]]         | Get auth codes for a training job |
| `POST`   | [[Search training jobs|`/v1/training_jobs/search`]]                                                                         | Search across all training jobs   |

## Frontier Gateway endpoints

For the conceptual guide and end-to-end examples, see the [[Baseten Frontier Gateway|Frontier Gateway overview]].

### Endpoints

| Method   | Endpoint                                                                                       | Description        |
| :------- | :--------------------------------------------------------------------------------------------- | :----------------- |
| `POST`   | [[Create an endpoint|`/v1/gateway/endpoints`]]                     | Create an endpoint |
| `GET`    | [[List endpoints|`/v1/gateway/endpoints`]]                         | List endpoints     |
| `GET`    | [[Get an endpoint|`/v1/gateway/endpoints/{endpoint_id}`]]          | Get an endpoint    |
| `PATCH`  | [[Update an endpoint|`/v1/gateway/endpoints/{endpoint_id}`]] | Update an endpoint |
| `DELETE` | [[Delete an endpoint|`/v1/gateway/endpoints/{endpoint_id}`]]       | Delete an endpoint |

### Groups

| Method   | Endpoint                                                                    | Description    |
| :------- | :-------------------------------------------------------------------------- | :------------- |
| `POST`   | [[Create a group|`/v1/gateway/groups`]]            | Create a group |
| `GET`    | [[List groups|`/v1/gateway/groups`]]               | List groups    |
| `GET`    | [[Get a group|`/v1/gateway/groups/{group_id}`]]    | Get a group    |
| `PATCH`  | [[Update a group|`/v1/gateway/groups/{group_id}`]] | Update a group |
| `DELETE` | [[Delete a group|`/v1/gateway/groups/{group_id}`]] | Delete a group |

### API keys

| Method   | Endpoint                                                                                                   | Description               |
| :------- | :--------------------------------------------------------------------------------------------------------- | :------------------------ |
| `POST`   | [[Create an API key|`/v1/gateway/groups/{group_id}/api_keys`]]                  | Create an API key         |
| `GET`    | [[List API keys for a group|`/v1/gateway/groups/{group_id}/api_keys`]]          | List API keys for a group |
| `GET`    | [[Get an API key|`/v1/gateway/groups/{group_id}/api_keys/{api_key_prefix}`]]    | Get an API key            |
| `DELETE` | [[Revoke an API key|`/v1/gateway/groups/{group_id}/api_keys/{api_key_prefix}`]] | Revoke an API key         |

---
Part of [[Management Api (Reference)]]
