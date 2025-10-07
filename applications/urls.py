# applications/urls.py
from django.urls import path
from .views import ApplicationCreateView

urlpatterns = [
    # The full URL will be /api/applications/create/
    path('create/', ApplicationCreateView.as_view(), name='application-create'),
]