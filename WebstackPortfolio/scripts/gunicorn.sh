#!/bin/bash

# Define variables
PROJECT_DIR="/home/ubuntu/alx-intranet_clone/WebstackPortfolio"
GUNICORN_SOCKET="/run/gunicorn.sock"
GUNICORN_BIN="$PROJECT_DIR/new_env/bin/gunicorn"
APP_MODULE="WebstackPortfolio.wsgi:application"

# Start Gunicorn
sudo $GUNICORN_BIN --bind unix:$GUNICORN_SOCKET --workers 3 --access-logfile - $APP_MODULE