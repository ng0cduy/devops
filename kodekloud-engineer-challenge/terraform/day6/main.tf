resource "aws_eip" "eip" {
  domain = "vpc"
  # Use the 'tags' block to assign a name and other metadata
  tags = {
    Name = "nautilus-eip"
  }
}
