from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection
import traceback

class Command(BaseCommand):
    help = 'Initialize database and create tables if they dont exist'

    def handle(self, *args, **options):
        try:
            # Check if tables exist
            with connection.cursor() as cursor:
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = [row[0] for row in cursor.fetchall()]
                
            self.stdout.write(f"Existing tables: {tables}")
            
            if 'gallery_gallery' not in tables:
                self.stdout.write(self.style.WARNING("Gallery table missing, running migrations..."))
                
                # Run migrations
                call_command('migrate', '--run-syncdb', verbosity=2)
                
                # Verify table was created
                with connection.cursor() as cursor:
                    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='gallery_gallery';")
                    if cursor.fetchone():
                        self.stdout.write(self.style.SUCCESS("Gallery table created successfully"))
                    else:
                        self.stdout.write(self.style.ERROR("Failed to create gallery table"))
            else:
                self.stdout.write(self.style.SUCCESS("Gallery table already exists"))
                
            # Populate gallery
            call_command('populate_gallery')
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error during database initialization: {e}"))
            traceback.print_exc()
