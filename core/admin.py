from django.contrib import admin

from .models import Customer, Document

# Register your models here.

admin.site.register((Customer, Document))
