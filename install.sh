#!/bin/bash

sudo rm /etc/nginx/sites-available/default
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

cd /home/box/web
gunicorn -w 1 -b 0.0.0.0:8080 hello:app &
gunicorn -w 1 -b 0.0.0.0:8000 ask.ask.wsgi:application
