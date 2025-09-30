# interviews/views.py
from rest_framework import generics, permissions
from .models import Interview
from applications.models import Application
from .serializers import InterviewSerializer, InterviewCreateSerializer
from jobs.permissions import IsJobOwner

class InterviewListCreateView(generics.ListCreateAPIView):
    """
    List all interviews for a specific application or create a new one.
    """
    permission_classes = [permissions.IsAuthenticated, IsJobOwner]
    
    def get_queryset(self):
        application_id = self.kwargs['application_id']
        return Interview.objects.filter(application_id=application_id)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return InterviewCreateSerializer
        return InterviewSerializer

    def perform_create(self, serializer):
        application = Application.objects.get(pk=self.kwargs['application_id'])
        serializer.save(application=application)

class InterviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific interview.
    """
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = [permissions.IsAuthenticated, IsJobOwner]