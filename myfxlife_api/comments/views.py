from rest_framework import generics, permissions
from myfxlife_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


# View to List comments or create a comment if logged in.

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



# View to Retrieve a comment, or update or delete it by id if you own it.
        
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()