from django.contrib import admin

from .models import Customer, Document, Profession, DataSheet

# Register your models here.

admin.site.register((Customer, Document, Profession, DataSheet))
