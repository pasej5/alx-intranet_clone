#!/bin/bash

# Create the virtual environment if it doesn't exist
if [ ! -d "/home/ubuntu/alx-intranet_clone/WebstackPortfolio/new_env" ]; then
    python3 -m venv /home/ubuntu/alx-intranet_clone/WebstackPortfolio/new_env
fi

# Activate the virtual environment
source /home/ubuntu/alx-intranet_clone/WebstackPortfolio/new_env/bin/activate

# Install system dependencies
sudo apt-get update
sudo apt-get install -y nginx

# Install Python dependencies
pip install --upgrade pip
pip install -r /home/ubuntu/alx-intranet_clone/WebstackPortfolio/requirements.txt
