#!/usr/bin/bash

# Remove old static files and logs
sudo rm -rf /home/ubuntu/alx-intranet_clone/WebstackPortfolio/staticfiles/*
sudo rm -rf /home/ubuntu/alx-intranet_clone/WebstackPortfolio/logs/*

# Ensure important files and directories are preserved
# You might include additional directories or files as needed

# Restart Gunicorn and Nginx if necessary
sudo systemctl restart gunicorn
sudo systemctl restart nginx
logs