from rest_framework import permissions


class ObjectOwner(permissions.BasePermission):
    sade_method = ['GET']

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in self.sade_method:
            return True
        else:
            return bool(obj.user == request.user)