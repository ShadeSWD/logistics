from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        if view.action in ('create', 'list', 'retrieve', 'update', 'partial_update', 'destroy'):
            return request.user.is_staff
        return True
