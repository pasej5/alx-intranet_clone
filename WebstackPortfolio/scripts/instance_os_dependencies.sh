#!/bin/bash

# Define variables
PROJECT_DIR="/home/ubuntu/alx-intranet_clone/WebstackPortfolio"

# Activate virtual environment
source $PROJECT_DIR/new_env/bin/activate

# Install Python dependencies
pip install -r $PROJECT_DIR/requirements.txt
