#!/usr/bin/bash
sudo cp /home/ubuntu/alx-intranet_clone/WebstackPortfolio/gunicorn/gunicorn.socket  /etc/systemd/system/gunicorn.socket
sudo cp /home/ubuntu/alx-intranet/WebstackPortFoilo/gunicorn/gunicorn.service  /etc/systemd/system/gunicorn.service

sudo systemctl start gunicorn.service
sudo systemctl enable gunicorn.service