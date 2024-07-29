#!/usr/bin/bash

# Exit on any error
set -e

# necessary system packages
sudo apt-get update
sudo apt-get install -y nginx python3-venv python3-pip

# Create the virtual environment if it doesn't exist
VENV_DIR="/home/ubuntu/alx-intranet_clone/WebstackPortfolio/new_env"
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
fi

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r /home/ubuntu/alx-intranet_clone/WebstackPortfolio/requirements.txt
