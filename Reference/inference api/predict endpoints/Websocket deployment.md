---
tags: [baseten, reference, inference-api]
source: https://docs.baseten.co/reference/inference-api/predict-endpoints/deployment-websocket
---

> Connect over WebSocket to a specific deployment.

Use this endpoint to connect over WebSockets to a specific deployment.

`entity` is `model` or `chain`, depending on whether you call a Baseten model or a Chain.

```sh theme={"system"}
wss://{entity}-{entity_id}.api.baseten.co/deployment/{deployment_id}/websocket
```

See [[WebSockets]] for more details.

### Parameters

  The type of entity you want to connect to. Either `model` or `chain`.

  The ID of the model or chain you want to connect to.

  The ID of the deployment you want to connect to.

  Your Baseten API key, passed as `Authorization: Bearer $BASETEN_API_KEY`. `Api-Key` is also accepted as the scheme.

  ```sh websocat theme={"system"}
  websocat -H 'Authorization: Bearer EMPTY' \
      wss://{entity}-{model_id}.api.baseten.co/deployment/{deployment_id}/websocket
  ```

---
Part of [[Inference Api (Reference)]]
