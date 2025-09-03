from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'body', 'created_at', 'active']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True) 

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'author_name',
            'published',
            'created_at',
            'updated_at',
            'comments',  
        ]
