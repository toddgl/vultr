## Ansible to deploy a Freebsd Server running Django on vultr

Currently work in progress

To create a new server use the following:

ansible-playbook --ask-vault-pass --extra-vars '@secrets.yml' -i hosts vultr.yml -e "vultr_server_name=ansible-demo"

Log into the Vultr instance and copy the root password from the server detail screen the root password need to he updated in the secrets.yml file using this command;

ansible-vault edit secrets.yml

Then run the following command to set up users and the SSH public keys

ansible-playbook --extra-vars '@secrets.yml' -i hosts bootstrap-ansible.yml -e "host=ansible-demo inventory_group_name=git"

The host file will be updated as a result of these to playbook runs

To delete the server use the following command.

ansible-playbook --extra-vars '@secrets.yml' vultr.yml -e "vultr_server_name=ansible-demo delete=true"
