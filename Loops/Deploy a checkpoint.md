---
tags: [baseten, loops]
source: https://docs.baseten.co/loops/deploy-checkpoints
---

> Turn a Loops sampler checkpoint into a dedicated inference deployment and call it.

A sampler checkpoint deploys to a dedicated Baseten inference deployment that serves the base model with your LoRA adapter loaded. Deployment works whether or not the training session is still running: checkpoints outlive the session, so you can [[Quickstart|shut the trainer and sampler down]] first and deploy later.

Deploying needs an `hf_access_token` in [[Secrets (Organization)|workspace secrets]], because the deployment downloads the base weights from Hugging Face.

## Deploy from the CLI

Run [[Loops CLI reference|`truss loops checkpoints deploy`]] with the checkpoint's globally unique `id` (the `id` field from [[Quickstart|listing checkpoints]], not the checkpoint name):

```bash theme={"system"}
uvx truss loops checkpoints deploy --checkpoint-ids <id>
```

The `--checkpoint-ids` flag skips the checkpoint picker, but the command still prompts for a model name, GPU type, GPU count, and the Hugging Face secret name (default `hf_access_token`). A successful deploy prints the IDs you need to call the model:

```output theme={"system"}
Successfully created deployment: deployment-1
Model ID: wnpkzp03
Deployment ID: qrpg2r0
Deployment succeeded.
Set the model parameter on each request to the Loops checkpoint name (e.g. step-100).
```

The deployment downloads base weights and starts the inference server, so several minutes pass before it reaches `ACTIVE`.

To inspect the generated Truss config without deploying, pass `--dry-run`.

## Deploy from the dashboard

Every Loop has a page in the dashboard at `app.baseten.co/training/loop/<run_id>`, reachable from the Training tab. Its Checkpoints table lists each saved checkpoint with its `bt://` path, type, and size, and is where you deploy one; the flow matches [[Get started (Training)|deploying job checkpoints]].

## Call the deployed model

Call the deployment's OpenAI-compatible chat completions route. The URL includes the deployment ID, and `model` is the checkpoint *name* (`checkpoint_id`), not its globally unique `id`:

  ```bash Request theme={"system"}
  curl -X POST "https://model-<model_id>.api.baseten.co/deployment/<deployment_id>/sync/v1/chat/completions" \
    -H "Authorization: Bearer $BASETEN_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "step-1",
      "messages": [{"role": "user", "content": "What is the capital of France?"}]
    }'
  ```

  ```json Output theme={"system"}
  {
    "model": "step-1",
    "choices": [
      {
        "message": {
          "role": "assistant",
          "content": "The capital of France is **Paris**.\n\nLocated in northeastern France…"
        },
        "finish_reason": "length"
      }
    ]
  }
  ```

For request options, streaming, and client libraries, see [[Call your model (Inference)|calling your model]].

## Delete the deployment

The deployment bills for its GPU while it's live. Delete it with [[Delete models|`DELETE /v1/models/{model_id}`]] when you're done:

  ```bash Request theme={"system"}
  curl -X DELETE "https://api.baseten.co/v1/models/<model_id>" \
    -H "Authorization: Bearer $BASETEN_API_KEY"
  ```

  ```json Output theme={"system"}
  {"id": "wnpkzp03", "deleted": true}
  ```

Deleting the deployment doesn't touch the checkpoint. You can redeploy it any time.

## Next steps

* **[[Train on a dataset]]**: Move from the quickstart's single example to a real training loop.
* **[[Concepts (Loops)|Loops concepts]]**: How checkpoints relate to sessions, trainers, and samplers.

---
Part of [[Loops Hub]]
