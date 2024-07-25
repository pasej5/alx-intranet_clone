#!/usr/bin/bash

# Define variables
PROJECT_DIR="/home/ubuntu/alx-intranet_clone/WebstackPortfolio"
GUNICORN_SOCKET="/run/gunicorn.sock"

# Remove Gunicorn socket
if [ -e $GUNICORN_SOCKET ]; then
    sudo rm $GUNICORN_SOCKET
fi

# Clean up old static files
sudo rm -rf $PROJECT_DIR/staticfiles/*