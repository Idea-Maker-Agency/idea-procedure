- make sure you have installed all dependencies including gunicorn in the virtual environment
---

### FILES TO BE UPDATED
- gunicorn_conf.py
- production.service 
- nginx_conf

---

#### gunicorn_conf.py
 TO UPDATE: ``user`` `` bind``
 
 
### production.service
TO UPDATE: 
- ``Description`` short description
- ``User``
- ``Group``
- ``WorkingDirectory`` root working directory of your project
- ``ExecStart``  PATH_TO_VIRTUALENV, PATH_TO_GUNICORN_CONF_FILE, PATH_FOR_LOGFILE

### MAKE SURE YOU HAVE CREATED ``LOG`` FOLDER ALREADY AND YOU UPUDATED ALL FILES ACCORDINGLY

---

- COPY `production.service` file to `/etc/systemd/system/`
- RUN command `sudo systemctl start production` and `sudo systemctl enable production`.
 We can confirm that the operation was successful by checking for the socket file.

- COPY `nginx_conf` file to `/etc/nginx/sites-available`
- make sure you rename it with your domain name example: `example.com or example.app`
- Save and close the file when you are finished. Now, we can enable the file by linking it to the sites-enabled directory:
- `sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled`
- Test your Nginx configuration for syntax errors by typing:
- `sudo nginx -t`


Now RESTART NGINX SERVICE
- `sudo systemctl restart nginx`

---

### INSTALL SSL CERTBOT
follow the steps
- `sudo apt-get update`
- `sudo apt-get install software-properties-common`
- `sudo add-apt-repository universe`
- `sudo add-apt-repository ppa:certbot/certbot`
- `sudo apt-get update`

Now install certbot package for nginx
- `sudo apt-get install certbot python-certbot-nginx`
- Run this command to get a certificate and have Certbot edit your Nginx configuration automatically to serve it, turning on HTTPS access in a single step.

- `sudo certbot --nginx`



