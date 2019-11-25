###################################################################
#
# Usage:
# fab doit(path_to_ssh_key) django

#
# If you use a passphrase then add --prompt-for-passphrase
####################################################################
from fabric import task, Connection


@task
def doit(ctx, ip, keypath):
    ctx.user = 'root'
    ctx.host = ip
    ctx.connect_kwargs.key_filename = ''.format(keypath)


@task
def django(ctx):
    conn = Connection(ctx.host, ctx.user, connect_kwargs=ctx.connect_kwargs)
    print('apt-get update')
    conn.sudo('apt-get update -y', pty=True)
    print('apt-get upgrade')
    conn.sudo('apt-get upgrade -y', pty=True)
    print('apt-get install python3-django python3-pip virtualenv postgresql nginx -y')
    conn.sudo('apt-get install python3-django python3-pip virtualenv postgresql nginx -y', pty=True)
    print('add-apt-repository ppa:certbot/certbot')
    conn.sudo('add-apt-repository ppa:certbot/certbot', pty=True)
    print('apt-get install python-certbot-nginx -y')
    conn.sudo('apt-get install python-certbot-nginx -y', pty=True)
    print('useradd -m django')
    conn.sudo('useradd -m django')
    print('usermod -s /bin/bash django')
    conn.sudo('usermod -s /bin/bash django')
    print('copy ssh keys')
    conn.sudo('cp -r .ssh/ /home/django/.ssh')
    print('create swap file')
    conn.sudo('fallocate -l 2G /swapfile')
    conn.sudo('chmod 600 /swapfile')
    conn.sudo('mkswap /swapfile')
    conn.sudo('swapon /swapfile')
    conn.sudo('cp /etc/fstab /etc/fstab.bak')
    conn.sudo('echo "/swapfile none swap sw 0 0" | sudo tee -a /etc/fstab')
    conn.sudo('swapon --show')


