from rest_framework.generics import ListAPIView

from blog.models import Post

from  .serializers import PostSerializer

class PostListAPIview(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer