#!/usr/bin/bash

# Exit on error
set -e

# Define variables
PROJECT_DIR="/home/ubuntu/alx-intranet_clone/WebstackPortfolio"
VENV_DIR="$PROJECT_DIR/new_env"
GUNICORN_SOCKET="/run/gunicorn.sock"
GUNICORN_BIN="$VENV_DIR/bin/gunicorn"
APP_MODULE="WebstackPortfolio.WebstackPortfolio.wsgi:application"
LOG_DIR="$PROJECT_DIR/logs"
GUNICORN_LOGFILE="$LOG_DIR/gunicorn.log"

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
sudo mkdir -p /run
sudo chmod 777 /run

# Ensure the logs directory exists
mkdir -p $LOG_DIR

# Start Gunicorn server
echo "Starting Gunicorn..."
$GUNICORN_BIN --workers 3 --bind unix:$GUNICORN_SOCKET $APP_MODULE --log-file $GUNICORN_LOGFILE --log-level debug

echo "Gunicorn started."
