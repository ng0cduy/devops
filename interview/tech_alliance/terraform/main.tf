resource "helm_release" "s3_sync_service" {
  name       = var.release_name
  chart      = "${path.module}/../helm/s3-sync-service"
  namespace  = var.namespace
  create_namespace = true

  values = [
    yamlencode(var.settings)
  ]
  wait = true
}
