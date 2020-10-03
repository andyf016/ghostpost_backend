from rest_framework import serializers
from postapp.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        sentiment_display = serializers.CharField(source='get_sentiment_display')
        fields = [
            'id',
            'url',
            'sentiment',
            'body',
            'up_votes',
            'down_votes',
            'total_votes',
            'created',
            'update']