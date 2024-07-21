#!/bin/bash

# Update the package list and install necessary dependencies
sudo yum -y update
sudo yum -y install ruby wget nginx python3-pip

# Install CodeDeploy agent
cd /home/ec2-user
wget https://aws-codedeploy-eu-north-1.s3.eu-north-1.amazonaws.com/latest/install
sudo chmod +x ./install
sudo ./install auto
sudo service codedeploy-agent start

# Install Gunicorn and other Python dependencies
pip3 install gunicorn django

# Enable and start Nginx
sudo systemctl enable nginx
sudo systemctl start nginx
