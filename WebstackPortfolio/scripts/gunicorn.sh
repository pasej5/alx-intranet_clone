#!/usr/bin/bash

# Define variables
PROJECT_DIR="/home/ubuntu/alx-intranet_clone/WebstackPortfolio/WebstackPortfolio"
GUNICORN_SOCKET="/run/gunicorn.sock"
GUNICORN_BIN="$PROJECT_DIR/WebstackPortfolio/new_env/bin/gunicorn"
APP_MODULE="WebstackPortfolio.wsgi:application"

# Create the /run directory if it doesn't exist and set permissions
sudo mkdir -p /run
sudo chown ubuntu:ubuntu /run

# Ensure the project directory has correct permissions
sudo chown -R ubuntu:ubuntu $PROJECT_DIR

# Recreate the virtual environment if needed
if [ ! -d "$PROJECT_DIR/WebstackPortfolio/new_env" ]; then
    echo "Virtual environment not found. Creating a new one..."
    python3 -m venv $PROJECT_DIR/WebstackPortfolio/new_env
fi

# Activate the virtual environment and install dependencies
source $PROJECT_DIR/WebstackPortfolio/new_env/bin/activate
pip install --upgrade pip
pip install -r $PROJECT_DIR/requirements.txt

# Fix shebang line in gunicorn if needed
GUNICORN_EXECUTABLE="$PROJECT_DIR/WebstackPortfolio/new_env/bin/gunicorn"
if [ -f "$GUNICORN_EXECUTABLE" ]; then
    CURRENT_SHEBANG=$(head -n 1 "$GUNICORN_EXECUTABLE")
    EXPECTED_SHEBANG="#!/home/ubuntu/alx-intranet_clone/WebstackPortfolio/WebstackPortfolio/new_env/bin/python3"
    if [ "$CURRENT_SHEBANG" != "$EXPECTED_SHEBANG" ]; then
        echo "Updating shebang line in gunicorn executable..."
        sed -i "1s|$CURRENT_SHEBANG|$EXPECTED_SHEBANG|" "$GUNICORN_EXECUTABLE"
    fi
else
    echo "Gunicorn executable not found. Please check your setup."
    exit 1
fi

# Set PYTHONPATH
export PYTHONPATH=$PROJECT_DIR

# Start Gunicorn
exec $GUNICORN_BIN --bind unix:$GUNICORN_SOCKET --workers 3 --access-logfile - $APP_MODULE
