from django.shortcuts import render
from django.contrib import messages
from gallery.models import Gallery

def index(req):
    return render(req, 'index.html')


def about(req):
    return render(req, 'about.html')


def services(req):
    return render(req, 'services.html')


def gallery(req):
    images = []
    try:
        # Check if table exists first
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='gallery_gallery';")
            if cursor.fetchone():
                from gallery.models import Gallery
                images = Gallery.objects.all()
                print(f"Gallery loaded successfully: {len(images)} items")
            else:
                print("Gallery table does not exist")
    except Exception as e:
        # Log the error and continue with empty list
        print(f"Gallery database error: {e}")
        import traceback
        traceback.print_exc()
        images = []
    
    return render(req, 'gallery.html', {'images': images})


def contact(req):
    return render(req, 'contact.html')

