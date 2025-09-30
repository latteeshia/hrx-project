# jobs/urls.py

from django.urls import path
from .views import JobListCreateView, JobDetailView

urlpatterns = [
    # This path is now the root of /api/jobs/
    path('', JobListCreateView.as_view(), name='job-list-create'),
    
    # This path becomes /api/jobs/<id>/
    path('<int:pk>/', JobDetailView.as_view(), name='job-detail'),
]