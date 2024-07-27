#!/usr/bin/bash

# Exit on error
set -e

# Define variables
PROJECT_DIR="/home/ubuntu/alx-intranet_clone/WebstackPortfolio/WebstackPortfolio"
VENV_DIR="$PROJECT_DIR/new_env"
GUNICORN_SOCKET="/run/gunicorn.sock"
GUNICORN_BIN="$VENV_DIR/bin/gunicorn"
APP_MODULE="WebstackPortfolio.wsgi:application"
REQUIREMENTS_FILE="$PROJECT_DIR/requirements.txt"

# Function to ensure the project directory exists and has correct permissions
ensure_permissions() {
    echo "Checking project directory permissions..."
    if [ ! -d "$PROJECT_DIR" ]; then
        echo "Project directory not found: $PROJECT_DIR"
        exit 1
    fi

    # Create the /run directory if it doesn't exist and set permissions
    sudo mkdir -p /run
    sudo chown ubuntu:ubuntu /run

    # Ensure the project directory has correct permissions
    sudo chown -R ubuntu:ubuntu $PROJECT_DIR
}

# Function to create or activate the virtual environment
setup_virtualenv() {
    echo "Setting up virtual environment..."
    if [ ! -d "$VENV_DIR" ]; then
        echo "Virtual environment not found. Creating a new one..."
        python3 -m venv $VENV_DIR
    fi

    echo "Activating virtual environment..."
    source $VENV_DIR/bin/activate
}

# Function to install or upgrade dependencies
install_dependencies() {
    echo "Upgrading pip and reinstalling Gunicorn..."
    $VENV_DIR/bin/pip install --upgrade pip
    $VENV_DIR/bin/pip uninstall -y gunicorn || true
    $VENV_DIR/bin/pip install gunicorn

    echo "Installing dependencies from requirements.txt..."
    if [ -f "$REQUIREMENTS_FILE" ]; then
        $VENV_DIR/bin/pip install -r $REQUIREMENTS_FILE
    else
        echo "Requirements file not found at $REQUIREMENTS_FILE"
        exit 1
    fi
}

# Function to start Gunicorn
start_gunicorn() {
    echo "Starting Gunicorn..."
    export PYTHONPATH=$PROJECT_DIR
    exec $GUNICORN_BIN --bind unix:$GUNICORN_SOCKET --workers 3 --access-logfile - $APP_MODULE
}

# Main script execution
ensure_permissions
setup_virtualenv
install_dependencies
start_gunicorn

