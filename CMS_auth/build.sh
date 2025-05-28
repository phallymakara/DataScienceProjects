#!/usr/bin/env bash
# exit on error
set -o errexit

# Update pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Run DB migrations if there are any
flask db upgrade

# Create upload directories
mkdir -p static/uploads/profiles 