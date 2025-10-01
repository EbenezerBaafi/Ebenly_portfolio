from django.shortcuts import render, redirect
from .models import Portfolio
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

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

def Contact():
    if request.method == 'Post':
        # Create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)

        # Check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            emaail = form.cleaned_date['email']
            message = form.cleaned_data['message']
            subject = form.cleaned_data['subject']

            full_subject = f"New contact form submission: {subject}"
            full_message = f"Message from: {name}\nEmail:{email}\n\nMessage:\n\n{message}"

        try:
            # Send email
            send_email(
                full_subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.Default_FROM_EMAIL],
                fail_silently=False,
            )
            # if successful, redirect to a 'thank you' page or back to home
            return redirect('project_index')
        except Exception as e:
            # Log the error (you can use Django's logging framework)
            print(f"Error sending email: {e}")
            # Optionally, you can add a message to the user about the failure

    else:
        # If a GET (or any other method) we'll create a blank form
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'projects/contact.html', context)