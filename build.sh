#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Try to install psycopg separately if needed
echo "Ensuring PostgreSQL adapter is installed..."
pip install psycopg[binary] || pip install psycopg2-binary

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Run migrations
echo "Running migrations..."
python manage.py migrate