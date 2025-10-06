# applications/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Application
from jobs.models import Job
from .serializers import ApplicationCreateSerializer

class ApplicationCreateView(generics.CreateAPIView):
    serializer_class = ApplicationCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            job_id = request.data.get('job')
            if not job_id:
                return Response({'error': 'Job ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

            if not Job.objects.filter(pk=job_id).exists():
                return Response({'error': f'Invalid pk "{job_id}" - This job does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

            if Application.objects.filter(job_id=job_id, applicant=request.user).exists():
                return Response(
                    {'error': 'You have already applied for this job.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            return super().create(request, *args, **kwargs)
        
        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'An unexpected server error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)