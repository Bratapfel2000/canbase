from django.shortcuts import render
from django.http import HttpResponse

def somu_overview(request):
    return render(request, 'sondermuenz/overview.html')

