#!/usr/bin/bash

# Exit on error
set -e

# Define variables
PROJECT_DIR="/home/ubuntu/alx-intranet_clone"
VENV_DIR="$PROJECT_DIR/new_env"
GUNICORN_SOCKET="/run/gunicorn.sock"
GUNICORN_BIN="$VENV_DIR/bin/gunicorn"
APP_MODULE="WebstackPortfolio.wsgi:application"
LOG_DIR="$PROJECT_DIR/logs"
GUNICORN_LOGFILE="$LOG_DIR/gunicorn.log"

# Create the virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
    echo "Virtual environment created at $VENV_DIR"
else
    echo "Virtual environment already exists at $VENV_DIR"
fi

# Verify the existence of the activate script
if [ -f "$VENV_DIR/bin/activate" ]; then
    echo "Activating virtual environment..."
    source $VENV_DIR/bin/activate
else
    echo "Error: Virtual environment activate script not found."
    exit 1
fi

# Upgrade pip and install gunicorn
echo "Upgrading pip and installing gunicorn..."
pip install --upgrade pip
pip install gunicorn

# Ensure the /run directory exists and is writable
sudo mkdir -p /run
sudo chmod 777 /run

# Ensure the logs directory exists
mkdir -p $LOG_DIR

# Ensure the log file is writable
touch $GUNICORN_LOGFILE
chmod 664 $GUNICORN_LOGFILE

# Start Gunicorn server
echo "Starting Gunicorn..."
exec $GUNICORN_BIN --workers 3 --bind unix:$GUNICORN_SOCKET $APP_MODULE --log-file $GUNICORN_LOGFILE --log-level debug

echo "Gunicorn started."
