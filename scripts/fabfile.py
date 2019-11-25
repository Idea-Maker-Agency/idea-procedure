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

