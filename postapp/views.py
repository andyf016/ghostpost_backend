from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from postapp.models import Post
from postapp.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

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
