from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL now points to home
    path('projects/', views.project_index, name='project_index'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('contact/', views.Contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]