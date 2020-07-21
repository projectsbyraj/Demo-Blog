from rest_framework import serializers

from .models import Blog, Comment


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Blog
        fields = ('url', 'title', 'text', 'owner')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    blog = serializers.ReadOnlyField(source='blogs.title')

    class Meta:
        model = Comment
        fields = ('url', 'text', 'owner', 'blog')
