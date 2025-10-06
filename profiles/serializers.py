# profiles/serializers.py
from rest_framework import serializers
from .models import Profile
from users.serializers import RegisterSerializer

class ProfileSerializer(serializers.ModelSerializer):
    user = RegisterSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'full_name', 'bio', 'resume']