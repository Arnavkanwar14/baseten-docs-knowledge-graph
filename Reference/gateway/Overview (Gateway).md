---
tags: [baseten, reference, gateway]
source: https://docs.baseten.co/reference/gateway/overview
---

> Manage Frontier Gateway endpoints, groups, and federated API keys through the Baseten REST API.

The Frontier Gateway API manages the resources behind your branded inference gateway: the **endpoints** that route slugs to deployments, the **groups** that model your customers and their limits, and the **federated API keys** your customers call with. For the conceptual guide and end-to-end examples, see the [[Baseten Frontier Gateway|Frontier Gateway overview]].

These endpoints live under `/v1/gateway/` and are gated to Frontier Gateway workspaces. Authenticate with a workspace API key with management scope, passed as `Authorization: Api-Key $BASETEN_API_KEY`. Requests from workspaces that aren't onboarded return `403`. The full OpenAPI spec is available at [api.baseten.co/v1/spec](https://api.baseten.co/v1/spec) for generating API clients.

## Endpoints

An endpoint maps a routing slug to the deployment that serves it. Use these routes to create, inspect, re-point, and delete endpoints.

| Method   | Endpoint                                                                                       | Description        |
| :------- | :--------------------------------------------------------------------------------------------- | :----------------- |
| `POST`   | [[Create an endpoint|`/v1/gateway/endpoints`]]                     | Create an endpoint |
| `GET`    | [[List endpoints|`/v1/gateway/endpoints`]]                         | List endpoints     |
| `GET`    | [[Get an endpoint|`/v1/gateway/endpoints/{endpoint_id}`]]          | Get an endpoint    |
| `PATCH`  | [[Update an endpoint|`/v1/gateway/endpoints/{endpoint_id}`]] | Update an endpoint |
| `DELETE` | [[Delete an endpoint|`/v1/gateway/endpoints/{endpoint_id}`]]       | Delete an endpoint |

## Groups

A group owns the model set, rate and usage limits, and place in the hierarchy that its keys inherit. Use these routes to manage groups and inspect their usage.

| Method   | Endpoint                                                                           | Description     |
| :------- | :--------------------------------------------------------------------------------- | :-------------- |
| `POST`   | [[Create a group|`/v1/gateway/groups`]]                   | Create a group  |
| `GET`    | [[List groups|`/v1/gateway/groups`]]                      | List groups     |
| `GET`    | [[Get a group|`/v1/gateway/groups/{group_id}`]]           | Get a group     |
| `GET`    | [[Get group usage|`/v1/gateway/groups/{group_id}/usage`]] | Get group usage |
| `PATCH`  | [[Update a group|`/v1/gateway/groups/{group_id}`]]        | Update a group  |
| `DELETE` | [[Delete a group|`/v1/gateway/groups/{group_id}`]]        | Delete a group  |

## API keys

A federated API key is the credential your customers call with, bound to one group whose limits it inherits. Use these routes to mint, list, and revoke keys.

| Method   | Endpoint                                                                                                   | Description               |
| :------- | :--------------------------------------------------------------------------------------------------------- | :------------------------ |
| `POST`   | [[Create an API key|`/v1/gateway/groups/{group_id}/api_keys`]]                  | Create an API key         |
| `POST`   | [[Register an API key|`/v1/gateway/groups/{group_id}/api_keys/register`]]       | Register an API key       |
| `GET`    | [[List API keys for a group|`/v1/gateway/groups/{group_id}/api_keys`]]          | List API keys for a group |
| `GET`    | [[Get an API key|`/v1/gateway/groups/{group_id}/api_keys/{api_key_prefix}`]]    | Get an API key            |
| `DELETE` | [[Revoke an API key|`/v1/gateway/groups/{group_id}/api_keys/{api_key_prefix}`]] | Revoke an API key         |

## Billing webhooks

Frontier Gateway emits a signed per-request usage event to your webhook endpoint for every call. For the payload shape and signature verification, see [[Billing webhooks (Gateway)|Billing webhooks]].

---
Part of [[Gateway (Reference)]]
