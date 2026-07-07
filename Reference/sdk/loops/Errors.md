---
tags: [baseten, reference, sdk]
source: https://docs.baseten.co/reference/sdk/loops/errors
---

> The Loops SDK exception types and when each is raised.

Exceptions raised by the [[ServiceClient]], [[TrainingClient]], and [[SamplingClient]] when a server operation fails.

  The server reports that an async operation failed. The `error_class` attribute carries the server-side exception class name (for example, `"ValueError"` or `"DispatcherError"`), which is useful for routing in caller code.

  The server returned 404 for an operation ID. This can mean the server has no record of the operation (after a pod restart, for example) or that the result was TTL-evicted. Resubmit the operation if the work is still needed; the server's idempotency-key deduplication prevents double-execution.

  The server is shutting down (503 response). Retry the request against a different replica.

---
Part of [[Sdk (Reference)]]
