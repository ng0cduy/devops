resource "aws_vpc" "devops_vpc" {
  cidr_block = "192.168.0.0/24"

  tags = {
    Name = "devops-vpc"
  }
}
