# analytics/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from jobs.models import Job
from applications.models import Application
from django.db.models import Count
from .permissions import IsAdminUser

User = get_user_model()

class AnalyticsDashboardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        total_students = User.objects.filter(role='student').count()
        
        students_placed = User.objects.filter(application__status='Accepted').distinct().count()
        
        total_jobs = Job.objects.count()
        
        #                             HERE is the new fix
        #                                  |
        #                                  V
        top_companies = Application.objects.filter(status='Accepted') \
            .values('job__company') \
            .annotate(hired_count=Count('applicant', distinct=True)) \
            .order_by('-hired_count')[:5]

        data = {
            'total_students': total_students,
            'students_placed': students_placed,
            'placement_percentage': round((students_placed / total_students * 100), 2) if total_students > 0 else 0,
            'total_jobs': total_jobs,
            'top_hiring_companies': list(top_companies)
        }
        
        return Response(data)