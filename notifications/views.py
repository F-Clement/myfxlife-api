# from django.db.models import Count
from rest_framework import generics, permissions
from .serializers import NotificationSerializer
from .models import Notification
from myfxlife_api.permissions import IsOwnerOrFollowerOnly

# Restring notifications views only to owner and followers.

class NotificationList(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsOwnerOrFollowerOnly, permissions.IsAuthenticated]
    queryset = Notification.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Notification.objects.filter(owner__followed__in=self.request.user.following.all())
    
    def get_queryset(self):
        return (self.queryset.filter(owner=self.request.user))



class NotificationDetail(generics.RetrieveDestroyAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsOwnerOrFollowerOnly, permissions.IsAuthenticated]
    queryset = Notification.objects.all()

    def get_queryset(self):
        return Notification.objects.filter(owner__followed__in=self.request.user.following.all())
    
    def get_queryset(self):
        return (self.queryset.filter(owner=self.request.user))
