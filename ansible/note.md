# Ansible Useful command

* ``` ansible --list-hosts data_center ```

* ``` ansible data_center -m command -a 'uname -r' ```

* ``` ansible data_center -m command -a 'cat /etc/os-release' ```

* ``` ansible node1 -m ping ```

* Most modules are idempotent, which means they only make changes if a change is needed.
Idempotent modules can be run safely multiple times.
