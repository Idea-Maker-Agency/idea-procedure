# Ansible

Running ansible on wsl (windows subsytem linux)

1. Install ansible on wsl
2. Create an ssh key pair if you don't have one.
3. Create a playbook.yml as shown in `deployment/ansible/playbook.yml`
4. run the command:

`ansible-playbook --private-key <keyfile> -i django@<server> playbook.yml`

_Note_: Due to difficulties changing the permissions of the ssh private key on wsl, I
had to run the command in the /user/tom/.ssh/ directory where the file was already 
permission 600. So my command was:  
`ansible-playbook --private-key id_rsa -i django@<server> /mnt/d/projects/ansible/playbook.yml`