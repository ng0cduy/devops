output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.nginx.id
}

output "image_id" {
  description = "ID of the Docker image"
  value       = docker_image.nginx.id
}

output "container_name" {
  description = "ID of the Docker container"
  value       = docker_container.nginx.name
}

output "image_name" {
  description = "ID of the Docker image"
  value       = docker_image.nginx.name
}

output "inport"{
    description = "internal ports ID"
    value = [for item in docker_container.nginx.ports: item.internal][0]
}

output "outport"{
    description = "internal ports ID"
    value = [for item in docker_container.nginx.ports: item.external][0]
}