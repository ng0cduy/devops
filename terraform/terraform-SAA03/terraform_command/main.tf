terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.5.0"
    }
  }
}

provider "aws" {
  # Configuration options
  region = "ap-southeast-1"
}

resource "aws_instance" "myEC2Instance" {
    ami = "ami-123456"
    instance_type = "t3.medium"
    key_name = "my_key_pair"
    tags = {
        Name = "MyEC2Instance"
    }
}