from django.db.models import Count
from rest_framework import generics
from .serializers import NotificationSerializer
from .models import Notification
from myfxlife_api.permissions import IsOwnerOrFollowerOnly


class NotificationList(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsOwnerOrFollowerOnly]
    queryset = Notification.objects.annotate(
        notification_count = Count('owner__notification', distinct=True) 
    ).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class NotificationDetail(generics.RetrieveDestroyAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsOwnerOrFollowerOnly]
    queryset = Notification.objects.annotate(
        notification_count = Count('owner__notification', distinct=True)
    ).order_by('-created_at')