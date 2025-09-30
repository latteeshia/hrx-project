# users/urls.py - Correct version

from django.urls import path
from .views import RegisterView

urlpatterns = [
    # The path should be 'register/'
    path('register/', RegisterView.as_view(), name='register'),
]