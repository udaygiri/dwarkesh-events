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

# Set Django settings module explicitly
export DJANGO_SETTINGS_MODULE=dwarkeshevents.settings

# Check Django installation and settings
echo "Checking Django installation..."
python -c "import django; print(f'Django version: {django.get_version()}')"

# Check if manage.py exists and is executable
echo "Checking manage.py..."
ls -la manage.py
python manage.py --help > /dev/null

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --verbosity=2

# Run migrations
echo "Running migrations..."
python manage.py migrate --verbosity=2