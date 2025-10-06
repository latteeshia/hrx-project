# users/permissions.py
from rest_framework.permissions import BasePermission

class IsRecruiterOrReadOnly(BasePermission):
    """
    Allows anyone to view (GET), but only recruiters to create (POST).
    """
    def has_permission(self, request, view):
        # Allow all "safe" methods (GET, HEAD, OPTIONS) for anyone.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        # For other methods (like POST), check if the user is an authenticated recruiter.
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.role == 'recruiter'
        )