# jobs/models.py
from django.db import models
from django.conf import settings

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='jobs', 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title