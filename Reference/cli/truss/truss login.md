---
tags: [baseten, reference, cli]
source: https://docs.baseten.co/reference/cli/truss/login
---

> Authenticate with Baseten.

```sh theme={"system"}
truss login [OPTIONS]
```

Authenticates with Baseten and stores the credential for reuse by other Truss commands.

`truss login` is an alias for [[truss auth|`truss auth login`]].
With no flags, it runs interactively and prompts you to choose between pasting an API key and logging in through your browser.
To authenticate non-interactively, pass `--browser` or `--api-key`.

For details on how Truss stores credentials and how to manage multiple remotes, see [[truss auth|`truss auth`]].

### Options

  Log in through your browser using the OAuth device flow. Mutually exclusive with `--api-key`.

  Baseten [[API keys|API key]]. If provided, the command runs in non-interactive mode. Mutually exclusive with `--browser`.

  Name of the remote to create or update in `~/.trussrc`. Defaults to `baseten`.

  Logging verbosity. `humanfriendly` (default) is pretty-printed; `INFO`, `DEBUG`, `WARNING` produce structured logs.

  Disable interactive prompts. Use in CI/automated contexts where stdin isn't a TTY.

**Examples:**

Authenticate interactively and choose a method when prompted:

```bash theme={"system"}
# Using a local truss installation
truss login

# Using uvx (no installation required)
uvx truss login
```

You should see:

```
💻 Let's add a Baseten remote!
? How would you like to authenticate?
  Paste an API key
> Log in via browser (OAuth)
```

Authenticate non-interactively with an API key:

```bash theme={"system"}
truss login --api-key $BASETEN_API_KEY
# or with uvx:
uvx truss login --api-key $BASETEN_API_KEY
```

Log in through your browser:

```bash theme={"system"}
truss login --browser
# or with uvx:
uvx truss login --browser
```

The CLI opens your browser to the verification page with your user code pre-filled. Approve the request, and the CLI automatically stores the OAuth tokens and prints:

```
🔓 Logged in to remote `baseten`.
```

---
Part of [[Cli (Reference)]]
