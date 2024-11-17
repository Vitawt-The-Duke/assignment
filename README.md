
# BloxRoute Repository

## Overview

This repository contains solutions to three take-home assignments that cover a range of topics, including Terraform, AWS, Ethereum client monitoring, and Fluentd log management. Each assignment focuses on a specific technical area, with detailed implementation steps and supporting files.

---

## Repository Structure

```
BloxRoute/
├── evidence/                  # Screenshots and logs for completed tasks
│   ├── assignment_1/          # Evidence for Assignment 1
│   ├── assignment_2/          # Evidence for Assignment 2
│   └── assignment_3/          # Evidence for Assignment 3
├── fluentd/                   # Files related to Fluentd configuration (Assignment 3)
│   ├── group_vars/
│   ├── host_vars/
│   ├── roles/                 # Ansible roles for Fluentd management
│   ├── ansible.cfg
│   ├── denylist.txt           # Deny list file for Fluentd filtering
│   └── inventory/             # Ansible inventory
│       └── main.yml
├── geth_and_lighthouse/       # Files related to Ethereum client monitoring (Assignment 2)
│   ├── Dockerfile
│   ├── health.py              # API service for monitoring Ethereum nodes
│   ├── Makefile
│   ├── requirements.txt       # Dependencies for the Python API service
│   └── test_health.py         # Unit tests for the API service
├── terraform/                 # Terraform files (Assignment 1)
│   ├── main.tf
│   ├── outputs.tf
│   ├── provider.tf
│   ├── variables.tf           # Configuration variables for Terraform
│   └── terraform.tfstate      # Terraform state file (not included in version control)
|---ASSIGNMENT.md              # Documentation for Assignment 1 extra part
├── ASSIGNMENT1.md             # Documentation for Assignment 1 extra part
├── ASSIGNMENT2.md             # Documentation for Assignment 2
├── ASSIGNMENT3.md             # Documentation for Assignment 3
└── README.md                  # This file
```

---

## Assignments Overview

### **Assignment 1: Terraform and AWS**

- **Objective**: Deploy an Nginx server on AWS using Terraform.
- **Steps**:
  1. Install Terraform and configure AWS CLI.
  2. Define and customize variables in `variables.tf`.
  3. Run `terraform init`, `terraform plan`, and `terraform apply` to provision resources.
  4. Verify the deployment by accessing the Nginx welcome page.
- **Evidence**: Screenshots and logs are stored in the `evidence/assignment_1/` folder.

---

### **Assignment 2: API Service for Node Status**

- **Objective**: Build an API service to monitor Ethereum client (Geth and Lighthouse) health and metrics.
- **Key Components**:
  - Ethereum clients setup using [eth-docker](https://github.com/eth-educators/eth-docker).
  - Python-based health API to monitor Geth and Lighthouse nodes.
- **Endpoints**:
  - `/status`: Checks node health.
  - `/height`: Fetches the current block height.
  - `/peers`: Displays the number of peers connected.
  - `/all`: Consolidates all metrics in one response.
- **How to Run**:
  - Install dependencies: `pip install -r requirements.txt`.
  - Run locally: `python health.py` or use Docker (`make build`, `make docker-run`).
  - Run tests: `make test`.
- **Evidence**: Logs and screenshots stored in `evidence/assignment_2/`.

---

### **Assignment 3: Linux, Ansible, and Fluentd**

- **Objective**: Use Ansible to install and configure Fluentd for handling Nginx logs.
- **Tasks**:
  1. Install Fluentd and configure it to process Nginx access and error logs.
  2. Implement filtering based on a deny list and route excluded logs to `denylist_audit.log`.
  3. Configure log rotation to retain logs for 7 days.
- **How to Run**:
  - Run specific Ansible tasks using tags: `cleanup`, `install`, `configure`, `logrotate`.
- **Evidence**: Logs, screenshots, and deny list stored in `evidence/assignment_3/`.

---

## How to Use This Repository

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd BloxRoute
   ```
2. Follow the individual assignment instructions in `ASSIGNMENT1.md`, `ASSIGNMENT2.md`, and `ASSIGNMENT3.md`.
3. Check the `evidence/` folder for task outputs and logs.

---

## Notes

- This repository demonstrates a range of skills in infrastructure automation, application monitoring, and log management.
- Security considerations are documented for each assignment to distinguish between development and production practices.
