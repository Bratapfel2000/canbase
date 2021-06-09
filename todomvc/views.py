from django.shortcuts import render
from django.http import HttpResponse



def react(request):
    return render(request, 'todomvc/react.html')
