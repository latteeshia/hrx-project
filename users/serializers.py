# users/serializers.py

from rest_framework import serializers
from .models import CustomUser # Correctly imports CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser # Correctly uses CustomUser
        fields = ('id', 'username', 'email', 'password', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # This method correctly creates a new CustomUser and hashes the password
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', 'student')
        )
        return user