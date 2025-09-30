from django.urls import path
from . import views

urlpatterns = [
    # When the user visits the root of the 'projects' app (e.g., /projects/)
    # call the view function named 'project_index'
    path('', views.project_index, name='project_index'),
]