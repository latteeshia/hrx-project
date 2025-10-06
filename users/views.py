# users/views.py
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer,MyTokenObtainPairSerializer 
from rest_framework_simplejwt.views import TokenObtainPairView # <-- ADD THIS IMPORT

User = get_user_model()

# This part you already have is correct
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

# ADD THIS NEW CLASS AT THE BOTTOM
class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer