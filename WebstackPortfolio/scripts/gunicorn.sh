#!/usr/bin/bash

# Define variables
PROJECT_DIR="/home/ubuntu/alx-intranet_clone/WebstackPortfolio"
GUNICORN_SOCKET="/run/gunicorn.sock"
GUNICORN_BIN="$PROJECT_DIR/new_env/bin/gunicorn"
APP_MODULE="WebstackPortfolio.wsgi:application"

# Navigate to project directory
cd $PROJECT_DIR/WebstackPortfolio || exit 1

# Activate the virtual environment
source $PROJECT_DIR/new_env/bin/activate

# Start Gunicorn
exec $GUNICORN_BIN --bind unix:$GUNICORN_SOCKET --workers 3 --access-logfile - $APP_MODULE