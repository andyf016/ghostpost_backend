from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from postapp.models import Post
from postapp.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Create your views here.
