# Assignment 1: Terraform and AWS

## Steps to Deploy

1. Ensure you have Terraform installed: https://www.terraform.io/downloads
2. Configure AWS CLI with credentials: `aws configure` or `export AWS_PROFILE=$MYPROFILENAME`
3. Clone this repository and navigate to the `terraform/` directory.
4. Required configuration variables or files (you may customize it) descibed in `terraform/variables.tf` file.
5. Run:
   ```bash
   terraform init
   terraform plan
   terraform apply --auto-approve
   ```
6. Testing:
   After deployment, Terraform will output the nginx_server_public_ip.
   Verify that Nginx is installed and running using one of the following methods:

   Using Curl:
   ```bash
   curl http://<nginx_server_public_ip>
   ```
   You should see the Nginx default welcome page content.

   Using a Browser:
   Open a browser and navigate to http://<nginx_server_public_ip>.
   You should see the Nginx welcome page.