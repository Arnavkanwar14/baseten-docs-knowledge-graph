---
tags: [baseten, reference, gateway]
source: https://docs.baseten.co/reference/gateway/api-keys/revoke-an-api-key
---

> Revoke a federated API key by its prefix. Other keys under the same group are unaffected.

Revoke a single federated API key by its `prefix`. Other keys under the same group are unaffected. Revocation is irreversible: the key can't authenticate any further request and can't be restored. To restore access for the same downstream customer, mint a new key under the same group with [[Create an API key]].

### Authentication

  Workspace API key with management scope, passed as `Authorization: Api-Key $BASETEN_API_KEY` (or `Bearer`; both are accepted).

### Path parameters

  Internal Baseten ID of the owning group.

  The key's prefix.

### Response

  The prefix of the revoked key.

### Errors

| Status          | Meaning                                                                                           |
| --------------- | ------------------------------------------------------------------------------------------------- |
| `403 Forbidden` | The group or key exists but isn't in your workspace, or the caller doesn't have management scope. |
| `404 Not Found` | No group or key with these identifiers in your workspace, or the key has already been revoked.    |

  ```bash curl theme={"system"}
  curl --request DELETE \
    --url https://api.baseten.co/v1/gateway/groups/abc123hash/api_keys/sky_sCqhBwEy4kPd \
    --header "Authorization: Api-Key $BASETEN_API_KEY"
  ```

  ```json 200 theme={"system"}
  {
    "prefix": "sky_sCqhBwEy4kPd"
  }
  ```

---
Part of [[Gateway (Reference)]]
