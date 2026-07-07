---
tags: [baseten, deployment]
source: https://docs.baseten.co/deployment/concepts
---

> Deployments, environments, resources, autoscaling, and CI/CD on Baseten.

When you run `truss push`, Baseten creates a [[Deployments|deployment]]: a running instance of your model on GPU infrastructure with an API endpoint. This page explains how deployments are managed, versioned, and scaled.

## Deployments

A [[Deployments|deployment]] is a single version of your model running on specific hardware. Every `truss push` creates a new deployment. You can have multiple deployments of the same model running simultaneously, which is how you test new versions without affecting production traffic. Deployments can be deactivated to stop serving (and stop incurring cost) or deleted permanently when they're no longer needed.

For rapid iteration, use `truss push --watch` to create a **development deployment**, a mutable instance that live-reloads as you edit your model code. Development deployments can't be promoted to an environment.

<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployments.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=833c7f33c3a39b50502326b9cec14090" alt="Baseten deployments dashboard showing multiple model versions" width="964" height="552" data-path="images/deployments.png" />

## Environments

As your model matures, you'll want a way to manage releases. [[Environments]] provide stable endpoints that persist across deployments. A typical setup has a development environment for testing and a production environment for live traffic. Each environment maintains its own autoscaling settings, metrics, and endpoint URL. When a new deployment is ready, you promote it to an environment, and traffic shifts to the new version without changing the endpoint your application calls.

<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=e922f3e12c24577d6594ca58f80431ee" alt="Deployment environments with development and production endpoints" width="964" height="552" data-path="images/deployment-environments.png" />

## Resources

Every deployment runs on a specific [[Resources|instance type]] that defines its GPU, CPU, and memory allocation. Choosing the right instance balances inference speed against cost. You'll set the instance type in your `config.yaml` before deployment, or adjust it later through the Baseten UI. Smaller models run well on an L4 (24 GB VRAM), while large LLMs may need A100s or H100s with tensor parallelism across multiple GPUs.

<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=028f7b8a7c5e1d92f0b55f2eec8aad11" alt="Resource configuration showing GPU instance type selection" width="964" height="552" data-path="images/deployment-resources.png" />

## Autoscaling

You don't manage replicas manually. [[Autoscaling]] adjusts the number of running instances based on incoming traffic. You'll configure a minimum and maximum replica count, a concurrency target, and a scale-down delay. When traffic drops, replicas scale down (optionally to zero, eliminating all cost). When traffic spikes, new replicas spin up automatically. [[Cold starts|Cold start optimization]] and network acceleration keep response times fast even when scaling from zero.

<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=f867eb7ccef178bae2fd11117365bebb" alt="Autoscaling configuration with replica count and concurrency settings" width="964" height="552" data-path="images/deployment-autoscaling.png" />

For the mechanics of how the autoscaler tracks in-flight requests and adjusts replicas, see [[How Baseten works]]. For engine-specific autoscaling settings (BEI and Engine-Builder-LLM), see [[Autoscaling engines]].

## Request lifecycle

When a request reaches your deployment, it passes through authentication, routing, and replica selection before your model code executes. Understanding this path helps you diagnose errors and configure timeouts. See [[Request lifecycle]] for the full journey of a request, including queuing, load shedding, and HTTP status codes.

## CI/CD

When your model code lives in a Git repository, you can automate deployments with CI/CD. The [[CICD|Truss Push GitHub Action]] deploys your model, validates it with a predict request, and optionally promotes it to production. You'll configure the trigger (such as pushes or pull requests to specific branches) in your GitHub Actions workflow file.

---
Part of [[Deployment Hub]]
