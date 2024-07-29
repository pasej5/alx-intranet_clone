#!/usr/bin/bash

# Exit on error
set -e

# Define variables
PROJECT_DIR="/home/ubuntu/alx-intranet_clone/WebstackPortfolio"
VENV_DIR="$PROJECT_DIR/new_env"
GUNICORN_SOCKET="/run/gunicorn.sock"
GUNICORN_BIN="$VENV_DIR/bin/gunicorn"
APP_MODULE="WebstackPortfolio.wsgi:application"

# Create the virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
fi

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Upgrade pip and install gunicorn
echo "Upgrading pip and installing gunicorn..."
pip install --upgrade pip
pip install gunicorn

# Ensure the /run directory exists and is writable
sudo mkdir -
