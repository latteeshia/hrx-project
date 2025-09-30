# users/views.py

from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import UserSerializer # Changed to UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer # Changed to UserSerializer