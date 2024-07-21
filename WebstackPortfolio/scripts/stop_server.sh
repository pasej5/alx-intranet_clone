#!/bin/bash

# Stop Gunicorn
pkill gunicorn

# Stop Nginx
sudo systemctl stop nginx