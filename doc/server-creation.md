# Steps to create a server on Digital Ocean

### Install necessary packages
`sudo apt-get update -y`  
`sudo apt-get upgrade -y` 
`sudo apt-get install python3-django python3-pip virtualenv postgresql nginx -y`  

### Add certbot for SSL (letsencrypt)
`sudo add-apt-repository ppa:certbot/certbot`
`sudo apt-get install python-certbot-nginx -y` 

### Create user account and give sudo privileges
`useradd -m django`  

Set shell to bash (my preference)  
`sudo usermod -s /bin/bash django`  

`visudo`  
add `django ALL=(ALL) NOPASSWD:ALL`

### Copy ssh keys so you can log in as django
cp ssh keys to django/.ssh  
  
### prepare code repository
`mkdir /home/django/sites/`  
