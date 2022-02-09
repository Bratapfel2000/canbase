# api/views.py
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer


class PostAPIView(generics.ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer