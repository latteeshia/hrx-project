# jobs/views.py
from rest_framework import generics, permissions
from .models import Job
from .serializers import JobSerializer
from .permissions import IsJobOwner  # <-- Corrected import
from .filters import JobFilter

class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = JobFilter

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    # Use the new, more powerful permission class
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsJobOwner]