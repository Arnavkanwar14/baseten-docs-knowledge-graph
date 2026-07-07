---
tags: [baseten, reference, gateway]
source: https://docs.baseten.co/reference/gateway/endpoints/get-an-endpoint
---

> Retrieve a single Frontier Gateway endpoint by its ID.

Retrieve a single endpoint by its `id`, including its slug and configured targets.

### Authentication

  Workspace API key with management scope, passed as `Authorization: Api-Key $BASETEN_API_KEY` (or `Bearer`; both are accepted).

### Path parameters

  Identifier of the endpoint, returned as `id` by [[Create an endpoint]].

### Response

The endpoint, with the same shape as the [[Create an endpoint]] response: `id`, `slug`, `targets`, `created_at`, and `updated_at`.

### Errors

| Status          | Meaning                                                                                       |
| --------------- | --------------------------------------------------------------------------------------------- |
| `403 Forbidden` | The endpoint exists but isn't in your workspace, or the caller doesn't have management scope. |
| `404 Not Found` | No endpoint with this `id` in your workspace.                                                 |

  ```bash curl theme={"system"}
  curl --request GET \
    --url https://api.baseten.co/v1/gateway/endpoints/abc123hash \
    --header "Authorization: Api-Key $BASETEN_API_KEY"
  ```

  ```json 200 theme={"system"}
  {
    "id": "abc123hash",
    "slug": "my-org/glm-5.2",
    "targets": [
      {
        "provider": "BASETEN",
        "model_id": "3kZ9xqd",
        "environment_name": "staging"
      }
    ],
    "created_at": "2026-06-17T12:00:00Z",
    "updated_at": "2026-06-17T12:00:00Z"
  }
  ```

---
Part of [[Gateway (Reference)]]
