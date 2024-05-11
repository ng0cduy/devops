terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "ap-southeast-1"
}

resource "aws_instance" "app_server" {
  ami                    = "ami-0a95d2cc973f39afc"
  instance_type          = "t2.micro"
  vpc_security_group_ids = ["sg-01cdc52ba27e12d87"]
  subnet_id              = "subnet-083ca3b885fe6c1cd"
  tags = {
    Name          = var.instance_name
    Owner         = "DevopsEnigneer"
    ApplicationID = "Terraform"
    Environment   = "DEVELOPMENT"
  }
}
