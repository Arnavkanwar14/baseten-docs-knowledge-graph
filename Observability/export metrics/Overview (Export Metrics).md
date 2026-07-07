---
tags: [baseten, observability, export-metrics]
source: https://docs.baseten.co/observability/export-metrics/overview
---

> Export metrics from Baseten to your observability stack

Baseten provides a metrics endpoint in Prometheus format, allowing integration with observability tools like Prometheus, OpenTelemetry Collector, Datadog Agent, and Vector.

## Set up metrics scraping

  

  
    Use the Authorization header with a [Baseten API key](https://app.baseten.co/settings/api_keys):

    ```json theme={"system"}
    {"Authorization": "Bearer YOUR_API_KEY"}
    ```
  

  
    Recommended 1-minute interval (metrics update every 30 seconds).
  

## Supported integrations

Baseten metrics can be collected through [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) and exported to:

* [[Export to Prometheus|Prometheus]]
* [[Export to Datadog|Datadog]]
* [[Export to Grafana Cloud|Grafana]]
* [[Export to New Relic|New Relic]]

For available metrics, see the [[Metrics support matrix|supported metrics reference]].

## Rate limits

* **6 requests per minute per organization**
* Exceeding this limit results in **HTTP 429 (Too Many Requests)** responses.
* To stay within limits, use a **1-minute scrape interval**.

---
Part of [[Export Metrics (Observability)]]
