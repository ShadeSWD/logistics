from rest_framework.permissions import BasePermission


class IsVendor(BasePermission):
    def has_permission(self, request, view):
        try:
            request.user.is_vendor
        except AttributeError:
            return False
        if view.action in ('list', 'retrieve'):
            return True
        if view.action in ('create', 'update', 'partial_update', 'destroy'):
            return request.user.is_vendor
        return True
