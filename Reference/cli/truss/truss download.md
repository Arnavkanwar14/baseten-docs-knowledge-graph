---
tags: [baseten, reference, cli]
source: https://docs.baseten.co/reference/cli/truss/download
---

> Download the Truss for a deployed model.

```sh theme={"system"}
truss download [OPTIONS]
```

Downloads the Truss for a deployed model as a tar file or extracts it into a directory. Use this to inspect the exact configuration and code that is running for a deployment, or to recover a Truss when the original source is unavailable.

You must pass exactly one of `--out-file` or `--out-dir`.

### Options

  Name of the remote in `.trussrc`. If omitted, Truss prompts to select one.

  ID of the model.

  ID of the deployment.

  Save the Truss as a tar file at this path. Mutually exclusive with `--out-dir`.

  Extract the Truss into this directory. Mutually exclusive with `--out-file`.

  Allow overwriting an existing file or non-empty directory. Without this flag, the command fails if the target file exists or the target directory is non-empty.

  Logging verbosity. `humanfriendly` (default) is pretty-printed; `INFO`, `DEBUG`, `WARNING` produce structured logs.

  Disable interactive prompts. Use in CI/automated contexts where stdin isn't a TTY.

**Examples:**

Download a Truss as a tar file:

```sh theme={"system"}
truss download --model-id YOUR_MODEL_ID --deployment-id YOUR_DEPLOYMENT_ID --out-file my-truss.tar
```

Extract a Truss into a directory:

```sh theme={"system"}
truss download --model-id YOUR_MODEL_ID --deployment-id YOUR_DEPLOYMENT_ID --out-dir ./my-truss
```

Overwrite an existing tar file:

```sh theme={"system"}
truss download --model-id YOUR_MODEL_ID --deployment-id YOUR_DEPLOYMENT_ID --out-file my-truss.tar --overwrite
```

---
Part of [[Cli (Reference)]]
