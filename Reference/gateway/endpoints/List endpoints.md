---
tags: [baseten, reference, gateway]
source: https://docs.baseten.co/reference/gateway/endpoints/list-endpoints
---

> List every Frontier Gateway endpoint in your workspace.

List the endpoints in your workspace, each with its slug and configured targets. The response is paginated.

### Authentication

  Workspace API key with management scope, passed as `Authorization: Api-Key $BASETEN_API_KEY` (or `Bearer`; both are accepted).

### Query parameters

  Page size. Default 100, maximum 1000.

  Opaque cursor for the next page, taken from `pagination.cursor` of a previous response. Omit it for the first page.

### Response

  The endpoints in this page. Each entry has the same shape as the [[Create an endpoint]] response: `id`, `slug`, `targets`, `created_at`, and `updated_at`.

  Pagination metadata.

  * **`has_more`** (`boolean`): Whether more endpoints are available beyond this page.
  * **`cursor`** (`string`): Cursor to pass as `cursor` to fetch the next page, or `null` on the last page.

### Errors

| Status          | Meaning                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------- |
| `403 Forbidden` | Workspace isn't onboarded to Frontier Gateway, or the caller doesn't have management scope. |

  ```bash curl theme={"system"}
  curl --request GET \
    --url https://api.baseten.co/v1/gateway/endpoints \
    --header "Authorization: Api-Key $BASETEN_API_KEY"
  ```

  ```bash next page theme={"system"}
  curl --request GET \
    --url "https://api.baseten.co/v1/gateway/endpoints?cursor=aVd2Yk54T2d2V0dFWE13R1l4R2k5UVE=" \
    --header "Authorization: Api-Key $BASETEN_API_KEY"
  ```

  ```json 200 theme={"system"}
  {
    "items": [
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
    ],
    "pagination": {
      "has_more": true,
      "cursor": "aVd2Yk54T2d2V0dFWE13R1l4R2k5UVE="
    }
  }
  ```

---
Part of [[Gateway (Reference)]]
