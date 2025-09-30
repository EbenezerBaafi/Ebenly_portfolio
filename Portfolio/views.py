from django.shortcuts import render, get_object_or_404
from .models import Portfolio

def project_index(request):
    projects = Portfolio.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/index.html', context)

def project_detail(request, pk):
    # Fetch the project by primary key
    projects = Portfolio.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/detail.html', context)