#!/bin/bash
# Update the package list and install necessary dependencies
sudo apt-get update
sudo apt-get -y install nginx python3-pip
pip3 install -r /var/www/html/WebstackPortfolio/requirements.txt
