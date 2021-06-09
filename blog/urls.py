from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, AddCommentView

urlpatterns = [
    #path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    path('sitemap/', views.sitemap, name='blog-sitemap'),
]