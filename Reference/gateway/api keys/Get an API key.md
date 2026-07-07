---
tags: [baseten, reference, gateway]
source: https://docs.baseten.co/reference/gateway/api-keys/get-an-api-key
---

> Fetch metadata for one federated API key by its prefix. The plaintext key is never returned after creation.

Fetch one federated API key by its `prefix`. Only metadata is returned; the plaintext key is shown exactly once at creation and is unrecoverable afterward. To inspect the model access and limits the key resolves to, fetch its [[Get a group|group]] and read the `effective_models` block.

### Authentication

  Workspace API key with management scope, passed as `Authorization: Api-Key $BASETEN_API_KEY` (or `Bearer`; both are accepted).

### Path parameters

  Internal Baseten ID of the owning group.

  The key's prefix (the substring before the `.` in the full key string). Returned as `prefix` from [[Create an API key]] and from [[List API keys for a group]].

### Response

  The key's prefix.

  Display name set when the key was minted. `null` if no name was provided.

### Errors

| Status          | Meaning                                                                                           |
| --------------- | ------------------------------------------------------------------------------------------------- |
| `403 Forbidden` | The group or key exists but isn't in your workspace, or the caller doesn't have management scope. |
| `404 Not Found` | No group or key with these identifiers in your workspace, or the key has been revoked.            |

  ```bash curl theme={"system"}
  curl --request GET \
    --url https://api.baseten.co/v1/gateway/groups/abc123hash/api_keys/sky_sCqhBwEy4kPd \
    --header "Authorization: Api-Key $BASETEN_API_KEY"
  ```

  ```json 200 theme={"system"}
  {
    "prefix": "sky_sCqhBwEy4kPd",
    "name": "prod-key-1"
  }
  ```

---
Part of [[Gateway (Reference)]]
