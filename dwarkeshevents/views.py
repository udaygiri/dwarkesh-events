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
    images = Gallery.objects.all()
    return render(req, 'gallery.html', {'images' : images})


def contact(req):
    return render(req, 'contact.html')

