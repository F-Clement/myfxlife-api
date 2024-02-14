from rest_framework import generics, permissions
from myfxlife_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


#Create LIST views so that users can list posts and create posts

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Create Detail view for post so users can retrieve, update and delete posts
        
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()