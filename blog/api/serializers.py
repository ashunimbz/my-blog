from rest_framework.serializers import ModelSerializer

from blog.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model =  Post
        fields = [
            'title',
            'author' ,
            'text',
            'published_date',
            'id',
        ]