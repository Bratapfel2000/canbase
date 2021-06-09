from django.shortcuts import render
from django.http import HttpResponse


def ba2k_home(request):
    return render(request, 'bratapfel2000/ba2k_home.html')

def ba2k_about(request):
    return HttpResponse('<h1>Bratapfel About</h1>')

def ba2k_main(request):
    return render(request, 'bratapfel2000/ba2k_main.html')

def ba2k_experiments(request):
    return render(request, 'bratapfel2000/ba2k_experiments.html')

def ba2k_zwischenspeicher(request):
    return render(request, 'bratapfel2000/ba2k_zwischenspeicher.html')

def ba2k_testarea_1(request):
    return render(request, 'bratapfel2000/ba2k_test-area-1.html')

def django_setup(request):
    return render(request, 'bratapfel2000/ba2k_django-setup.html')