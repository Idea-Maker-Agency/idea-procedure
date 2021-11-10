# Steps to setup Github Actions

## Set up ssh key on server
Go to /home/django/.ssh  
Create an ssh keypair: `ssh-keygen`  
No password needed and leave the file names as id_rsa and id_rsa.pub  

## Add these secrets to the project repo
USER: django  
DEV_HOST: (the website url such as dev.example.com)   
STAGING_HOST: (staging.example.com)  
PRODUCTION_HOST: (www.example.com)  
PRIVATE_KEY: Enter the contents of the file id_rsa created above.

