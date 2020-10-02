from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from postapp.models import Post
from postapp.serializers import PostSerializer
from django.utils import timezone

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def up_vote(self, request, pk=None):
        post = self.get_object()
        #serializer = self.get_serializer(post, many=False)
        post.up_votes = post.up_votes + 1
        post.total_votes = post.total_votes +1
        post.update = timezone.now()
        post.save()
        return Response({'status': 'upvote!'})
    
    @action(detail=True, methods=['post'])
    def down_vote(self, request, pk=None):
        post = self.get_object()
        #serializer = self.get_serializer(post, many=False)
        post.down_votes = post.down_votes + 1
        post.total_votes = post.total_votes - 1
        post.update = timezone.now()
        post.save()
        return Response({'status': 'Downvote!'})
    
    @action(detail=False)
    def list_boasts(self, request):
        boasts = Post.objects.filter(sentiment='b')

        page = self.paginate_queryset(boasts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(boasts, many=True)
        return Response(serializer.data)
    
    @action(detail=False)
    def list_roasts(self, request):
        boasts = Post.objects.filter(sentiment='r')

        page = self.paginate_queryset(boasts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(boasts, many=True)
        return Response(serializer.data)
    
    @action(detail=False)
    def highest_rated(self, request):
        rated = Post.objects.all().order_by('-total_votes')

        page = self.paginate_queryset(rated)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(rated, many=True)
        return Response(serializer.data)
