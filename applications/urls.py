# applications/urls.py

from django.urls import path
# Import all three views now
from .views import (
    ApplyForJobView,
    ListJobApplicationsView,

    UpdateApplicationStatusView
)

urlpatterns = [
    # POST /api/jobs/<job_id>/apply/
    path('jobs/<int:job_id>/apply/', ApplyForJobView.as_view(), name='apply-for-job'),
    
    # GET /api/jobs/<job_id>/applications/
    path('jobs/<int:job_id>/applications/', ListJobApplicationsView.as_view(), name='list-job-applications'),
    
    # PATCH /api/applications/<application_id>/
    # Add this new line for updating
    path('applications/<int:application_id>/', UpdateApplicationStatusView.as_view(), name='update-application-status'),
]