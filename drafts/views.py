from rest_framework import generics
from myfxlife_api.permissions import AuthorOnly
from .models import Draft
from .serializers import DraftSerializer


#Create LIST views so that a user can list his Draft post

class DraftList(generics.ListCreateAPIView):
    serializer_class = DraftSerializer
    permission_classes = [AuthorOnly]
    queryset = Draft.objects.all()


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Create Detail view for Draft post so users can retrieve, update and delete drafts
        
class DraftDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DraftSerializer
    permission_classes = [AuthorOnly]
    queryset = Draft.objects.all()