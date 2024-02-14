from django.db.models import Count
from rest_framework import generics, permissions, filters
from myfxlife_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


#Create LIST views so that users can list posts and create posts

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count = Count('comment', distinct=True),
        likes_count =Count('likes', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = [
        'comments_count',
        'likes_count',
    ]
    search_fields = [
        'owner__username',
        'title'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Create Detail view for post so users can retrieve, update and delete posts
        
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count = Count('owner__comment', distinct=True),
        likes_count =Count('owner__like', distinct=True)
    ).order_by('-created_at')