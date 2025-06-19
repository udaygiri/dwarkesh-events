#!/bin/bash
# Exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Create staticfiles directory if it doesn't exist
mkdir -p staticfiles

# Collect static files
python manage.py collectstatic --no-input --clear

# Apply database migrations with verbose output
echo "Applying database migrations..."
python manage.py migrate --verbosity=2

# Show database tables to verify migration
echo "Checking database tables..."
python manage.py shell -c "from django.db import connection; cursor = connection.cursor(); cursor.execute('SELECT name FROM sqlite_master WHERE type=\"table\";'); print([row[0] for row in cursor.fetchall()])"

# Populate gallery with sample data
echo "Populating gallery with sample data..."
python manage.py populate_gallery

# Create superuser if specified in environment variables
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] && [ -n "$DJANGO_SUPERUSER_EMAIL" ]; then
    python manage.py createsuperuser --noinput
fi

# Final verification - checking gallery table and data...
python manage.py shell -c "
from gallery.models import Gallery
import traceback
try:
    count = Gallery.objects.count()
    print(f'Gallery table exists with {count} items')
    if count > 0:
        first_item = Gallery.objects.first()
        print(f'First item: {first_item.title}')
    else:
        print('No gallery items found - this may cause template errors')
except Exception as e:
    print(f'Error accessing gallery table: {e}')
    traceback.print_exc()
"
