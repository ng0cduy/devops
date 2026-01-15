output "helm_release_name" {
  description = "The name of the Helm release"
  value       = helm_release.s3_sync_service.name
}

output "helm_release_status" {
  description = "The status of the Helm release"
  value       = helm_release.s3_sync_service.status
}

output "service_namespace" {
  description = "The namespace where the service is deployed"
  value       = helm_release.s3_sync_service.namespace
}
