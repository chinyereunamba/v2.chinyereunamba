from django.urls import path
from django.conf.urls import handler403, handler404, handler500
from .views import *

# handler403 = 'base.views.error_403'
# handler404 = 'base.views.error_404'
# handler500 = 'base.views.error_500'

urlpatterns = [
    path('', home, name="home"),

    path('projects/', projects, name="projects"),
    path('projects/create-project/', createProject, name="createProject"),
    path('projects/<slug:slug>/', viewProject, name="viewProject"),
    path('projects/update-project/<slug:slug>/', updateProject, name="updateProject"),
    path('projects/delete-project/<slug:slug>/', deleteProject, name="deleteProject"),


    path('contact/', sendEmail, name="contact"),
]
