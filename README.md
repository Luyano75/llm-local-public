# LLM Local Deployment with Ansible

This repository provides a set of Ansible playbooks to provision a Linux server and deploy Ollama for local LLM (Large Language Model) execution. It includes tasks for system hardening, Docker installation, and Ollama configuration.

## Architecture

The project consists of several Ansible playbooks:
- `provision.yml`: Prepares the base system (updates, common tools, Docker, IPv6 disabling).
- `install_llm.yml`: Installs Ollama using the official installer script and configures it.
- `install_llm_manual.yml`: Performs a manual, clean installation of Ollama from binaries.
- `reboot.yml`: A simple utility to reboot the remote server.
- `test_ollama.py`: A Python script to verify the deployment by sending a test prompt to the API.

## Prerequisites

- A Linux server (Ubuntu recommended) with SSH access.
- Ansible installed on your local machine.
- Python 3 and the `requests` library (for the test script).

## Installation Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/llm-local.git
   cd llm-local
   ```

2. Configure your inventory:
   Edit `inventory.ini` and replace the placeholders with your server's IP and username.

3. Run the provisioning playbook:
   ```bash
   ansible-playbook -i inventory.ini provision.yml
   ```

4. Install Ollama:
   You can either use the official script:
   ```bash
   ansible-playbook -i inventory.ini install_llm.yml
   ```
   Or the manual installation:
   ```bash
   ansible-playbook -i inventory.ini install_llm_manual.yml
   ```

## Configuration

### Ansible Variables
Variables such as `ansible_user` and `ansible_host` are defined in `inventory.ini`.

### Python Test Script
The `test_ollama.py` script uses environment variables for configuration. You can use a `.env` file or export them directly:

- `OLLAMA_HOST`: The IP or hostname of your LLM server (default: `localhost`).
- `OLLAMA_PORT`: The port Ollama is listening on (default: `11434`).
- `OLLAMA_MODEL`: The model to use for testing (default: `phi3:mini`).

Example:
```bash
export OLLAMA_HOST=192.168.1.26
python3 test_ollama.py
```

## Security Considerations

- **External Access**: The playbooks configure Ollama to listen on `0.0.0.0`. Ensure your server's firewall (e.g., UFW) restricts access to port 11434 to authorized IPs only.
- **SSH Access**: It is recommended to use SSH keys rather than passwords for Ansible authentication.
- **IPv6**: These playbooks disable IPv6 system-wide for network stability in certain environments. Remove these tasks from `provision.yml` if IPv6 is required.

