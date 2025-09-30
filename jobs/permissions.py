# jobs/permissions.py
from rest_framework import permissions

class IsJobOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of a job to edit or see related objects.
    """
    def has_object_permission(self, request, view, obj):
        # For a Job object itself
        if hasattr(obj, 'posted_by'):
            return obj.posted_by == request.user
        # For an Application object
        if hasattr(obj, 'job'):
            return obj.job.posted_by == request.user
        # For an Interview object
        if hasattr(obj, 'application'):
            return obj.application.job.posted_by == request.user
        return False