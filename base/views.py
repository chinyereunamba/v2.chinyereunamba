from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .models import *
from .forms import *

# Create your views here.


def home(request):
    posts = Project.objects.all()[:3]

    context = {
        "posts": posts,
    }
    return render(request, "base/index.html", context=context)



def projects(request):
    posts = Project.objects.all()

    context = {
        "posts": posts,
    }
    return render(request, "base/projects.html", context=context)


@login_required()
def createProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect('projects')

    action = 'Create Project'
    context = {
        'form': form,
        'option': action,
    }

    return render(request, "base/create-project.html", context=context)


@login_required()
def updateProject(request, slug):
    post = Project.objects.get(slug=slug)
    form = ProjectForm(instance=post)
    action = 'Update Project'
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()

        return redirect('viewProject', slug=slug)

    context = {
        'form': form,
        'option': action,
    }

    return render(request, "base/create-project.html", context=context)


def viewProject(request, slug):
    post = Project.objects.get(slug=slug)

    context = {
        'post': post
    }

    return render(request, "base/viewProject.html", context=context)


def deleteProject(request, slug):
    post = Project.objects.get(slug=slug)

    if request.method == "POST":
        post.delete()
        return redirect('projects')

    context = {
        'post': post,
    }
    return render(request, 'base/delete.html', context=context)


def sendEmail(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            html = render_to_string('base/email.html', {
                'name': name,
                "email": email,
                'subject': subject,
                'message': message
            })

            send_mail(
                subject=subject,
                message=message,
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=True,
                html_message=html
            )
        return render(request, 'base/email_sent.html')


    context = {
        'form': form,
    }

    return render(request, 'base/contact.html', context)
