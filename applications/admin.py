# applications/admin.py
from django.contrib import admin
from .models import Application

# This makes the Application model visible in the admin panel
admin.site.register(Application)