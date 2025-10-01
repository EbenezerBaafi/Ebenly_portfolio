from django import forms
from .models import Portfolio

class ContactForm(forms.Form):
    # fields for name, email, message
    name = forms.CharField(max_length=100, label='Your Name', required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)