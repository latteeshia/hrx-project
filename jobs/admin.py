# jobs/admin.py

from django.contrib import admin
from .models import Job

# This line tells the admin site to show the Job model
admin.site.register(Job)