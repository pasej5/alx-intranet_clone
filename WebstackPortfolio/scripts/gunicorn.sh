#!/usr/bin/bash

# Define variables
PROJECT_DIR="/home/ubuntu/alx-intranet_clone/WebstackPortfolio/WebstackPortfolio"
VENV_DIR="$PROJECT_DIR/new_env"
GUNICORN_SOCKET="/run/gunicorn.sock"
GUNICORN_BIN="$VENV_DIR/bin/gunicorn"
APP_MODULE="WebstackPortfolio.wsgi:application"
REQUIREMENTS_FILE="/home/ubuntu/alx-intranet_clone/WebstackPortfolio/requirements.txt"

# Create the /run directory if it doesn't exist and set permissions
sudo mkdir -p /run
sudo chown ubuntu:ubuntu /run

# Ensure the project directory has correct permissions
sudo chown -R ubuntu:ubuntu $PROJECT_DIR

# Recreate the virtual environment if needed
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found. Creating a new one..."
    python3 -m venv $VENV_DIR
fi

# Activate the virtual environment and install dependencies
source $VENV_DIR/bin/activate
pip install --upgrade pip
if [ -f "$REQUIREMENTS_FILE" ]; then
    pip install -r $REQUIREMENTS_FILE
else
    echo "Requirements file not found at $REQUIREMENTS_FILE"
    exit 1
fi

# Fix shebang line in gunicorn if needed
if [ -f "$GUNICORN_BIN" ]; then
    CURRENT_SHEBANG=$(head -n 1 "$GUNICORN_BIN")
    EXPECTED_SHEBANG="#!/home/ubuntu/alx-intranet_clone/WebstackPortfolio/WebstackPortfolio/new_env/bin/python3"
    if [ "$CURRENT_SHEBANG" != "$EXPECTED_SHEBANG" ]; then
        echo "Updating shebang line in gunicorn executable..."
        sed -i "1s|$CURRENT_SHEBANG|$EXPECTED_SHEBANG|" "$GUNICORN_BIN"
    fi
else
    echo "Gunicorn executable not found. Please check your setup."
    exit 1
fi

# Set PYTHONPATH
export PYTHONPATH=$PROJECT_DIR

# Start Gunicorn
exec $GUNICORN_BIN --bind unix:$GUNICORN_SOCKET --workers 3 --access-logfile - $APP_MODULE