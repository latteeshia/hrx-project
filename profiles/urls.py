# profiles/urls.py
from django.urls import path
from .views import ProfileDetailView

urlpatterns = [
    # GET or PATCH /api/profile/
    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
]