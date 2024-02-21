from rest_framework import generics, permissions
from .models import Draft
from .serializers import DraftSerializer


#Create LIST views so that a draft owner can list his draft posts

class DraftList(generics.ListCreateAPIView):
    serializer_class = DraftSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Draft.objects.all()


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return (self.queryset.filter(owner=self.request.user))


# Create Detail view for Draft post so only owner can retrieve, update and delete drafts
        
class DraftDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DraftSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Draft.objects.all()

    def get_queryset(self):
        return (self.queryset.filter(owner=self.request.user))
    