from rest_framework import generics
from myfxlife_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

"""
Using generic views to create to achieve get and post functionality
"""
class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()



"""
Using generic views to get a single profile by its identity
and update it if user owns it.
"""  
class ProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()

