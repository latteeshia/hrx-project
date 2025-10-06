# jobs/urls.py
from django.urls import path
from .views import (
    JobListView,
    JobDetailView,
    JobCreateView,
    RecruiterJobsView
)

urlpatterns = [
    # For getting all jobs (homepage)
    path('', JobListView.as_view(), name='job-list'),
    
    # For creating a new job
    path('create/', JobCreateView.as_view(), name='job-create'),
    
    # For a recruiter to see their own jobs
    path('my-jobs/', RecruiterJobsView.as_view(), name='recruiter-jobs'),
    
    # For seeing a single job's detail
    path('<int:pk>/', JobDetailView.as_view(), name='job-detail'),
]