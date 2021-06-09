from django.urls import path
from . import views

urlpatterns = [
    path('', views.somu_overview, name='somu-overview'),
]