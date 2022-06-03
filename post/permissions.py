from rest_framework import permissions


class CommentAccesse(permissions.BasePermission):
    safe_method = ['GET']

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # just post owner and comment owner can delete that
        if request.method in self.safe_method:
            return True
        else:
            return bool((obj.user == request.user) or (obj.post.user == request.user))