# interviews/urls.py
from django.urls import path
from .views import InterviewListCreateView, InterviewDetailView

urlpatterns = [
    path('applications/<int:application_id>/interviews/', InterviewListCreateView.as_view(), name='interview-list-create'),
    path('interviews/<int:pk>/', InterviewDetailView.as_view(), name='interview-detail'),
]