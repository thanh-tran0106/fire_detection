#!/bin/bash

# Update package lists
sudo apt-get update

# Install Flask using pip
sudo apt-get install -y python3-pip
pip3 install Flask

# Create directory structure
mkdir RpiFlaskServer
cd RpiFlaskServer
mkdir static templates
touch run.py

# Display completion message
echo "Flask and directory structure installation completed."
