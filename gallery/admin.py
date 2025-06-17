from django.contrib import admin
from .models import Gallery

# Register your models here.

admin.site.register(Gallery) # This line registers the Gallery model with the Django admin site, allowing it to be managed through the admin interface.