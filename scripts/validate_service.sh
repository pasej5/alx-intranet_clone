#!/bin/bash
# Validate the Nginx service is running
if systemctl status nginx | grep -q 'active (running)'; then
  echo "Nginx is running"
  exit 0
else
  echo "Nginx is NOT running"
  exit 1
fi