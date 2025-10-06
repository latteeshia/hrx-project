# jobs/admin.py
from django.contrib import admin
from .models import Job

# This makes the Job model visible in the admin panel
admin.site.register(Job)