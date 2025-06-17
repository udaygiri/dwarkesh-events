"""
URL configuration for dwarkeshevents project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from contact.views import contact_inquiry

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='Home'),    path('about/', views.about, name='About'),
    path('services/', views.services, name='Services'),
    path('gallery/', views.gallery, name='Gallery'),
    path('contact/', views.contact, name='Contact'),
    path('send-form/', contact_inquiry, name='Contact-inquiry'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
