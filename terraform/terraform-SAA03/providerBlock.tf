terraform {
  required_providers {
    //terraform registry
    aws = {
        source = "hashicorp/aws"
        version = "5.73.0"
    }
  }
}

provider "aws" { // must be the same as the above required_providers
    region = "ap-southeast-2"
    secret_key = "secret_key" //username
    access_key = "access_key" //password
}