# S3 Sync Service Deployment

This project contains the solution for deploying a containerized service that syncs data from S3, compresses it, and serves it via Nginx. The solution includes Docker automation, a parametrized Helm chart, and a Terraform module for deployment to EKS.

## Project Structure

- `docker/`: Contains the Dockerfile and automation script.
- `helm/`: Contains the Helm chart `s3-sync-service`.
- `terraform/`: Contains the Terraform module to deploy the Helm chart.

## Prerequisites

- Docker
- AWS CLI
- Terraform
- kubectl
- An existing EKS cluster
- An S3 bucket with data to sync

## Part 1: Docker Image

The Docker image is based on `nginx:alpine` and includes the AWS CLI.
The entrypoint script (`script.sh`) performs the following:
1. Syncs data from the S3 bucket specified by `S3_BUCKET` env var.
2. Compresses the data into `backup.tar.gz`.
3. Starts Nginx to serve the file.

### Build and Push

```bash
cd docker
docker build -t <your-registry>/s3-sync-service:latest .
docker push <your-registry>/s3-sync-service:latest
```

## Part 2: Helm Chart

The Helm chart deploys the application with the following requirements:
- **Replicas**: Configurable via `replicaCount`.
- **Anti-Affinity**: Pods are scheduled on different nodes using `podAntiAffinity` with `requiredDuringSchedulingIgnoredDuringExecution`.
- **Node Selector**: Pods are scheduled only on nodes labeled `test-nodes: true`.

### Key Values (`values.yaml`)

- `replicaCount`: Number of replicas (default: 3).
- `s3Bucket`: The S3 bucket name.
- `nodeSelector`: `{ test-nodes: "true" }`.
- `ingress`: Configured for `copilot.tecalliance.net`.

## Part 3: Terraform Deployment

The Terraform module deploys the Helm chart to an existing EKS cluster.

### Usage

1. Initialize Terraform:
   ```bash
   cd terraform
   terraform init
   ```

2. Create a `terraform.tfvars` file or pass variables via command line:
   ```hcl
   cluster_name     = "my-eks-cluster"
   region           = "us-east-1"
   image_repository = "<your-registry>/s3-sync-service"
   image_tag        = "latest"
   s3_bucket        = "my-data-bucket"
   ```

3. Apply the configuration:
   ```bash
   terraform apply
   ```

## IAM Policies

The Pods need permission to read from the S3 bucket. This should be provided via an IAM Role for Service Accounts (IRSA) or the Node Instance Role.

**Required Policy:**

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::<your-bucket-name>",
                "arn:aws:s3:::<your-bucket-name>/*"
            ]
        }
    ]
}
```

If using IRSA, annotate the ServiceAccount in `values.yaml`:

```yaml
serviceAccount:
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::<account-id>:role/<role-name>
```

## Accessing the Service

Once deployed, the service will be available at `http://copilot.tecalliance.net` (assuming DNS is configured to point to the Ingress Controller).
You can download the backup at `http://copilot.tecalliance.net/backup.tar.gz`.
