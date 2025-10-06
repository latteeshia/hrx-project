# applications/models.py
from django.db import models
from django.conf import settings # <-- IMPORT SETTINGS

# We no longer need to import the User model directly

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    
    # THE FIX: Point to the custom user model via settings
    posted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='jobs_posted', 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    
    # THE FIX: Point to the custom user model via settings
    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='applications'
    )
    date_applied = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'applicant')

    def __str__(self):
        return f"{self.applicant.username}'s application for {self.job.title}"