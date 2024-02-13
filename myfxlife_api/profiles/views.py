from rest_framework import generics, permissions
from myfxlife_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListCreateAPIView):
    """
    Using generic views to create to achieve get and post functionality
    """
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Profile.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
