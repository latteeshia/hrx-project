# interviews/serializers.py
from rest_framework import serializers
from .models import Interview
from applications.serializers import ApplicationSerializer

class InterviewSerializer(serializers.ModelSerializer):
    # ... (this class stays the same)
    application = ApplicationSerializer(read_only=True)

    class Meta:
        model = Interview
        fields = ['id', 'application', 'scheduled_at', 'interview_type', 'status', 'notes']

class InterviewCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating (scheduling) a new interview.
    """
    # --- MAKE THIS CHANGE ---
    # This field will be populated by the view, not the user.
    application = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Interview
        # We list all fields so the response after creation is complete.
        fields = ['id', 'application', 'scheduled_at', 'interview_type', 'status', 'notes']