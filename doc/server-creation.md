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
  
cd into the directory and clone the repo

`git clone git@github.com:tkwon/<project> src`

You should now have `/home/django/sites/<project>src`

### prepare the virtual environment
in the project directory run:

`virtualenv env --python=python3`

Note: I typically name the virtualenv directory "prod" or "stage" to indicate what its used for.

### Prepare the systemctl files
in our project home directory there is a folder called "deployment".
Those hold the various files including systemctl/*.service and *.socket

1. Fix the paths inside the files to match your installation.
2. `cd /etc/systemd/system`
3. `sudo ln -s /home/django/sites/<project>/src/deployment/systemctl/staging.service`   
4. `sudo ln -s /home/django/sites/<project>/src/deployment/systemctl/staging.socket`   
5. Tell systemctl to read those new files:  
`sudo systemctl daemon-reload`   
6. Tell systemctl to restart those processes if the server is rebooted.  
`sudo systemctl enable staging.socket`    
`sudo systemctl enable staging.socket`  
7. Tell systemctl to start the processes.  
`sudo systemctl start staging.socket`  
`sudo systemctl start staging.service`  

You can check /run to see if the .sock file is created  
You can also see if the gunicorn process is running  
`sudo systemctl status staging.service`

### Configure nginx 
1. go into the nginx config directory
`cd /etc/nginx/sites-enabled`
2. remove the default and then link to our config in the deployment directory
`sudo ln -s /home/django/sites/<project>/src/deployment/nginx/nginx-stage.conf`
3. Edit the file making sure all paths are correct.
4. Test file
`sudo nginx -t`
5. restart nginx
`sudo service nginx restart`

You website should now be visible!