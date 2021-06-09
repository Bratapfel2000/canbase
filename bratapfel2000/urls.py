from django.urls import path
from . import views

urlpatterns = [
    path('', views.ba2k_home, name='ba2k-home'),
    #path('about/', views.ba2k_about, name='ba2k-about'),
    path('main/', views.ba2k_main, name='ba2k-main'),
    path('experiments/', views.ba2k_experiments, name='ba2k-experiments'),
    path('zwischenspeicher/', views.ba2k_zwischenspeicher, name='ba2k-zwischenspeicher'),
    path('test-area-1/', views.ba2k_testarea_1, name='ba2k_testarea_1'),
    path('django-setup/', views.django_setup, name='ba2k-django-setup'),
]