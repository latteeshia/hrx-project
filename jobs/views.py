# jobs/views.py
from rest_framework import generics, permissions
from .models import Job
from .serializers import JobSerializer

class JobListView(generics.ListAPIView):
    queryset = Job.objects.all().order_by('-date_posted')
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]

class JobDetailView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]

class JobCreateView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

# jobs/views.py
# ... (at the end of the file, after your other views)

class RecruiterJobsView(generics.ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filter jobs to only those posted by the current user
        return Job.objects.filter(posted_by=self.request.user).order_by('-date_posted')