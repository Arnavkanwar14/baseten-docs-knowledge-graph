---
tags: [baseten, reference, gateway]
source: https://docs.baseten.co/reference/gateway/endpoints/delete-an-endpoint
---

> Delete a Frontier Gateway endpoint and stop routing its slug.

Delete an endpoint. The call tears down the endpoint and its targets and stops routing its slug. The slug is freed for reuse: you can `POST /v1/gateway/endpoints` again with the same value to provision a fresh endpoint.

### Authentication

  Workspace API key with management scope, passed as `Authorization: Api-Key $BASETEN_API_KEY` (or `Bearer`; both are accepted).

### Path parameters

  Identifier of the endpoint to delete, returned as `id` by [[Create an endpoint]].

### Response

  Identifier of the deleted endpoint.

  Slug of the deleted endpoint.

### Errors

| Status          | Meaning                                                                                       |
| --------------- | --------------------------------------------------------------------------------------------- |
| `403 Forbidden` | The endpoint exists but isn't in your workspace, or the caller doesn't have management scope. |
| `404 Not Found` | No endpoint with this `id` in your workspace, or it has already been deleted.                 |

  ```bash curl theme={"system"}
  curl --request DELETE \
    --url https://api.baseten.co/v1/gateway/endpoints/abc123hash \
    --header "Authorization: Api-Key $BASETEN_API_KEY"
  ```

  ```json 200 theme={"system"}
  {
    "id": "abc123hash",
    "slug": "my-org/glm-5.2"
  }
  ```

---
Part of [[Gateway (Reference)]]
