variable "instance_type" {
  default = "t2.micro"
  description = "EC2 instance type"
}

variable "key_name" {
  default = "test_blox"
  description = "Name of the AWS key pair"
}

variable "ami_id" {
  default = "ami-0a422d70f727fe93e" # Ubuntu 22.04 LTS for eu-west-1
  description = "AMI ID for Ubuntu 22.04"
}

variable "pub_key_path" {
  default = "~/.ssh/id_ed25519.pub"
}