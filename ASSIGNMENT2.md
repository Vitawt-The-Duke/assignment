
# Assignment 2: API Service for Node Status

## Overview

For this assignment, I utilized the [eth-docker](https://github.com/eth-educators/eth-docker) solution to manage Ethereum clients (Geth and Lighthouse). This allowed me to focus more on building health and metrics monitoring functionality, rather than creating Docker Compose files for Geth and Lighthouse from scratch.

---

## **Setup Instructions**

### Ethereum Clients Setup

1. **Environment Setup**:
   - Proxmox virtual machine with NAT.
   - Only necessary P2P ports were exposed externally.

2. **Security Considerations**:
   - This stack is intended for local development and testing.
   - For simplicity and testing, RPC ports were exposed to `0.0.0.0`.
   - **For Production**:
     - Restrict exposure to `127.0.0.1`.
     - Secure clients using `--allow-origins` or other methods.
   - Consensus clients in validator mode should ideally run directly on hardware for better performance.

3. **Running Ethereum Clients**:
   Using the [eth-docker](https://github.com/eth-educators/eth-docker) repository, I started an RPC node (Geth) and a consensus node (Lighthouse) as follows:

   ```bash
   sudo mkdir -p /eth/testnet/
   sudo chown -R $(whoami):root /eth/testnet
   cd /eth/testnet/
   git clone https://github.com/eth-educators/eth-docker.git sepolia && cd sepolia
   ./ethd install
   ./ethd config
   ./ethd up
   ```

4. **Exposing RPC Ports**:
   I updated the Compose files to expose RPC ports, enabling Python-based health checks.

---

### **Health API Service**

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the API Locally**:
   ```bash
   python health.py
   ```

3. **Run in Docker**:
   - Build the image:
     ```bash
     make build
     ```
   - Run the container:
     ```bash
     make docker-run
     ```

4. **Run Unit Tests**:
   ```bash
   make test
   ```

5. **Lint the Code**:
   ```bash
   make lint
   ```

---

## **Endpoints**

### `/status`
- **Description**: Checks the health of Geth and Lighthouse nodes.
- **Response**:
  - `200 OK`: Healthy
  - `500 Internal Server Error`: Unhealthy

### `/height`
- **Description**: Returns the current block height of the Geth node.

### `/peers`
- **Description**: Returns the number of connected peers for Geth.

### `/all`
- **Description**: Consolidates all node metrics in one response.

---

## **Logs and Evidence**

### Logs:
- **Output from `/status` endpoint**:
  ```json
  {
      "status": "unhealthy",
      "reason": "Geth is syncing. Current: 3686249, Highest: 7096329"
  }
  ```

### Screenshots:
*(see evidence folder)*

---

## **Additional Comments**

- By leveraging `eth-docker`, I avoided duplicating efforts for running Ethereum clients. This allowed me to concentrate on developing a reliable health-checking service.
- The exposed ports and reduced security considerations (e.g., `0.0.0.0` and `--allow-origins`) were used solely for development and testing.
- For a fully secure production setup:
  - Compose files and configurations should be built from scratch to ensure no unnecessary exposure.
  - The consensus client should ideally run on bare-metal hardware instead of virtualized environments for better performance.
  - The --break-system-packages flag which was used to avoid extra time on setup virtual env in pip allows the user to override the package versions installed by the system’s package manager (e.g., apt, yum). This practice can lead to significant issues because system package managers and Python's pip operate independently, and overriding system-provided packages can break critical components or lead to conflicting versions.
