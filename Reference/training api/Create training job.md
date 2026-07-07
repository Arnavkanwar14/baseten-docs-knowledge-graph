---
tags: [baseten, reference, training-api]
source: https://docs.baseten.co/reference/training-api/create-training-job
---

> Creates a training job with the specified configuration.

## OpenAPI

````yaml post /v1/training_projects/{training_project_id}/jobs
openapi: 3.1.0
info:
  description: REST API for management of Baseten resources
  title: Baseten management API
  version: 1.0.0
servers:
  - url: https://api.baseten.co
security:
  - BearerAuth: []
paths:
  /v1/training_projects/{training_project_id}/jobs:
    parameters:
      - $ref: '#/components/parameters/training_project_id'
    post:
      summary: Create a training job.
      description: Creates a training job with the specified configuration.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateTrainingJobRequestV1'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateTrainingJobResponseV1'
      x-codeSamples:
        - lang: bash
          source: >-
            curl --request POST \

            --url
            https://api.baseten.co/v1/training_projects/{training_project_id}/jobs
            \

            --header "Authorization: Bearer $BASETEN_API_KEY" \

            --data '{
              "training_job": {
                "image": {
                  "base_image": "hello-world",
                  "docker_auth": null
                },
                "compute": {
                  "node_count": 1,
                  "cpu_count": 1,
                  "memory": "2Gi",
                  "accelerator": {
                    "accelerator": "H100",
                    "count": 2
                  },
                  "availability_model": "spot"
                },
                "runtime": {
                  "start_commands": [
                    "python main.py"
                  ],
                  "environment_variables": {
                    "API_KEY": "your_api_key_here",
                    "PATH": "/usr/bin"
                  },
                  "enable_cache": true,
                  "cache_config": {
                    "enable_legacy_hf_mount": true,
                    "enabled": true,
                    "mount_base_path": "/root/.cache",
                    "require_cache_affinity": true
                  },
                  "checkpointing_config": {
                    "enabled": true,
                    "checkpoint_path": "/mnt/ckpts",
                    "volume_size_gib": 10
                  },
                  "load_checkpoint_config": null
                },
                "name": "gpt-oss-job",
                "truss_user_env": null,
                "interactive_session": null,
                "weights": [
                  {
                    "allow_patterns": null,
                    "auth": null,
                    "auth_secret_name": null,
                    "ignore_patterns": null,
                    "mount_location": "/app/models/base",
                    "source": "hf://meta-llama/Llama-3-8B@main"
                  }
                ],
                "enable_baseten_workdir": false,
                "priority": 0
              }
            }'
        - lang: python
          source: >-
            import requests

            import os

            API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

            url =
            "https://api.baseten.co/v1/training_projects/{training_project_id}/jobs"

            headers = {"Authorization": f"Bearer {API_KEY}"}

            response = requests.request(
                "POST",
                url,
                headers=headers,
                json={'training_job': {'image': {'base_image': 'hello-world', 'docker_auth': None}, 'compute': {'node_count': 1, 'cpu_count': 1, 'memory': '2Gi', 'accelerator': {'accelerator': 'H100', 'count': 2}, 'availability_model': 'spot'}, 'runtime': {'start_commands': ['python main.py'], 'environment_variables': {'API_KEY': 'your_api_key_here', 'PATH': '/usr/bin'}, 'enable_cache': True, 'cache_config': {'enable_legacy_hf_mount': True, 'enabled': True, 'mount_base_path': '/root/.cache', 'require_cache_affinity': True}, 'checkpointing_config': {'enabled': True, 'checkpoint_path': '/mnt/ckpts', 'volume_size_gib': 10}, 'load_checkpoint_config': None}, 'name': 'gpt-oss-job', 'truss_user_env': None, 'interactive_session': None, 'weights': [{'allow_patterns': None, 'auth': None, 'auth_secret_name': None, 'ignore_patterns': None, 'mount_location': '/app/models/base', 'source': 'hf://meta-llama/Llama-3-8B@main'}], 'enable_baseten_workdir': False, 'priority': 0}}
            )

            print(response.text)
components:
  parameters:
    training_project_id:
      schema:
        type: string
      name: training_project_id
      in: path
      required: true
  schemas:
    CreateTrainingJobRequestV1:
      description: A request to create a training job.
      properties:
        training_job:
          $ref: '#/components/schemas/CreateTrainingJobV1'
          description: The training job to create.
      required:
        - training_job
      title: CreateTrainingJobRequestV1
      type: object
    CreateTrainingJobResponseV1:
      description: A response to creating a training job.
      properties:
        training_job:
          $ref: '#/components/schemas/TrainingJobV1'
          description: The created training job.
      required:
        - training_job
      title: CreateTrainingJobResponseV1
      type: object
    CreateTrainingJobV1:
      description: Configuration for a training job.
      properties:
        image:
          $ref: '#/components/schemas/CreateTrainingJobImageV1'
          examples:
            - base_image: hello-world
              docker_auth: null
        compute:
          $ref: '#/components/schemas/CreateTrainingJobComputeV1'
          examples:
            - accelerator:
                accelerator: H100
                count: 2
              availability_model: spot
              cpu_count: 1
              memory: 2Gi
              node_count: 1
        runtime:
          $ref: '#/components/schemas/CreateTrainingJobRuntimeV1'
          description: Configuration for the runtime environment of the training job.
          examples:
            - artifacts: []
              cache_config: null
              checkpointing_config:
                checkpoint_path: null
                enabled: false
                volume_size_gib: null
              enable_cache: null
              environment_variables:
                API_KEY: your_api_key_here
                PATH: /usr/bin
              load_checkpoint_config: null
              start_commands:
                - python main.py
        name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Name of the training job.
          examples:
            - gpt-oss-job
          title: Name
        truss_user_env:
          anyOf:
            - $ref: '#/components/schemas/TrussUserEnv'
            - type: 'null'
          default: null
          description: Truss user environment information
        interactive_session:
          anyOf:
            - $ref: '#/components/schemas/InteractiveSessionConfigV1'
            - type: 'null'
          default: null
          description: Configuration for interactive debugging sessions.
        weights:
          description: >-
            MDN weight sources to mount in the training container. Weights are
            mirrored and cached for fast startup.
          examples:
            - - allow_patterns: null
                auth: null
                auth_secret_name: null
                ignore_patterns: null
                mount_location: /app/models/base
                source: hf://meta-llama/Llama-3-8B@main
          items:
            $ref: '#/components/schemas/CreateJobWeightConfigV1'
          title: Weights
          type: array
        enable_baseten_workdir:
          default: false
          description: >-
            When enabled, uses /b10/workspace as the working directory instead
            of the image WORKDIR.
          examples:
            - false
            - true
          title: Enable Baseten Workdir
          type: boolean
        priority:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Queue priority. Higher values are dequeued first. Defaults to 0.
          examples:
            - 0
            - 10
            - 100
          title: Priority
      required:
        - image
      title: CreateTrainingJobV1
      type: object
    TrainingJobV1:
      properties:
        id:
          description: Unique identifier of the training job.
          title: Id
          type: string
        created_at:
          description: Time the job was created in ISO 8601 format.
          format: date-time
          title: Created At
          type: string
        current_status:
          description: Current status of the training job.
          title: Current Status
          type: string
        error_message:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Error message if the training job failed.
          title: Error Message
        instance_type:
          $ref: '#/components/schemas/InstanceTypeV1'
          description: Instance type of the training job.
        updated_at:
          description: Time the job was updated in ISO 8601 format.
          format: date-time
          title: Updated At
          type: string
        training_project_id:
          description: ID of the training project.
          title: Training Project Id
          type: string
        training_project:
          $ref: '#/components/schemas/TrainingProjectSummaryV1'
          description: Summary of the training project.
        name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Name of the training job.
          examples:
            - gpt-oss-job
          title: Name
        checkpoint_sync_status:
          anyOf:
            - $ref: '#/components/schemas/CheckpointSyncStatus'
            - type: 'null'
          default: null
          description: Checkpoint sync status of the training job.
        priority:
          default: 0
          description: >-
            Queue priority. Higher values are dequeued first. NULL is treated as
            0.
          title: Priority
          type: integer
        availability_model:
          $ref: '#/components/schemas/V1AvailabilityModel'
          default: dedicated
          description: >-
            Capacity guarantee for the job. 'dedicated' is non-preemptible
            on-demand capacity; 'spot' is interruptible.
        user:
          anyOf:
            - $ref: '#/components/schemas/UserV1'
            - type: 'null'
          default: null
          description: The user who created the training job.
      required:
        - id
        - created_at
        - current_status
        - instance_type
        - updated_at
        - training_project_id
        - training_project
      title: TrainingJobV1
      type: object
    CreateTrainingJobImageV1:
      description: Configuration to create a training job image.
      properties:
        base_image:
          description: Base image for the training job.
          examples:
            - hello-world
          title: Base Image
          type: string
        docker_auth:
          anyOf:
            - $ref: '#/components/schemas/DockerAuthV1'
            - type: 'null'
          default: null
          description: Docker authentication credentials
      required:
        - base_image
      title: CreateTrainingJobImageV1
      type: object
    CreateTrainingJobComputeV1:
      description: Configuration to specify the compute for a training job.
      properties:
        node_count:
          default: 1
          description: Number of nodes for the training job.
          examples:
            - 1
          title: Node Count
          type: integer
        cpu_count:
          default: 1
          description: Number of cpus for the training job.
          examples:
            - 1
          title: Cpu Count
          type: integer
        memory:
          default: 2Gi
          description: Memory for the training job.
          examples:
            - 2Gi
          title: Memory
          type: string
        accelerator:
          anyOf:
            - $ref: '#/components/schemas/CreateTrainingJobAcceleratorV1'
            - type: 'null'
          default: null
          description: GPU specification for the training job
          examples:
            - accelerator: H100
              count: 2
        availability_model:
          $ref: '#/components/schemas/V1AvailabilityModel'
          default: dedicated
          description: >-
            Capacity guarantee for the job. 'dedicated' (the default) runs on
            on-demand capacity that is not preempted. 'spot' runs on
            interruptible capacity that may be preempted; the user is
            responsible for checkpointing their own progress.
          examples:
            - spot
      title: CreateTrainingJobComputeV1
      type: object
    CreateTrainingJobRuntimeV1:
      description: Configuration to specify the runtime environment for a training job.
      properties:
        start_commands:
          description: Commands to execute when starting the runtime.
          examples:
            - - python main.py
          items:
            type: string
          title: Start Commands
          type: array
        environment_variables:
          additionalProperties:
            anyOf:
              - type: string
              - $ref: '#/components/schemas/SecretReferenceV1'
          description: Environment variables to set in the runtime.
          examples:
            - API_KEY: your_api_key_here
              PATH: /usr/bin
          title: Environment Variables
          type: object
        artifacts:
          description: Runtime artifacts for the training job.
          items:
            $ref: '#/components/schemas/CreateTrainingJobS3Artifact'
          title: Artifacts
          type: array
        enable_cache:
          anyOf:
            - type: boolean
            - type: 'null'
          default: null
          description: Deprecated. Use cache_config instead.
          examples:
            - true
          title: Enable Cache
        cache_config:
          anyOf:
            - $ref: '#/components/schemas/CreateTrainingJobCacheConfig'
            - type: 'null'
          default: null
          description: Configuration for the read-write cache.
          examples:
            - enable_legacy_hf_mount: true
              enabled: true
              mount_base_path: /root/.cache
              require_cache_affinity: true
        checkpointing_config:
          $ref: '#/components/schemas/CreateTrainingJobCheckpointingConfig'
          description: Configuration for checkpointing.
          examples:
            - checkpoint_path: /mnt/ckpts
              enabled: true
              volume_size_gib: null
        load_checkpoint_config:
          anyOf:
            - $ref: '#/components/schemas/LoadCheckpointConfig'
            - type: 'null'
          default: null
          description: Configuration for loading checkpoints
      title: CreateTrainingJobRuntimeV1
      type: object
    TrussUserEnv:
      description: >-
        This data models is used to flexibly store info alongside oracle
        versions.

        There is a corresponding data model in the truss client.

        In contrast, here all fields are optional for backwards compatibility
        with old

        clients.
      properties:
        truss_client_version:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          title: Truss Client Version
        python_version:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          title: Python Version
        pydantic_version:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          title: Pydantic Version
        mypy_version:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          title: Mypy Version
        is_library_deployment:
          default: false
          title: Is Library Deployment
          type: boolean
        is_frontend_deployment:
          default: false
          title: Is Frontend Deployment
          type: boolean
        git_info:
          anyOf:
            - $ref: '#/components/schemas/GitInfo'
            - type: 'null'
          default: null
      title: TrussUserEnv
      type: object
    InteractiveSessionConfigV1:
      description: Configuration for interactive debugging sessions on training jobs.
      properties:
        trigger:
          $ref: '#/components/schemas/V1InteractiveSessionTrigger'
          default: on_demand
          description: >-
            When to create the interactive session. 'on_startup' creates on job
            start, 'on_failure' creates on job failure, 'on_demand' bypasses
            automatic session creation.
        timeout_minutes:
          default: 480
          description: Number of minutes before the interactive session times out.
          examples:
            - 480
            - 1440
            - 10080
          title: Timeout Minutes
          type: integer
        session_provider:
          $ref: '#/components/schemas/V1InteractiveSessionProvider'
          default: vs_code
          description: The IDE client for the interactive session.
        auth_provider:
          $ref: '#/components/schemas/V1InteractiveSessionAuthProvider'
          default: github
          description: The authentication provider for the interactive session.
      title: InteractiveSessionConfigV1
      type: object
    CreateJobWeightConfigV1:
      description: >-
        Weight source configuration for MDN (Model Distribution Network).

        Enables training jobs to mount external model weights from HuggingFace,
        S3, GCS, or R2

        via MDN's caching and CSI mounting infrastructure. Weights are mirrored
        once and

        deduplicated across training jobs.
      properties:
        source:
          description: 'Weight source URI. Supported formats: hf://, s3://, gs://, r2://'
          examples:
            - hf://meta-llama/Llama-3-8B@main
            - s3://my-bucket/models/llama
            - gs://my-bucket/models/llama
            - r2://account_id.bucket/models/llama
          title: Source
          type: string
        mount_location:
          description: Path where weights will be mounted in the container
          examples:
            - /app/models/base
            - /models/llama
          title: Mount Location
          type: string
        allow_patterns:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          default: null
          description: File patterns to include (Unix-style shell patterns)
          examples:
            - - '*.safetensors'
              - config.json
          title: Allow Patterns
        ignore_patterns:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          default: null
          description: File patterns to exclude (Unix-style shell patterns)
          examples:
            - - '*.bin'
              - '*.h5'
          title: Ignore Patterns
        auth_secret_name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: >-
            Name of the workspace secret for authentication (e.g., HuggingFace
            token)
          examples:
            - hf_token
            - aws_credentials
          title: Auth Secret Name
        auth:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          default: null
          description: Authentication configuration for the weight source.
          examples:
            - auth_method: CUSTOM_SECRET
              auth_secret_name: hf_token
          title: Auth
      required:
        - source
        - mount_location
      title: CreateJobWeightConfigV1
      type: object
    InstanceTypeV1:
      description: An instance type.
      properties:
        id:
          description: Identifier string for the instance type
          title: Id
          type: string
        name:
          description: Display name of the instance type
          title: Name
          type: string
        memory_limit_mib:
          description: Memory limit of the instance type in Mebibytes
          title: Memory Limit Mib
          type: integer
        millicpu_limit:
          description: CPU limit of the instance type in millicpu
          title: Millicpu Limit
          type: integer
        gpu_count:
          description: Number of GPUs on the instance type
          title: Gpu Count
          type: integer
        gpu_type:
          anyOf:
            - type: string
            - type: 'null'
          description: Type of GPU on the instance type
          title: Gpu Type
        gpu_memory_limit_mib:
          anyOf:
            - type: integer
            - type: 'null'
          description: Memory limit of the GPU on the instance type in Mebibytes
          title: Gpu Memory Limit Mib
      required:
        - id
        - name
        - memory_limit_mib
        - millicpu_limit
        - gpu_count
        - gpu_type
        - gpu_memory_limit_mib
      title: InstanceTypeV1
      type: object
    TrainingProjectSummaryV1:
      description: A summary of a training project.
      properties:
        id:
          description: Unique identifier of the training project.
          title: Id
          type: string
        name:
          description: Name of the training project.
          title: Name
          type: string
      required:
        - id
        - name
      title: TrainingProjectSummaryV1
      type: object
    CheckpointSyncStatus:
      description: Lifecycle state for the checkpoint uploader.
      enum:
        - SYNCING
        - COMPLETED
      title: CheckpointSyncStatus
      type: string
    V1AvailabilityModel:
      description: >-
        Capacity guarantee under which a training job is scheduled.

        ``DEDICATED`` is on-demand capacity that is not preempted (the default).
        ``SPOT`` is

        interruptible capacity that may be preempted; the user is responsible
        for checkpointing

        their own progress. A managed/resumable model where the platform handles

        checkpoint/resume on its own is intentionally not defined yet; it is
        planned for a

        future milestone.
      enum:
        - dedicated
        - spot
      title: V1AvailabilityModel
      type: string
    UserV1:
      description: A user.
      properties:
        email:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Email of the user.
          title: Email
      title: UserV1
      type: object
    DockerAuthV1:
      description: Docker authentication credentials.
      properties:
        registry:
          description: Registry to authenticate with
          title: Registry
          type: string
        auth_method:
          $ref: '#/components/schemas/DockerAuthType'
          description: Method to authenticate with the registry
          examples:
            - GCP_SERVICE_ACCOUNT_JSON
            - AWS_IAM
            - AWS_OIDC
            - GCP_OIDC
            - REGISTRY_SECRET
        gcp_service_account_json_docker_auth:
          anyOf:
            - $ref: '#/components/schemas/GcpServiceAccountJsonDockerAuthV1'
            - type: 'null'
          default: null
          description: GCP service account details for the registry
        aws_iam_docker_auth:
          anyOf:
            - $ref: '#/components/schemas/AwsIamDockerAuthV1'
            - type: 'null'
          default: null
          description: AWS details for the registry
        aws_oidc_docker_auth:
          anyOf:
            - $ref: '#/components/schemas/AwsOidcDockerAuthV1'
            - type: 'null'
          default: null
          description: AWS OIDC details for the registry
        gcp_oidc_docker_auth:
          anyOf:
            - $ref: '#/components/schemas/GcpOidcDockerAuthV1'
            - type: 'null'
          default: null
          description: GCP OIDC details for the registry
        registry_secret_docker_auth:
          anyOf:
            - $ref: '#/components/schemas/RegistrySecretDockerAuthV1'
            - type: 'null'
          default: null
          description: >-
            Required when auth_method is REGISTRY_SECRET. Supports any Docker
            registry (Docker Hub, GHCR, NGC, etc.) via username:password
            credentials stored as a Baseten secret.
      required:
        - registry
        - auth_method
      title: DockerAuthV1
      type: object
    CreateTrainingJobAcceleratorV1:
      properties:
        accelerator:
          description: GPU type for the training job.
          examples:
            - H100
          title: Accelerator
          type: string
        count:
          description: GPUs needed for the training job.
          examples:
            - 2
          title: Count
          type: integer
      required:
        - accelerator
        - count
      title: CreateTrainingJobAcceleratorV1
      type: object
    SecretReferenceV1:
      properties:
        name:
          description: Name of the secret to reference.
          examples:
            - hf_token
          title: Name
          type: string
      required:
        - name
      title: SecretReferenceV1
      type: object
    CreateTrainingJobS3Artifact:
      properties:
        s3_bucket:
          description: S3 bucket for the uploaded runtime artifact.
          examples:
            - my-s3-bucket
          title: S3 Bucket
          type: string
        s3_key:
          description: S3 key for the uploaded runtime artifact.
          examples:
            - my-s3-key
          title: S3 Key
          type: string
      required:
        - s3_bucket
        - s3_key
      title: CreateTrainingJobS3Artifact
      type: object
    CreateTrainingJobCacheConfig:
      properties:
        enable_legacy_hf_mount:
          default: false
          description: Whether to enable the legacy Hugging Face cache.
          examples:
            - true
          title: Enable Legacy Hf Mount
          type: boolean
        enabled:
          default: false
          description: Whether to enable the read-write cache.
          examples:
            - true
          title: Enabled
          type: boolean
        require_cache_affinity:
          default: true
          description: >-
            Whether to require region affinity for the read-write cache. If
            False, the resulting job is not guaranteed to be deployed alongside
            the previous cache.
          examples:
            - true
            - false
          title: Require Cache Affinity
          type: boolean
        mount_base_path:
          default: /root/.cache
          description: >-
            Mount base path for the cache directory. The project cache and team
            cache will be mounted under this path.
          examples:
            - /workspace/.cache
            - /root/.cache
          title: Mount Base Path
          type: string
      title: CreateTrainingJobCacheConfig
      type: object
    CreateTrainingJobCheckpointingConfig:
      properties:
        enabled:
          default: false
          description: Whether checkpointing is enabled.
          examples:
            - true
          title: Enabled
          type: boolean
        checkpoint_path:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: path where checkpoints will be saved.
          examples:
            - /mnt/ckpts
          title: Checkpoint Path
        volume_size_gib:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: >-
            Size of the volume in gibibytes. If not provided, the default size
            will be used
          examples:
            - 10
          title: Volume Size Gib
      title: CreateTrainingJobCheckpointingConfig
      type: object
    LoadCheckpointConfig:
      properties:
        enabled:
          default: false
          description: Whether checkpoint loading is enabled
          title: Enabled
          type: boolean
        download_folder:
          default: /tmp/loaded_checkpoints
          description: Folder where checkpoints will be downloaded
          title: Download Folder
          type: string
        checkpoints:
          description: List of checkpoint configurations
          items:
            discriminator:
              mapping:
                baseten_latest_checkpoint:
                  $ref: '#/components/schemas/BasetenLatestCheckpointConfig'
                baseten_named_checkpoint:
                  $ref: '#/components/schemas/BasetenNamedCheckpointConfig'
                loops_checkpoint:
                  $ref: '#/components/schemas/LoopsCheckpointConfig'
              propertyName: typ
            oneOf:
              - $ref: '#/components/schemas/BasetenLatestCheckpointConfig'
              - $ref: '#/components/schemas/BasetenNamedCheckpointConfig'
              - $ref: '#/components/schemas/LoopsCheckpointConfig'
          title: Checkpoints
          type: array
      title: LoadCheckpointConfig
      type: object
    GitInfo:
      properties:
        latest_commit_sha:
          title: Latest Commit Sha
          type: string
        latest_tag:
          anyOf:
            - type: string
            - type: 'null'
          title: Latest Tag
        commits_since_tag:
          anyOf:
            - type: integer
            - type: 'null'
          title: Commits Since Tag
        has_uncommitted_changes:
          title: Has Uncommitted Changes
          type: boolean
      required:
        - latest_commit_sha
        - latest_tag
        - commits_since_tag
        - has_uncommitted_changes
      title: GitInfo
      type: object
    V1InteractiveSessionTrigger:
      enum:
        - on_startup
        - on_failure
        - on_demand
      title: V1InteractiveSessionTrigger
      type: string
    V1InteractiveSessionProvider:
      enum:
        - vs_code
        - cursor
        - ssh
      title: V1InteractiveSessionProvider
      type: string
    V1InteractiveSessionAuthProvider:
      enum:
        - github
        - microsoft
      title: V1InteractiveSessionAuthProvider
      type: string
    DockerAuthType:
      enum:
        - GCP_SERVICE_ACCOUNT_JSON
        - AWS_IAM
        - AWS_OIDC
        - GCP_OIDC
        - REGISTRY_SECRET
      title: DockerAuthType
      type: string
    GcpServiceAccountJsonDockerAuthV1:
      description: GCP details for the registry.
      properties:
        service_account_json_secret_ref:
          $ref: '#/components/schemas/SecretReferenceV1'
          description: Name of the service account secret
      required:
        - service_account_json_secret_ref
      title: GcpServiceAccountJsonDockerAuthV1
      type: object
    AwsIamDockerAuthV1:
      description: AWS details for the registry.
      properties:
        access_key_secret_ref:
          $ref: '#/components/schemas/SecretReferenceV1'
          description: Name of the access key secret
        secret_access_key_secret_ref:
          $ref: '#/components/schemas/SecretReferenceV1'
          description: Name of the secret key secret
      required:
        - access_key_secret_ref
        - secret_access_key_secret_ref
      title: AwsIamDockerAuthV1
      type: object
    AwsOidcDockerAuthV1:
      description: AWS OIDC details for the registry.
      properties:
        role_arn:
          description: AWS IAM role ARN for OIDC authentication
          title: Role Arn
          type: string
        region:
          description: AWS region for OIDC authentication
          title: Region
          type: string
      required:
        - role_arn
        - region
      title: AwsOidcDockerAuthV1
      type: object
    GcpOidcDockerAuthV1:
      description: GCP OIDC details for the registry.
      properties:
        service_account:
          description: GCP service account name for OIDC authentication
          title: Service Account
          type: string
        workload_identity_provider:
          description: GCP workload identity provider for OIDC authentication
          title: Workload Identity Provider
          type: string
      required:
        - service_account
        - workload_identity_provider
      title: GcpOidcDockerAuthV1
      type: object
    RegistrySecretDockerAuthV1:
      description: >-
        Authentication via a Baseten secret for any Docker registry (Docker Hub,
        GHCR, NGC, etc.).

        The referenced secret must contain credentials in the format
        'username:password'.

        For Docker Hub, set registry to 'https://index.docker.io/v1/'. For GHCR,
        use 'ghcr.io'.
      properties:
        secret_ref:
          $ref: '#/components/schemas/SecretReferenceV1'
          description: >-
            Reference to a Baseten secret containing credentials in the format
            'username:password'
      required:
        - secret_ref
      title: RegistrySecretDockerAuthV1
      type: object
    BasetenLatestCheckpointConfig:
      properties:
        project_name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Name of the project to load the checkpoint from
          title: Project Name
        job_id:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: ID of the job to load the checkpoint from
          title: Job Id
        typ:
          const: baseten_latest_checkpoint
          default: baseten_latest_checkpoint
          title: Typ
          type: string
      title: BasetenLatestCheckpointConfig
      type: object
    BasetenNamedCheckpointConfig:
      properties:
        checkpoint_name:
          description: Name of the checkpoint to load from
          title: Checkpoint Name
          type: string
        project_name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Name of the project to load the checkpoint from
          title: Project Name
        job_id:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: ID of the job to load the checkpoint from
          title: Job Id
        typ:
          const: baseten_named_checkpoint
          default: baseten_named_checkpoint
          title: Typ
          type: string
      required:
        - checkpoint_name
      title: BasetenNamedCheckpointConfig
      type: object
    LoopsCheckpointConfig:
      properties:
        run_id:
          description: ID of the Loops run to load the checkpoint from
          title: Run Id
          type: string
        checkpoint_name:
          description: Name of the checkpoint to load
          title: Checkpoint Name
          type: string
        target:
          default: trainer
          description: >-
            Which checkpoint target to load: 'trainer' (full training state) or
            'sampler' (inference weights)
          enum:
            - trainer
            - sampler
          title: Target
          type: string
        typ:
          const: loops_checkpoint
          default: loops_checkpoint
          title: Typ
          type: string
      required:
        - run_id
        - checkpoint_name
      title: LoopsCheckpointConfig
      type: object
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Send `Authorization: Bearer <api_key>`. The legacy `Authorization:
        Api-Key <api_key>` scheme is also accepted.

````

---
Part of [[Training Api (Reference)]]
