from rest_framework import permissions
from .models import *


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if str(request.user.groups.all()[0]) == "ADMIN":
                return True
        return False


class IsManager(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            if str(request.user.groups.all()[0]) == "Manager":
                return True
            return False
        return bool(True)

