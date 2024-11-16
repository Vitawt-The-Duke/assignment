output "nginx_server_public_ip" {
  value = aws_instance.nginx.public_ip
  description = "Public IP of the Nginx server"
}
