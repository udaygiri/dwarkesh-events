#!/bin/bash
# Exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Create staticfiles directory if it doesn't exist
mkdir -p staticfiles

# Collect static files
python manage.py collectstatic --no-input --clear

# Apply database migrations with error handling
echo "=== DATABASE SETUP ==="
echo "Initializing database..."

# Use our custom database initialization command
python manage.py init_database

echo "Verifying database setup..."
python manage.py showmigrations gallery

# Create superuser if specified in environment variables
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] && [ -n "$DJANGO_SUPERUSER_EMAIL" ]; then
    echo "=== CREATING SUPERUSER ==="
    python manage.py createsuperuser --noinput
fi

# Add environment info for debugging
echo "=== ENVIRONMENT INFO ==="
echo "Python version: $(python --version)"
echo "Django version: $(python -c 'import django; print(django.get_version())')"
echo "Working directory: $(pwd)"
echo "Database file location: $(python -c 'from django.conf import settings; print(settings.DATABASES[\"default\"][\"NAME\"])')"

echo "=== BUILD COMPLETE ==="
echo "Gallery setup verification complete!"

# Final comprehensive test
echo "=== FINAL SYSTEM TEST ==="
python manage.py shell -c "
print('Testing gallery functionality...')
try:
    from gallery.models import Gallery
    from django.urls import reverse
    from django.test import Client
    
    # Test model access
    count = Gallery.objects.count()
    print(f'✓ Gallery model works: {count} items')
    
    # Test if we can import the view
    from dwarkeshevents.views import gallery
    print('✓ Gallery view import successful')
    
    print('Database initialization complete and verified!')
    
except Exception as e:
    print(f'✗ Final test failed: {e}')
    import traceback
    traceback.print_exc()
"
