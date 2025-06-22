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
echo "==========Django installation checked=========="

echo "|"
echo "|"
echo "|"
echo "V"

# Test Django settings import
echo "==========Testing Django settings import=========="
python -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dwarkeshevents.settings')
import django
django.setup()
from django.conf import settings
print(f'SECRET_KEY configured: {bool(settings.SECRET_KEY)}')
print(f'DEBUG: {settings.DEBUG}')
print(f'ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}')
print('Settings imported successfully')
"
echo "==========Django settings tested=========="

echo "|"
echo "|"
echo "|"
echo "V"

# Check available management commands
echo "==========Checking available commands=========="
python manage.py help
echo "==========Available commands listed=========="

echo "|"
echo "|"
echo "|"
echo "V"

# Check if manage.py exists and is executable
echo "==========Checking manage.py=========="
ls -la manage.py
python manage.py --help > /dev/null
echo "==========manage.py is executable=========="

echo "|"
echo "|"
echo "|"
echo "V"

# Collect static files
echo "==========Collecting static files=========="
python manage.py collectstatic --noinput --verbosity=2
echo "==========Static files collected=========="

echo "|"
echo "|"
echo "|"
echo "V"

# Run migrations
echo "==========Running migrations=========="
python manage.py migrate --verbosity=2
echo "==========Migrations completed=========="