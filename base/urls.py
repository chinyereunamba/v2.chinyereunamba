from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),

    path('projects/', projects, name="projects"),
    path('create-project/', createProject, name="createProject"),
    path('projects/<slug:slug>/', viewProject, name="viewProject"),
    path('update-project/<slug:slug>/', updateProject, name="updateProject"),
    path('delete-project/<slug:slug>/', deleteProject, name="deleteProject"),


    path('contact/', sendEmail, name="contact"),
]
