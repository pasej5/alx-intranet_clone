#!/bin/bash

# Change to the project directory
cd /home/ec2-user/alx-intranet_clone/WebstackPortfolio

# Start Gunicorn
gunicorn --workers 3 --bind unix:/home/ec2-user/alx-intranet_clone/WebstackPortfolio/webstackportfolio.sock WebstackPortfolio.wsgi:application &

# Start Nginx
sudo systemctl restart nginx
