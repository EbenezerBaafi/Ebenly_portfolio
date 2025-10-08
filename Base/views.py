from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact


# Create your views here.
def home(request):
    return render(request, 'home.html')
def contact(request):
    if request.method=="POST":
        print('Post')
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        content = request.POST.get('content')
        print(name,email,number,content)

        if len(name) > 1 and len(name)<30:
            pass
        else:
            messages.error(request, 'Name must be between 1 and 30 characters long')
            return render(request, 'home.html')


        if len(email) > 1 and len(email)<30:
            pass
        else:
            messages.error(request, 'Email must be between 1 and 30 characters long')
            return render(request, 'home.html')

        if len(number) > 1 and len(number)<13:
            pass
        else:
            messages.error(request, 'Number must be between 1 and 13 characters long')
            return render(request, 'home.html')
        ins = models.Contact(name=name,email=email,number=number,content=content)
        ins.save()


