# Terraform file for configuration of instace in AWS account 
# access_key & secrey_key are modified for security reason. 

provider "aws" {
  access_key = "AKIAJ4UVY6RXXXXAHFKQ"
  secret_key = "KoE+lGl385gg+PcT9VHxxxxS76V7yZycY138Tl13"
  region     = "us-east-2"
}

resource "aws_instance" "example" {
  ami           = "ami-0b1e356e"
  instance_type = "t2.micro"
}