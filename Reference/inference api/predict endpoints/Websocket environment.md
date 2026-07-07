---
tags: [baseten, reference, inference-api]
source: https://docs.baseten.co/reference/inference-api/predict-endpoints/environments-websocket
---

> Connect over WebSocket to the deployment associated with an environment.

Use this endpoint to connect over WebSockets to the deployment associated with the specified [[Environments|environment]].

`entity` is `model` or `chain`, depending on whether you call a Baseten model or a Chain.

```sh theme={"system"}
wss://{entity}-{entity_id}.api.baseten.co/environments/{env_name}/websocket
```

See [[WebSockets]] for more details.

### Parameters

  The type of entity you want to connect to. Either `model` or `chain`.

  The ID of the model or chain you want to connect to.

  The name of the environment you want to connect to.

  Your Baseten API key, passed as `Authorization: Bearer $BASETEN_API_KEY`. `Api-Key` is also accepted as the scheme.

  ```sh websocat theme={"system"}
  websocat -H 'Authorization: Bearer EMPTY' \
      wss://{entity}-{model_id}.api.baseten.co/environments/{env_name}/websocket
  ```

---
Part of [[Inference Api (Reference)]]
