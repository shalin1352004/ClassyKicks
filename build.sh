#!/bin/bash

# Build script for ClassyKicks Django project

echo "Building ClassyKicks project..."

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

echo "Build completed successfully!" 