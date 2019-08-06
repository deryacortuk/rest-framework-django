from rest_framework.permissions import BasePermission

class notAuthenticated(BasePermission):
    message ="you already have account"
    def has_permission(self, request, view):
        return not request.user and not request.user.is_authenticated


