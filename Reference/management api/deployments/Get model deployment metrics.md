---
tags: [baseten, reference, management-api]
source: https://docs.baseten.co/reference/management-api/deployments/get-deployment-metrics
---

> Gets the metrics for a model deployment in the given time range.

> **Note:**
  This endpoint is in beta. The request and response structure may change before it's generally available.

## OpenAPI

````yaml get /v1/models/{model_id}/deployments/{deployment_id}/metrics
openapi: 3.1.0
info:
  description: REST API for management of Baseten resources
  title: Baseten management API
  version: 1.0.0
servers:
  - url: https://api.baseten.co
security:
  - BearerAuth: []
paths:
  /v1/models/{model_id}/deployments/{deployment_id}/metrics:
    parameters:
      - $ref: '#/components/parameters/model_id'
      - $ref: '#/components/parameters/deployment_id'
    get:
      summary: Gets the metrics for a model deployment.
      description: Gets the metrics for a model deployment in the given time range.
      parameters:
        - name: mode
          in: query
          required: false
          description: >-
            'CURRENT': a single instantaneous snapshot at now; start/end must be
            omitted. 'SUMMARY': a single value set aggregating the whole window.
            'SERIES': evenly-spaced value sets across the window, with the step
            derived from the window duration.
          schema:
            $ref: '#/components/schemas/DeploymentMetricModeV1'
            default: CURRENT
        - name: start_epoch_millis
          in: query
          required: false
          description: >-
            Epoch millis timestamp to start fetching metrics. Defaults to one
            hour before the end.
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            default: null
            title: Start Epoch Millis
        - name: end_epoch_millis
          in: query
          required: false
          description: >-
            Epoch millis timestamp to end fetching metrics. Defaults to the
            current time. The window between start and end must not exceed 7
            days.
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            default: null
            title: End Epoch Millis
        - name: metrics
          in: query
          required: false
          description: >-
            Names of the metrics to return; see
            https://docs.baseten.co/observability/export-metrics/supported-metrics
            for the available names. When omitted, a default set is returned:
            baseten_replicas_active, baseten_inference_requests_total, and
            baseten_end_to_end_response_time_seconds. Unknown names are
            rejected; valid names that do not apply to the deployment are
            omitted from the response.
          schema:
            items:
              type: string
            title: Metrics
            type: array
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetDeploymentMetricsResponseV1'
      x-codeSamples:
        - lang: bash
          source: >
            curl --request GET \

            --url
            https://api.baseten.co/v1/models/{model_id}/deployments/{deployment_id}/metrics
            \

            --header "Authorization: Bearer $BASETEN_API_KEY"
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/models/{model_id}/deployments/{deployment_id}/metrics"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "GET",
                url,
                headers=headers,
                json={}
            )

            print(response.text)
components:
  parameters:
    model_id:
      schema:
        type: string
      name: model_id
      in: path
      required: true
    deployment_id:
      schema:
        type: string
      name: deployment_id
      in: path
      required: true
  schemas:
    DeploymentMetricModeV1:
      description: How metric values are aggregated over the request.
      enum:
        - CURRENT
        - SUMMARY
        - SERIES
      title: DeploymentMetricModeV1
      type: string
    GetDeploymentMetricsResponseV1:
      description: >-
        Deployment metrics over a time window, index-mapped: metric descriptors

        appear once in ``metric_descriptors``; each value set's ``values`` are
        aligned

        to that order.
      properties:
        start_epoch_millis:
          description: Start of the returned window.
          title: Start Epoch Millis
          type: integer
        end_epoch_millis:
          description: End of the returned window.
          title: End Epoch Millis
          type: integer
        mode:
          $ref: '#/components/schemas/DeploymentMetricModeV1'
          description: The aggregation mode used.
        step_seconds:
          anyOf:
            - type: integer
            - type: 'null'
          description: Seconds per step; populated only in SERIES mode, null otherwise.
          title: Step Seconds
        metric_descriptors:
          description: Descriptors for each metric; position defines the values index.
          items:
            $ref: '#/components/schemas/DeploymentMetricDescriptorV1'
          title: Metric Descriptors
          type: array
        metric_values:
          description: >-
            Metric values per time step covering the window. In summary mode
            this always contains exactly one value set spanning the whole
            window.
          items:
            $ref: '#/components/schemas/DeploymentMetricValueSetV1'
          title: Metric Values
          type: array
      required:
        - start_epoch_millis
        - end_epoch_millis
        - mode
        - step_seconds
        - metric_descriptors
        - metric_values
      title: GetDeploymentMetricsResponseV1
      type: object
    DeploymentMetricDescriptorV1:
      description: >-
        Describes one metric. Its position in the response
        ``metric_descriptors``

        list is the index used to read that metric out of each value set's
        ``values``.

        A metric may break down into multiple labeled series (e.g. latency
        quantiles,

        or volume by status). ``label_sets`` enumerates those series in order;
        each

        value set's value for this metric is a list aligned to that order.
      properties:
        name:
          description: Canonical metric name.
          title: Name
          type: string
        unit_hint:
          $ref: '#/components/schemas/DeploymentMetricUnitHintV1'
          description: Advisory unit of the metric's values.
        kind:
          $ref: '#/components/schemas/DeploymentMetricKindV1'
          description: >-
            Semantic hint for how the metric behaves (GAUGE, COUNTER,
            HISTOGRAM).
        label_sets:
          description: >-
            The metric's series, in order. Each entry is the set of labels
            identifying one series; the value at the same index in each value
            set's ``values`` is that series' value. A plain metric has a single
            entry with no labels (`{}`). A histogram has one entry per quantile
            plus an average, e.g. {'quantile': '0.5'} … {'quantile': '0.99'},
            {'stat': 'avg'}. A by-status metric has one entry per status, e.g.
            {'status': '2xx'}.
          items:
            additionalProperties:
              type: string
            type: object
          title: Label Sets
          type: array
      required:
        - name
        - unit_hint
        - kind
        - label_sets
      title: DeploymentMetricDescriptorV1
      type: object
    DeploymentMetricValueSetV1:
      description: >-
        The metric values for one time step. ``values`` is aligned by index to
        the

        response ``metric_descriptors`` list.
      properties:
        start_epoch_millis:
          description: >-
            Start of the step. The step spans until the next value set's start,
            or the window end for the last one; a summary has a single value set
            starting at the window start.
          title: Start Epoch Millis
          type: integer
        values:
          description: >-
            Metric values aligned to the ``metric_descriptors`` index. Each
            entry is a list aligned to that descriptor's ``label_sets`` (a
            single-element list for a plain metric). A series with no data in
            this step is null.
          items:
            items:
              anyOf:
                - type: number
                - type: 'null'
            type: array
          title: Values
          type: array
      required:
        - start_epoch_millis
        - values
      title: DeploymentMetricValueSetV1
      type: object
    DeploymentMetricUnitHintV1:
      description: >-
        Advisory unit of a metric's values. Values are reported as scraped, so
        the

        hint describes the raw value (e.g. GPU memory is reported in mebibytes).

        - ``PER_SECOND``: a rate per second.

        - ``SECONDS``: a duration in seconds.

        - ``BYTES``: a size in bytes.

        - ``MEBIBYTES``: a size in mebibytes (MiB).

        - ``COUNT``: a dimensionless tally of discrete things.

        - ``RATIO``: a dimensionless ratio. Usually in ``[0, 1]`` but may exceed
        1
          (e.g. CPU usage in cores = cpu-seconds/second).
      enum:
        - PER_SECOND
        - SECONDS
        - BYTES
        - MEBIBYTES
        - COUNT
        - RATIO
      title: DeploymentMetricUnitHintV1
      type: string
    DeploymentMetricKindV1:
      description: >-
        Semantic hint for how a metric behaves, to aid client rendering and

        aggregation. It does not describe the value's shape — that is carried by
        the

        descriptor's ``label_sets`` (a metric may break down into multiple
        series).

        - ``GAUGE``: an instantaneous value (e.g. queue size, running requests).

        - ``COUNTER``: a cumulative total over the step (e.g. tokens, restarts).

        - ``HISTOGRAM``: a distribution, exposed as quantile/average series.
      enum:
        - GAUGE
        - COUNTER
        - HISTOGRAM
      title: DeploymentMetricKindV1
      type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Send `Authorization: Bearer <api_key>`. The legacy `Authorization:
        Api-Key <api_key>` scheme is also accepted.

````

---
Part of [[Management Api (Reference)]]
