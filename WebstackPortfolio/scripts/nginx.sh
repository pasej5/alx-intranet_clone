#!/usr/bin/bash

# Define variables
NGINX_CONFIG="/etc/nginx/sites-available/webstackportfolio"
NGINX_SYMLINK="/etc/nginx/sites-enabled/webstackportfolio"

# Copy the Nginx configuration file
sudo cp $PROJECT_DIR/nginx/webstackportfolio $NGINX_CONFIG

# Remove old symlink if it exists
if [ -L $NGINX_SYMLINK ]; then
    sudo rm $NGINX_SYMLINK
fi

# Create a new symlink
sudo ln -s $NGINX_CONFIG $NGINX_SYMLINK

# Test Nginx configuration
sudo nginx -t

# Restart Nginx
sudo systemctl restart nginx