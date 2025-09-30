# jobs/models.py

from django.db import models
from users.models import CustomUser # We need to link a job to a user

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    # Link to the user who posted the job
    # We limit choices to only users with the 'recruiter' role
    posted_by = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        limit_choices_to={'role': 'recruiter'}
    )

    def __str__(self):
        return f"{self.title} at {self.company}"