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
    alias = "zone1"          //used for multi region
    region = "ap-southeast-2"
    secret_key = "secret_key" //username
    access_key = "access_key" //password
}

provider "aws" { // must be the same as the above required_providers
    alias = "zone2"          //used for multi region
    region = "ap-southeast-2"
    secret_key = "secret_key" //username
    access_key = "access_key" //password
}

resource "aws_instance" "ec2-1" {
    provider = aws.zone1
    ami = "ami-12345678" // replace with a valid AMI ID
    instance_type = "t2.micro"

}