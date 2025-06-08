terraform {
  required_providers {
    aws = { // can be aws or aws_provider
        source = "hasicorp/aws"
        version = "5.73.0"
    }
  }
  backend "s3" {
    bucket = "value"
    key = "state/terraform.tfstate"
    region = "ap-southeast-2"
  }
}