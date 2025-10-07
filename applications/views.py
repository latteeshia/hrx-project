# applications/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Application
from jobs.models import Job  # CORRECTED: Import Job from the 'jobs' app
from .serializers import ApplicationCreateSerializer

class ApplicationCreateView(generics.CreateAPIView):
    serializer_class = ApplicationCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        job_id = request.data.get('job')
        
        # Check if the job actually exists before trying to apply
        if not Job.objects.filter(pk=job_id).exists():
            return Response(
                {'error': f'Invalid pk "{job_id}" - This job does not exist.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if the user has already applied
        if Application.objects.filter(job_id=job_id, applicant=request.user).exists():
            return Response(
                {'error': 'You have already applied for this job.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)