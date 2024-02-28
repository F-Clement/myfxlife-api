from rest_framework import permissions

#Permissions to be used in our views when we want
#only user who own a resource or users allowed to have various CRUD functionalities


class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.owner == request.user
  

class IsOwnerOrFollowerOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.user in obj.owner.following.all():
      return True
    return obj.owner == request.user

