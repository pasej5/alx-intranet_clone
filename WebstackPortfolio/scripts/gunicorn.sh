#!/usr/bin/bash

# Define variables
PROJECT_DIR="/home/ubuntu/alx-intranet_clone/WebstackPortfolio"
GUNICORN_SOCKET="/run/gunicorn.sock"
GUNICORN_BIN="$PROJECT_DIR/new_env/bin/gunicorn"
APP_MODULE="WebstackPortfolio.WebstackPortfolio.wsgi:application"

# Create the /run directory if it doesn't exist and set permissions
sudo mkdir -p /run
sudo chown ubuntu:ubuntu /run
sudo chown -R ubuntu:ubuntu $PROJECT_DIR


# Navigate to project directory
cd $PROJECT_DIR

# Set PYTHONPATH
export PYTHONPATH=$PROJECT_DIR

# Activate the virtual environment
source $PROJECT_DIR/new_env/bin/activate

# Start Gunicorn
exec $GUNICORN_BIN --bind unix:$GUNICORN_SOCKET --workers 3 --access-logfile - $APP_MODULE
