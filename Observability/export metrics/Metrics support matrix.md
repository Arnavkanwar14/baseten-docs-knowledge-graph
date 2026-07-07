---
tags: [baseten, observability, export-metrics]
source: https://docs.baseten.co/observability/export-metrics/supported-metrics
---

> Every metric you can export from Baseten, with its type and labels

This page lists every metric the Baseten [[Overview (Export Metrics)|metrics export endpoint]] exposes, with each metric's name, type, and labels.

Baseten serves these metrics in Prometheus format at `https://app.baseten.co/metrics`. For the endpoint URL, authentication, scrape interval, and supported integrations (Prometheus, Datadog, Grafana, New Relic), see the [[Overview (Export Metrics)|export overview]].

## How to read this page

Each metric is listed by its Prometheus name, with:

* **Type:** `counter` (a cumulative total that only increases), `gauge` (a point-in-time value), or `histogram` (a distribution you can compute percentiles from).
* **Labels:** the dimensions you can filter and group by. Common labels are `model_id`, `model_name`, and `deployment_id`; `environment` and `rollout_phase` appear only for deployments tied to an [[Deployments|environment]]. Some metrics, such as the engine metrics, use a smaller label set.

These are the same measurements shown in the dashboard [[Metrics|Metrics tab]], exposed here for export. The two sets overlap but aren't identical: a few values are graphed in the dashboard without being exportable, and some exported metrics aren't graphed.

## Availability

Some metrics are emitted only for certain deployments:

* **BIS-LLM metrics** (`baseten_llm_*`) appear for each [[Overview (Bis Llm)|BIS-LLM]] deployment. See [BIS-LLM metrics](#bis-llm-metrics).
* **vLLM and SGLang metrics** appear when Baseten detects that engine on your deployment. See [[Metrics|vLLM and SGLang metrics]].
* **Pod health metrics** (`baseten_container_restarts_total` and `baseten_pod_readiness`) roll out behind a feature flag. Contact your account team if they aren't yet visible for your organization.

***

## `baseten_inference_requests_total`

Cumulative number of requests to the model.

Type: `counter`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  The status code of the response.

  Whether the request was an [[Async inference|async inference request]].

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_end_to_end_response_time_seconds`

End-to-end response time in seconds.

Type: `histogram`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  The status code of the response.

  Whether the request was an [[Async inference|async inference request]].

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_container_cpu_usage_seconds_total`

Cumulative CPU time consumed by the container in core-seconds.

Type: `counter`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  The ID of the replica.

  The environment that the deployment corresponds to. Empty if the deployment is
  not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_replicas_active`

Number of replicas ready to serve model requests.

Type: `gauge`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  The environment that the deployment corresponds to. Empty if the deployment is
  not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_replicas_starting`

Number of replicas starting up--that is, either waiting for resources to be available or loading the model.

Type: `gauge`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  The environment that the deployment corresponds to. Empty if the deployment is
  not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_container_restarts_total`

Cumulative number of times the model container has been restarted. Restarts are typically caused by application crashes, out-of-memory kills, or failed liveness probes. See [[Health checks|custom health checks]] for how liveness affects restart behavior.

Type: `counter`

> **Note:**
  This metric rolls out behind a feature flag. Contact your account team if it's not yet visible for your organization.

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_pod_readiness`

Number of pods grouped by their Kubernetes Ready condition. A pod with `condition="true"` is serving traffic; `condition="false"` means the pod is starting up, failing its readiness probe, or shutting down.

Type: `gauge`

> **Note:**
  This metric rolls out behind a feature flag. Contact your account team if it's not yet visible for your organization.

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  The Kubernetes Ready condition for the pods in this sample.

  Possible values:

  * `"true"`: Pods are ready and serving traffic.
  * `"false"`: Pods are starting up, failing readiness probes, or shutting down.
  * `"unknown"`: The Ready condition can't be determined (for example, the kubelet hasn't reported recently).

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_container_cpu_memory_working_set_bytes`

Working set memory usage of the container in bytes.

Type: `gauge`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  The ID of the replica.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_request_size_bytes`

Request size in bytes. Proxy for input tokens.

Type: `histogram`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  The status code of the response.

  Whether the request was an [[Async inference|async inference request]].

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_response_size_bytes`

Response size in bytes. Proxy for generated tokens.

Type: `histogram`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  The status code of the response.

  Whether the request was an [[Async inference|async inference request]].

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_time_to_first_byte_seconds`

Time to first byte/write in seconds. Proxy for time-to-first-token (TTFT).

Type: `histogram`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  The status code of the response.

  Whether the request was an [[Async inference|async inference request]].

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_time_in_async_queue_seconds`

Time async requests spend queued before processing.

Type: `histogram`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_async_queue_size`

Number of queued async requests over time.

Type: `gauge`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_async_webhook_requests_total`

Cumulative number of [[Async inference|async inference]] webhook delivery requests sent.

Type: `counter`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_async_webhook_latency_seconds`

Latency of [[Async inference|async inference]] webhook delivery requests in seconds.

Type: `histogram`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_gpu_memory_used`

GPU memory used in MiB.

Type: `gauge`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  The ID of the replica.

  The ID of the GPU.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_gpu_utilization`

GPU utilization as a percentage (between 0 and 100).

Type: `gauge`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  The ID of the replica.

  The ID of the GPU.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_ongoing_websocket_connections`

Number of ongoing websocket connections.

Type: `gauge`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_concurrent_requests`

Total in-flight inference requests for a deployment, including both requests currently being serviced by replicas and requests waiting to be processed. [[Async inference|Async inference requests]] are not included in this metric. This is the primary signal that drives [[Autoscaling|autoscaling]] decisions.

Type: `gauge`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## BIS-LLM metrics

[[Overview (Bis Llm)|BIS-LLM]] deployments export engine-level and autoscaler metrics with the `baseten_llm_*` prefix, alongside the standard platform metrics above.

## `baseten_llm_input_tokens_total`

Total number of input tokens processed.

Type: `counter`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  A hashed identifier for the source pod. Use this label to distinguish per-pod series within a deployment without exposing raw pod names.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_llm_output_tokens_total`

Total number of output tokens generated.

Type: `counter`

Dashboard equivalent: `output_tokens`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  A hashed identifier for the source pod. Use this label to distinguish per-pod series within a deployment without exposing raw pod names.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_llm_input_tokens_per_request`

Distribution of input tokens per request.

Type: `histogram`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  A hashed identifier for the source pod. Use this label to distinguish per-pod series within a deployment without exposing raw pod names.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_llm_output_tokens_per_request`

Distribution of output tokens per request.

Type: `histogram`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  A hashed identifier for the source pod. Use this label to distinguish per-pod series within a deployment without exposing raw pod names.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_llm_tokens_per_second_per_request`

Distribution of tokens per second per request.

Type: `histogram`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  A hashed identifier for the source pod. Use this label to distinguish per-pod series within a deployment without exposing raw pod names.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_llm_kv_cache_hit_rate`

Distribution of KV cache hit rates observed by workers. Values are between 0 and 1.

Type: `histogram`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  A hashed identifier for the source pod. Use this label to distinguish per-pod series within a deployment without exposing raw pod names.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_llm_spec_decode_num_accepted_tokens_total`

Total number of accepted tokens from speculative decoding. Only present when speculative decoding is active on the deployment.

Type: `counter`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  A hashed identifier for the source pod. Use this label to distinguish per-pod series within a deployment without exposing raw pod names.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_llm_spec_decode_num_draft_tokens_total`

Total number of draft tokens generated by speculative decoding. Only present when speculative decoding is active on the deployment.

Type: `counter`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  A hashed identifier for the source pod. Use this label to distinguish per-pod series within a deployment without exposing raw pod names.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_llm_in_flight_tokens`

Instantaneous number of in-flight tokens across the deployment, including worker load and router-queued tokens.

Type: `gauge`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  A hashed identifier for the source pod. Use this label to distinguish per-pod series within a deployment without exposing raw pod names.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_llm_avg_in_flight_tokens`

Trailing average of in-flight tokens over the deployment's `autoscaling_window`.

Type: `gauge`

Dashboard equivalent: `autoscaler_avg_in_flight_tokens`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  A hashed identifier for the source pod. Use this label to distinguish per-pod series within a deployment without exposing raw pod names.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## `baseten_llm_num_requests`

Instantaneous number of concurrent in-flight requests across BIS-LLM workers.

Type: `gauge`

Dashboard equivalent: `concurrent_requests`

Labels:

  The ID of the model.

  The name of the model.

  The ID of the deployment.

  A hashed identifier for the source pod. Use this label to distinguish per-pod series within a deployment without exposing raw pod names.

  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.

  The phase of the deployment in the [[Deployments|promote to production process]]. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`

## vLLM and SGLang metrics

When Baseten [[Metrics|detects vLLM or SGLang]] on your deployment, it scrapes your container's `/metrics` endpoint and exports the engine's native metrics alongside Baseten's own. These also appear as graphs in the [[Metrics|Metrics tab]].

The engines define these metrics, not Baseten, and they change between versions. For the complete, current list, always refer to the official [vLLM](https://docs.vllm.ai/en/latest/design/v1/metrics.html) and [SGLang](https://docs.sglang.io/references/production_metrics.html) metrics documentation.

Baseten normalizes these metrics across engine versions and exports the most useful ones. Some exported metrics include tokens per second, time to first token, KV cache usage, and the number of requests running or queued.

Baseten attaches the same two labels to every exported engine metric:

  The ID of the deployment.

  The ID of the replica.

---
Part of [[Export Metrics (Observability)]]
