from rest_framework import serializers
from web.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'content', 'content', 'category', 'published','fc', 'fm', 'uc', 'um']