from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Comment
from .forms import CommentForm
from django.urls import reverse_lazy

def home(request):
	context = {
		'posts': Post.objects.all()
		}
	return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('blog-home')

    


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
    	post = self.get_object()
    	if self.request.user == post.author:
    		return True
    	return False

class PostDeleteView(DeleteView,LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    success_url ='/'

    def test_func(self):
    	post = self.get_object()
    	if self.request.user == post.author:
    		return True
    	return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'Abouts'})

def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact'})

def sitemap(request):
    return render(request, 'blog/sitemap.html')
