from rest_framework.viewsets import ModelViewSet
from web.models import Post
from web.api.serializers import PostSerializer
from web.api.permissions import IsAdminOrReadOnly

class PostViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()