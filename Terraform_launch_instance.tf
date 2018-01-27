# Terraform file for configuration of instace in AWS account 
# access_key & secrey_key are modified for security reason. 

provider "aws" {
  access_key = "MYACCESSKEY"
  secret_key = "MYSECRETKEY"
  region     = "us-east-2"
}

resource "aws_instance" "example" {
  ami           = "MY-AMI"
  instance_type = "t2.micro"
}
