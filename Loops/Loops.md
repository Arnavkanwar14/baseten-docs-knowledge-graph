---
tags: [baseten, loops]
source: https://docs.baseten.co/loops/overview
---

> Run Tinker-compatible SFT and async RL at long sequence lengths, then deploy checkpoints to the Baseten Inference Stack.

> **Note:**
  Loops is in early access. [Fill out the signup form](https://www.baseten.co/talk-to-us/loops-signup/) to request access for your workspace.

Loops is a Tinker-compatible training SDK for post-training large models at long sequence lengths. It lets you deploy dedicated training and sampling servers for any [[Supported base models|supported base model]], then run your existing Tinker scripts with minimal changes.

## How Loops works

A Loops session pairs a trainer with a sampler. The trainer runs forward, backward, and optimizer steps; the sampler generates from the latest weights the trainer publishes. They scale independently, so RL rollouts don't compete with training for compute, and you can await weight transfers synchronously or asynchronously to stay on-policy or run bounded off-policy algorithms.

Checkpoints are yours: download them as presigned URLs or deploy them to the Baseten Inference Stack through the UI, CLI, or API.

The [[Training on Baseten|Training overview]] compares Loops with Truss Train (the bring-your-own-container alternative) side by side.

## Where to go next

The [[Quickstart|Loops quickstart]] runs the full session lifecycle: train a step, sample from the tuned weights, list the checkpoint, and shut the servers down.

The [[Concepts (Loops)|Loops concepts]] page covers sessions, trainers, samplers, and checkpoints, and how weight sync keeps the trainer and sampler in step.

The [[Tinker compatibility]] page lists which Tinker API calls work unchanged in Loops and what behaves differently.

---
Part of [[Loops Hub]]
