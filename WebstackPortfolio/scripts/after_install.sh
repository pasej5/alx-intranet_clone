#!/usr/bin/bash

# Define variables
PROJECT_DIR="/home/ubuntu/alx-intranet_clone/WebstackPortfolio"
GUNICORN_SOCKET="/run/gunicorn.sock"

# Remove old Gunicorn socket if it exists
if [ -e $GUNICORN_SOCKET ]; then
    sudo rm $GUNICORN_SOCKET
fi

# Change to project directory
cd $PROJECT_DIR

# Install Python dependencies
source $PROJECT_DIR/new_env/bin/activate
pip install -r $PROJECT_DIR/requirements.txt

# Run database migrations
python3 manage.py migrate

# Collect static files
python3 manage.py collectstatic --noinput
