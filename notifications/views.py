from django.db.models import Count
from rest_framework import generics
from .serializers import NotificationSerializer
from .models import Notification
from myfxlife_api.permissions import IsOwnerOrReadOnly


class NotificationList(generics.ListAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.annotate(
        notification_count = Count('owner__notification', distinct=True) 
    ).order_by('-created_at')



class NotificationDetail(generics.RetrieveDestroyAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Notification.objects.annotate(
        notification_count = Count('owner__notification', distinct=True)
    ).order_by('-created_at')