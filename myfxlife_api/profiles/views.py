from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from myfxlife_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

"""
Using generic views to create List views for the Profile Model
"""
class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count = Count('owner__post', distinct=True),
        followers_count = Count('owner__followed', distinct=True),
        following_count = Count('owner__following', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
    ]

    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
    ]



"""
Using generic views to create Retrieve and Update views for
a singled out profile by id
"""  
class ProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count = Count('owner__post', distinct=True),
        followers_count = Count('owner__followed', distinct=True),
        following_count = Count('owner__following', distinct=True)
    ).order_by('-created_at')

