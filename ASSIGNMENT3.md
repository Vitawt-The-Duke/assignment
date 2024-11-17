readme_content = """
# Take-Home Assignment 3: Linux, Ansible, and Fluentd

## Task Overview

This assignment uses Ansible to install, configure, and manage Fluentd for handling Nginx logs. It includes the following tasks:

### Tasks
1. **Installation and Configuration (10 pts)**:
   - Install Fluentd using Ansible.
   - Configure Fluentd to process logs from Nginx access and error logs.
2. **Filtering and Routing (7 pts)**:
   - Implement filtering to exclude logs based on a deny list (`denylist.txt`).
   - Route filtered logs to a separate file `denylist_audit.log`.
3. **Documentation (3 pts)**:
   - Document setup steps, commands, and screenshots in this README.
4. **Extra Credit (5 pts)**:
   - Implement log rotation for Fluentd logs to retain only 7 days' worth of logs.

---

## Instructions

### Prerequisites
1. Install Ansible on your control node.
2. Ensure SSH access to target hosts.
3. Place the playbook and roles in your Ansible project directory.

---

## Playbook Overview

### Playbook: `main.yml`
This playbook contains the following tagged tasks:

```yaml
- name: Cleanup Fluentd
  hosts: all
  become: true
  roles:
    - cleanup_fluentd
  tags: cleanup

- name: Install Fluentd
  hosts: all
  become: true
  roles:
    - install_fluentd
  tags: install

- name: Configure Fluentd
  hosts: all
  become: true
  roles:
    - configure_fluentd
  tags: configure

- name: Configure logrotate
  hosts: all
  become: true
  roles:
    - logrotate_fluentd
  tags: logrotate
```

### Running Specific Tasks

You can use tags to run specific tasks:

Cleanup Fluentd: `ansible-playbook main.yml --tags cleanup`
Install Fluentd: `ansible-playbook main.yml --tags install`
Configure Fluentd: `ansible-playbook main.yml --tags configure`
Configure Logrotate: `ansible-playbook main.yml --tags logrotate`

**Role Descriptions**

1. Cleanup Fluentd
Removes existing Fluentd installations and related files:
Stops the service.
Deletes configuration and log directories.

2. Install Fluentd
Installs dependencies.
Installs Fluentd as a Ruby gem.
Sets up a systemd service for Fluentd.

3. Configure Fluentd

Configures Fluentd to:

Collect logs from /var/log/nginx/access.log and /var/log/nginx/error.log.
Apply filtering based on a deny list.
Route logs to appropriate files.
Dynamically updates pattern in the Fluentd configuration:

```bash
patterns=$(paste -sd '|' /etc/fluent/denylist.txt)
sed -i "s@pattern_file.*@pattern \"$patterns\"@" /etc/fluent/fluentd.conf
```

4. Configure Logrotate

Manages log rotation for Fluentd logs:

Logrotate configuration:

```bash
/var/log/fluent/*.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0640 <user> adm
    sharedscripts
    postrotate
        systemctl reload fluentd > /dev/null 2>&1 || true
    endscript
}
```

### Extra Credit: Log Rotation

The log rotation role ensures:

Daily log rotation.
Retention of the last 7 days of logs.
Compression of older logs.


Notes
Ensure the deny list (`denylist.txt`) contains valid patterns for exclusion.
Validate the Fluentd configuration after each update to prevent service disruptions.
