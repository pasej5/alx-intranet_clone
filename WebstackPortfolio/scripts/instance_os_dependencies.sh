#!/usr/bin/bash

# Exit on any error
set -e

# Update and install system dependencies
sudo apt-get update
sudo apt-get install -y nginx python3-pip python3-venv

# Create the virtual environment if it doesn't exist
if [ ! -d "/home/ubuntu/alx-intranet_clone/WebstackPortfolio/new_env" ]; then
    python3 -m venv /home/ubuntu/alx-intranet_clone/WebstackPortfolio/new_env
fi

# Activate the virtual environment
source /home/ubuntu/alx-intranet_clone/WebstackPortfolio/new_env/bin/activate

# Upgrade pip and install Python dependencies
pip install --upgrade pip
pip install -r /home/ubuntu/alx-intranet_clone/WebstackPortfolio/requirements.txt

# Create necessary directories for logs if they do not exist
mkdir -p /home/ubuntu/alx-intranet_clone/WebstackPortfolio/logs
sudo chown -R ubuntu:ubuntu /home/ubuntu/alx-intranet_clone/WebstackPortfolio/logs
