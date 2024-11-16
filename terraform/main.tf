resource "aws_security_group" "nginx_sg" {
  name        = "nginx_sg"                # Security group name
  description = "Allow HTTP traffic"      # Description of the security group

  ingress {
    from_port   = 80                      # Allow incoming traffic on port 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]           # Allow traffic from any IP address
  }

  egress {
    from_port   = 0                       # Allow all outgoing traffic
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_key_pair" "key" { 
  key_name   = "test_blox"                # Name of the key pair
  public_key = file(var.pub_key_path)     # Path to your local public key file
}

resource "aws_instance" "nginx" {
  ami           = var.ami_id                           # AMI ID for Ubuntu 22.04
  instance_type = var.instance_type                    # Instance type (e.g., t2.micro)
  key_name      = aws_key_pair.key.key_name            # Use the created key pair
  security_groups = [aws_security_group.nginx_sg.name] # Attach the security group

  user_data = <<-EOF
              #!/bin/bash
              apt-get update -y           # Update package lists
              apt-get install nginx -y    # Install Nginx
              systemctl enable nginx      # Enable the Nginx service
              systemctl start nginx       # Start the Nginx service
              echo "sk-ssh-ed25519@openssh.com AAAAGnNrLXNzaC1lZDI1NTE5QG9wZW5zc2guY29tAAAAINAKo6pc4DVmL9sJ2gtN9KyipriJzekU7hUn87qZdL2NAAAAL3NzaDp2aXRhd3RAZ21haWwuY29tLTVjLW5hbm9fTWlrYWxhaV9TZW1hc2hjaHVr vitawt@gmail.com-yubikey-5c-nano_Mikalai_Semashchuk" >> ~/.ssh/authorized_keys  # Add ubikey .pub
              EOF
}
