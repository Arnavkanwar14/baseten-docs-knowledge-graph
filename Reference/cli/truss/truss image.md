---
tags: [baseten, reference, cli]
source: https://docs.baseten.co/reference/cli/truss/image
---

> Build and manage Truss Docker images.

```sh theme={"system"}
truss image [OPTIONS] COMMAND [ARGS]...
```

Build and manage Docker images for your Truss.

***

## `build`

Build the Docker image for a Truss.

```sh theme={"system"}
truss image build [OPTIONS] [TARGET_DIRECTORY] [BUILD_DIR]
```

### Options

  Docker image tag.

  Use the host network for the Docker build.

  Logging verbosity. `humanfriendly` (default) is pretty-printed; `INFO`, `DEBUG`, `WARNING` produce structured logs.

  Disable interactive prompts. Use in CI/automated contexts where stdin isn't a TTY.

### Arguments

  A Truss directory. Defaults to current directory.

  Image context directory. If not provided, a temp directory is created.

**Example:**

Build a Docker image for your Truss:

```sh theme={"system"}
truss image build
```

Build with a custom tag:

```sh theme={"system"}
truss image build --tag my-model:v1
```

***

## `build-context`

Create a Docker build context for a Truss without building the image.

```sh theme={"system"}
truss image build-context [OPTIONS] BUILD_DIR [TARGET_DIRECTORY]
```

### Options

  Logging verbosity. `humanfriendly` (default) is pretty-printed; `INFO`, `DEBUG`, `WARNING` produce structured logs.

  Disable interactive prompts. Use in CI/automated contexts where stdin isn't a TTY.

### Arguments

  Directory where image context is created.

  A Truss directory. Defaults to current directory.

**Example:**

Create a build context in a specific directory:

```sh theme={"system"}
truss image build-context ./build-context
```

***

## `run`

Run the Docker image for a Truss locally.

```sh theme={"system"}
truss image run [OPTIONS] [TARGET_DIRECTORY] [BUILD_DIR]
```

### Options

  Docker image tag to run.

  Local port to expose the model on.

  Attach to the container process.

  Use the host network for the Docker build and run.

  Logging verbosity. `humanfriendly` (default) is pretty-printed; `INFO`, `DEBUG`, `WARNING` produce structured logs.

  Disable interactive prompts. Use in CI/automated contexts where stdin isn't a TTY.

### Arguments

  A Truss directory. Defaults to current directory.

  Image context directory. If not provided, a temp directory is created.

**Example:**

Build and run a Truss locally:

```sh theme={"system"}
truss image run
```

Run on a custom port:

```sh theme={"system"}
truss image run --port 9000
```

Run in attached mode:

```sh theme={"system"}
truss image run --attach
```

---
Part of [[Cli (Reference)]]
