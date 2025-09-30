# applications/views.py

from rest_framework import generics, permissions, serializers
from jobs.models import Job
from .models import Application
from .serializers import ApplicationSerializer

# --- PERMISSION CLASSES ---

class IsStudent(permissions.BasePermission):
    """Permission to only allow students to create an application."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'student'

# applications/views.py

# ... (imports and IsStudent class) ...

class IsJobOwner(permissions.BasePermission):
    """Permission to allow the owner of the related job to perform an action."""
    def has_permission(self, request, view):
        # For URLs with 'job_id' (like listing applications)
        if 'job_id' in view.kwargs:
            job_id = view.kwargs['job_id']
            try:
                job = Job.objects.get(pk=job_id)
                return job.posted_by == request.user
            except Job.DoesNotExist:
                return False

        # For URLs with 'application_id' (like updating an application)
        elif 'application_id' in view.kwargs:
            application_id = view.kwargs['application_id']
            try:
                application = Application.objects.get(pk=application_id)
                return application.job.posted_by == request.user
            except Application.DoesNotExist:
                return False
        
        return False
# --- API VIEWS ---

class ApplyForJobView(generics.CreateAPIView):
    """Allows a student to apply for a specific job."""
    serializer_class = ApplicationSerializer
    permission_classes = [IsStudent]

    def perform_create(self, serializer):
        job_id = self.kwargs.get('job_id')
        job = Job.objects.get(pk=job_id)
        if Application.objects.filter(job=job, applicant=self.request.user).exists():
            raise serializers.ValidationError('You have already applied for this job.')
        serializer.save(applicant=self.request.user, job=job)

class ListJobApplicationsView(generics.ListAPIView):
    """Allows a recruiter to see applications for one of their jobs."""
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsJobOwner]

    def get_queryset(self):
        job_id = self.kwargs.get('job_id')
        return Application.objects.filter(job_id=job_id)
    
class UpdateApplicationStatusView(generics.UpdateAPIView):
    """Allows a recruiter to update the status of an application."""
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsJobOwner]
    queryset = Application.objects.all()
    lookup_url_kwarg = 'application_id'