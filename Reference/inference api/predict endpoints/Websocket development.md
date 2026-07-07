---
tags: [baseten, reference, inference-api]
source: https://docs.baseten.co/reference/inference-api/predict-endpoints/development-websocket
---

> Connect over WebSocket to the development deployment of a model or chain.

Use this endpoint to connect over WebSockets to the development deployment of a model or chain.

```sh theme={"system"}
wss://{entity}-{entity_id}.api.baseten.co/development/websocket
```

See [[WebSockets]] for more details.

### Parameters

  The type of entity you want to connect to. Either `model` or `chain`.

  The ID of the model or chain you want to connect to.

  Your Baseten API key, passed as `Authorization: Bearer $BASETEN_API_KEY`. `Api-Key` is also accepted as the scheme.

  ```sh websocat theme={"system"}
  websocat -H 'Authorization: Bearer EMPTY' \
      wss://{entity}-{entity_id}.api.baseten.co/development/websocket
  ```

---
Part of [[Inference Api (Reference)]]
