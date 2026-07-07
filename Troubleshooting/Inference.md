---
tags: [baseten, troubleshooting]
source: https://docs.baseten.co/troubleshooting/inference
---

> Troubleshoot common problems during model inference

For HTTP status code and error message meanings (such as what a `502` indicates), see [[Inference errors]].

## Model I/O issues

### Error: JSONDecodeError

```
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

This error means you're attempting to pass a model input that is not JSON-serializable. For example, you might have left out the double quotes required for a valid string:

```sh theme={"system"}
truss predict -d 'This is not a string' # Wrong
truss predict -d '"This is a string"'   # Correct
```

## Model version issues

### Error: No OracleVersion matches the given query

```

```

Make sure that the model ID or deployment ID you're passing is correct and that the associated model has not been deleted.

Additionally, make sure you're using the correct endpoint:

* [Production environment endpoint](/reference/inference-api/predict-endpoints/environments-predict).
* [Development deployment endpoint](/reference/inference-api/predict-endpoints/development-predict).
* [Deployment endpoint](/reference/inference-api/predict-endpoints/deployment-predict).

## Authentication issues

### Error: Service provider not found

```
ValueError: Service provider example-service-provider not found in ~/.trussrc
```

This error means your `~/.trussrc` is incomplete or incorrect. It should be formatted as follows:

```
[baseten]
remote_provider = baseten
api_key = YOUR.API_KEY
remote_url = https://app.baseten.co
```

### Error: You have to log in to perform the request

```

```

This error occurs on `truss predict` when the API key in `~/.trussrc` for a given host is missing or incorrect. To fix it, update your API key in the `~/.trussrc` file.

### Error: Please check the API key you provided

```
{
        "error": "please check the api-key you provided"
}
```

This error occurs when using `curl` or similar to call the model through its API endpoint when the API key passed in the request header is not valid. Make sure you're using a valid API key then try again.

---
Part of [[Troubleshooting Hub]]
