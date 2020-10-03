from rest_framework import serializers
from postapp.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    sentiment_display = serializers.CharField(source='get_sentiment_display')
    class Meta:
        model = Post
        fields = [
            'id',
            'url',
            'sentiment_display',
            'sentiment',
            'body',
            'up_votes',
            'down_votes',
            'total_votes',
            'created',
            'update']