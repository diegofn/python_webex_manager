# python_webex_manager

This is a WebEx Meetings manager written in python and Flesk. It publish endpoint for Calendar services.

## Features
- Installation process to Flesk, Gunicorn and Apache installation manual
- Database token storage
- Calendly integration with endpoint

## Installation with Gunicorn and Apache Reverse Proxy

1. Install flask and request on venv
```Shell
$ apt-get install python3-venv
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
User=root
Group=www-data
WorkingDirectory=/root/Documents/python/python_webex_manager
Environment="PATH=/root/Documents/python/python_webex_manager/bin"
ExecStart=/root/Documents/python/python_webex_manager/bin/gunicorn --config gunicorn_config.py wsgi:app

[Install]
WantedBy=multi-user.target
```

3. Install the system service
```Shell
$ sudo systemctl start flaskwebexmanager.service
$ sudo systemctl enable flaskwebexmanager.service
$ sudo systemctl status flaskwebexmanager.service
```

4. Configure apache2 as reverse proxy
```Shell
$ sudo vi /etc/apache2/sites-available/webexmanager.conf
```

Add the following lines
```xml
<IfModule mod_ssl.c>
    <VirtualHost _default_:444>
        ServerAdmin openbsdhacker@gmail.com
	ServerName www.technilabs.app

        ErrorLog ${APACHE_LOG_DIR}/webexmanager-error.log
        CustomLog ${APACHE_LOG_DIR}/webexmanager-access.log combined

        SSLEngine on
        SSLCertificateFile	/etc/ssl/certs/techniclabs.app.crt
        SSLCertificateKeyFile /etc/ssl/private/techniclabs.app.key

        <Location />
            ProxyPass unix:/root/Documents/python/python_webex_manager/flask_webex_manager.sock|http://127.0.0.1/
            ProxyPassReverse unix:/root/Documents/python/python_webex_manager/flask_webex_manager.sock|http://127.0.0.1/
        </Location>
    </VirtualHost>
</IfModule>
```

Enable the site
```Shell
sudo a2ensite webexmanager.conf
systemctl reload apache2
```
