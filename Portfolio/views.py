from django.shortcuts import render
from .models import Portfolio

def project_index(request):
    projects = Portfolio.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/index.html', context)