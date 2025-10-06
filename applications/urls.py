# applications/urls.py
from django.urls import path
from .views import ApplicationCreateView

urlpatterns = [
    path('create/', ApplicationCreateView.as_view(), name='application-create'),
]