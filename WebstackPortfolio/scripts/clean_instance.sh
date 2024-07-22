#!/usr/bin/bash

# Stop the gunicorn and nginx services
sudo service gunicorn stop
sudo service nginx stop

# Remove previous application files
sudo rm -rf /home/ubuntu/WebstackPortfolio/*
