from django.db import models
from applications.models import Application

class Interview(models.Model):
    INTERVIEW_TYPES = (
        ('Phone Screen', 'Phone Screen'),
        ('Technical', 'Technical'),
        ('HR Round', 'HR Round'),
    )
    STATUS_CHOICES = (
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )

    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='interviews')
    scheduled_at = models.DateTimeField()
    interview_type = models.CharField(max_length=50, choices=INTERVIEW_TYPES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Scheduled')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.interview_type} for {self.application.student.username} - {self.status}"