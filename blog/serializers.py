from rest_framework import serializers
from .models import Post
	class PostSerializer(serializers.ModelSerializer):
		class Meta:
			fields = ('title', 'content', 'date_posted', 'author',)
			model = Post