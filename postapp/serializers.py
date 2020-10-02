from rest_framework import serializers
from postapp.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'sentiment',
            'body',
            'up_votes',
            'down_votes',
            'total_votes',
            'created',
            'update']