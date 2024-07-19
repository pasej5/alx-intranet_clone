#!/bin/bash

# Check if Gunicorn is running
if pgrep gunicorn > /dev/null
then
    echo "Gunicorn is running"
else
    echo "Gunicorn is not running"
    exit 1
fi

# Check if Nginx is running
if systemctl status nginx | grep running > /dev/null
then
    echo "Nginx is running"
else
    echo "Nginx is not running"
    exit 1
fi