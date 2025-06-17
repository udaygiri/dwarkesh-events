#!/bin/bash
# Exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Create superuser if specified in environment variables
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] && [ -n "$DJANGO_SUPERUSER_EMAIL" ]; then
    python manage.py createsuperuser --noinput
fi
