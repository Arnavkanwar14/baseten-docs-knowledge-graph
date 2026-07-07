---
tags: [baseten, reference, gateway]
source: https://docs.baseten.co/reference/gateway/api-keys/create-an-api-key
---

> Mint a federated API key under a Frontier Gateway group. The plaintext key is returned exactly once.

Mint a new federated API key under an existing group. The key inherits the group's effective model set and limits; the request body does not configure either on the key. The plaintext key is returned exactly once in the response and is unrecoverable afterward.

### Authentication

  Workspace API key with management scope, passed as `Authorization: Api-Key $BASETEN_API_KEY` (or `Bearer`; both are accepted).

### Path parameters

  Internal Baseten ID of the group to mint the key under. Returned as `id` from [[Create a group]].

### Body

  Display name for the key. Useful for distinguishing multiple keys under the same group.

### Response

  The plaintext key, formatted `prefix.secret`. Returned exactly once. Hand this to the downstream consumer immediately and store it securely on their side. Baseten does not store the secret portion and cannot show it again.

  The substring before the `.` in `api_key`. Use the prefix (not the full key) as the path parameter in every per-key URL.

  Echoes the request `name`. `null` if no name was provided.

### Errors

| Status          | Meaning                                                                                    |
| --------------- | ------------------------------------------------------------------------------------------ |
| `403 Forbidden` | The group exists but isn't in your workspace, or the caller doesn't have management scope. |
| `404 Not Found` | No group with this `id` in your workspace, or it has been deleted.                         |

  ```bash curl theme={"system"}
  curl --request POST \
    --url https://api.baseten.co/v1/gateway/groups/abc123hash/api_keys \
    --header "Authorization: Api-Key $BASETEN_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "name": "prod-key-1"
    }'
  ```

  ```json 200 theme={"system"}
  {
    "api_key": "sky_sCqhBwEy4kPd.<api-key-secret>",
    "prefix": "sky_sCqhBwEy4kPd",
    "name": "prod-key-1"
  }
  ```

---
Part of [[Gateway (Reference)]]
