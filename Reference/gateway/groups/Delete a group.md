---
tags: [baseten, reference, gateway]
source: https://docs.baseten.co/reference/gateway/groups/delete-a-group
---

> Delete a Frontier Gateway group, recursively remove its descendants, and revoke every key in the subtree.

Delete a group. The call removes the group, revokes every API key in the group, and recursively removes every descendant group and their keys. The group's `external_entity_id` is freed for reuse: you can `POST /v1/gateway/groups` again with the same value to provision a fresh group.

To revoke a single key without churning the whole group, use [[Revoke an API key]] instead.

### Authentication

  Workspace API key with management scope, passed as `Authorization: Api-Key $BASETEN_API_KEY` (or `Bearer`; both are accepted).

### Path parameters

  Internal Baseten ID of the group to delete.

### Response

  Internal ID of the deleted group.

  Group identity at the time of deletion. Same shape as on [[Create a group]].

  RFC 3339 UTC timestamp of deletion.

Descendant groups are soft-deleted in the same transaction but aren't included in the response body. Their keys are revoked and their model attachments are removed.

### Errors

| Status          | Meaning                                                                                    |
| --------------- | ------------------------------------------------------------------------------------------ |
| `403 Forbidden` | The group exists but isn't in your workspace, or the caller doesn't have management scope. |
| `404 Not Found` | No group with this `id` in your workspace, or it has already been deleted.                 |

  ```bash curl theme={"system"}
  curl --request DELETE \
    --url https://api.baseten.co/v1/gateway/groups/abc123hash \
    --header "Authorization: Api-Key $BASETEN_API_KEY"
  ```

  ```json 200 theme={"system"}
  {
    "id": "abc123hash",
    "metadata": {
      "name": "Acme prod",
      "external_entity_id": "cust_42"
    },
    "deleted_at": "2026-05-13T12:34:56Z"
  }
  ```

---
Part of [[Gateway (Reference)]]
