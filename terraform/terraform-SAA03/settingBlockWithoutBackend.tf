terraform {
  required_providers {
    aws = { // can be aws or aws_provider
        source = "hasicorp/aws"
        version = "5.73.0"
    }
  }
}