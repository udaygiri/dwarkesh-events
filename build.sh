#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
echo "==========Installing dependencies=========="
pip install --upgrade pip
pip install -r requirements.txt
echo "==========Dependencies installed=========="

echo "|"
echo "|"
echo "|"
echo "V"

# Try to install psycopg separately if needed
echo "==========Ensuring PostgreSQL adapter is installed=========="
pip install psycopg[binary] || pip install psycopg2-binary
echo "==========PostgreSQL adapter installed=========="

echo "|"
echo "|"
echo "|"
echo "V"

# Set Django settings module explicitly
export DJANGO_SETTINGS_MODULE=dwarkeshevents.settings

# Check Django installation and settings
echo "==========Checking Django installation=========="
python -c "import django; print(f'Django version: {django.get_version()}')"
echo "==========Django check complete=========="

echo "|"
echo "|"
echo "|"
echo "V"

# Collect static files
echo "==========Collecting static files=========="
python manage.py collectstatic --noinput
echo "==========Static files collected=========="

echo "|"
echo "|"
echo "|"
echo "V"

# Run database migrations
echo "==========Running database migrations=========="
python manage.py migrate
echo "==========Database migrations complete=========="

echo "|"
echo "|"
echo "|"
echo "V"

# Initialize database with sample data if needed
echo "==========Initializing database=========="
python manage.py init_database || echo "Database initialization skipped or failed"
echo "==========Database initialization complete=========="

echo "|"
echo "|"
echo "|"
echo "V"

echo "==========Build process complete=========="
