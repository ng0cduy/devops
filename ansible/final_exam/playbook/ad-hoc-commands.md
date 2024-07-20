# Q1
### Ensure users exist
ansible dbsystems -m ansible.builtin.user -a "name=supervisor home=/home/supervisor state=present group=supervisor" -b

ansible dbsystems -m ansible.builtin.user -a "name=consultant home=/home/consultant state=present group=consultant" -b

### Create .ssh directory for users
ansible dbsystems -m ansible.builtin.file -a "path=/home/supervisor/.ssh state=directory mode=0755 owner=supervisor group=supervisor" -b

ansible dbsystems -m ansible.builtin.file -a "path=/home/consultant/.ssh state=directory mode=0755 owner=consultant group=consultant" -b

### Copy authorized key for users from localhost
ansible dbsystems -m ansible.builtin.copy -a "src=/home/ansible/keys/supervisor/authorized_keys dest=/home/supervisor/.ssh/authorized_keys owner=supervisor group=supervisor mode=0600" -b

ansible dbsystems -m ansible.builtin.copy -a "src=/home/ansible/keys/consultant/authorized_keys dest=/home/consultant/.ssh/authorized_keys owner=consultant group=consultant mode=0600" -b

### Install auditd
ansible dbsystems,localhost -m ansible.builtin.dnf -a "name=audit state=present" -b

### Ensure auditd service is enabled and started
ansible dbsystems,localhost -m ansible.builtin.service -a "name=auditd state=started enabled=yes" -b

# Q2

### Ensure the user exists
ansible dbsystems -m ansible.builtin.user -a "name=linuxthi home=/home/linuxthi state=present group=linuxthi" -b

### Ensure the user can run sudo commands without a password
ansible dbsystems -m ansible.builtin.shell -a "echo 'linuxthi ALL=(ALL) NOPASSWD: ALL' | sudo tee -a /etc/sudoers && sudo visudo -cf /etc/sudoers" -b

### Verify the sudoers file
ansible dbsystems -m ansible.builtin.command -a "visudo -cf /etc/sudoers" -b

# Q3

## Install httpd and unzip
ansible dbsystems -m ansible.builtin.yum -a "name=httpd state=present" -b
ansible dbsystems -m ansible.builtin.yum -a "name=unzip state=present" -b

## Ensure httpd is running
ansible dbsystems -m ansible.builtin.service -a "name=httpd state=started enabled=yes" -b

## Download website zip file
ansible dbsystems -m ansible.builtin.get_url -a "url=https://drive.google.com/uc?id=1OGzCR0UG6qNZcOJmyuyptnR4HmUC_wjp&export=download dest=/tmp/website.zip mode=644" -b

## Ensure document root exists
ansible dbsystems -m ansible.builtin.file -a "path=/var/www/html state=directory mode=755" -b

## Ensure destination directory exists
ansible dbsystems -m ansible.builtin.file -a "path=/tmp/unarchive_folder state=directory" -b

## Unzip the zip file
ansible dbsystems -m ansible.builtin.unarchive -a "src=/tmp/website.zip dest=/tmp/unarchive_folder remote_src=yes" -b

## Copy website files to /var/www/html
ansible dbsystems -m ansible.builtin.shell -a "cp -r /tmp/unarchive_folder/* /var/www/html" -b

## Set proper ownership and permission
ansible dbsystems -m ansible.builtin.file -a "path=/var/www/html owner=apache group=apache mode=0755" -b

## Restart httpd service
ansible dbsystems -m ansible.builtin.systemd -a "name=httpd state=restarted" -b

## Delete specific folder and its contents in /tmp
ansible dbsystems -m ansible.builtin.file -a "path=/tmp/website.zip state=absent" -b
ansible dbsystems -m ansible.builtin.file -a "path=/tmp/unarchive_folder state=absent" -b

