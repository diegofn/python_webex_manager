# python_webex_manager

This is a WebEx Meetings manager written in python and Flesk. It publish endpoint for Calendar services.

## Features
- Installation process to Flesk, Gunicorn and nginx installation manual
- Database token storage
- Calendly integration with endpoint

## Installation with Gunicorn and nginx Reverse Proxy

1. Install flask and request on venv
```Shell
$ sudo apt-get install python3-venv
$ python -m venv .
$ source ./bin/activate
$ pip install flask
$ pip install requests
$ python app.py
```

2. Install and configure gunicorn
```Shell
$ pip install gunicorn
$ gunicorn --bind 127.0.0.1:8080 wsgi:app
```

3. Create a system services
```Shell
$ sudo vi /etc/systemd/system/flaskwebexmanager.service
```

Add the following lines
```
[Unit]
Description=Gunicorn instance to serve flask application for webex manager
After=network.target

[Service]
User=diegofn
Group=www-data
WorkingDirectory=/home/diegofn/Documents/python/python_webex_manager
Environment="PATH=/home/diegofn/Documents/python/python_webex_manager/bin"
ExecStart=/home/diegofn/Documents/python/python_webex_manager/bin/gunicorn --config gunicorn_config.py wsgi:app

[Install]
WantedBy=multi-user.target
```

3. Install the system service
```Shell
$ sudo systemctl start flaskwebexmanager.service
$ sudo systemctl enable flaskwebexmanager.service
$ sudo systemctl status flaskwebexmanager.service
```

4. Configure nginx as reverse proxy
```Shell
$ sudo vi /etc/nginx/sites-available/webexmanager
```

Add the following lines
```
server {
    listen 444;
    server_name techniclabs.app www.techniclabs.app;

    ssl_certificate           /etc/ssl/certs/techniclabs.app.crt;
    ssl_certificate_key       /etc/ssl/private/techniclabs.app.key;

    ssl on;
    ssl_session_cache  builtin:1000  shared:SSL:10m;
    ssl_protocols  TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers HIGH:!aNULL:!eNULL:!EXPORT:!CAMELLIA:!DES:!MD5:!PSK:!RC4;
    ssl_prefer_server_ciphers on;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/diegofn/Documents/python/python_webex_manager/flask_webex_manager.sock;
    }
}
```

Enable the site
```Shell
sudo ln -s /etc/nginx/sites-available/webexmanager /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```
