#!/bin/bash
# Update the package list and install any necessary dependencies
sudo yum -y update
sudo yum -y install nginx
sudo systemctl enable nginx
sudo systemctl start nginx