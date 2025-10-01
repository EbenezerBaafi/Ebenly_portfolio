from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_index, name='project_index'),  # Empty string for root URL
    path('', views.home, name='home'),  # New home page
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('contact/', views.Contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]