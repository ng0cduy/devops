variable "cluster_name" {
  description = "The name of the pre-existing EKS cluster"
  type        = string
}

variable "region" {
  description = "AWS Region where the cluster is located"
  type        = string
  default     = "us-east-1"
}

variable "namespace" {
  description = "Kubernetes namespace to deploy the service to"
  type        = string
  default     = "s3-sync-app"
}

variable "image_repository" {
  description = "The Docker image repository URL"
  type        = string
}

variable "image_tag" {
  description = "The Docker image tag"
  type        = string
  default     = "latest"
}

variable "s3_bucket" {
  description = "The name of the S3 bucket to sync data from"
  type        = string
}

variable "replica_count" {
  description = "Number of replicas for the deployment"
  type        = number
  default     = 3
}
