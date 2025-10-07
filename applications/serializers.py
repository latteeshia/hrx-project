# applications/serializers.py
from rest_framework import serializers
from .models import Application
from jobs.models import Job          # CORRECTED: Import Job from the 'jobs' app
from users.models import CustomUser  # CORRECTED: Import your CustomUser model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'role')

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('job',)

class ApplicationDetailSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    applicant = UserSerializer(read_only=True)

    class Meta:
        model = Application
        fields = ('id', 'job', 'applicant', 'date_applied')