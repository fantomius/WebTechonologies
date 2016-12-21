#!/bin/bash

sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo rm /etc/nginx/sites-enabled/default

cd /home/box/web
gunicorn -w 1 -b 0.0.0.0:8080 hello:app &
