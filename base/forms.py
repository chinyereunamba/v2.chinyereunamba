from django import forms
from django.forms import ModelForm

from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
            'title': forms.TextInput(attrs={
                'placeholder':'Title'
            }),
            'headline': forms.Textarea(attrs={
                'placeholder':'Headline'
            }),
            'body': forms.Textarea(attrs={
                'placeholder':'Body'
            }),
            'github': forms.TextInput(attrs={
                'placeholder':'https://github.com/'
            }),
            'slug': forms.TextInput(attrs={
                'placeholder':'slug'
            }),
        }


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'Chinyere Unamba',
        'name': 'name'
    }))
    email = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={
        'placeholder': 'chinyereunamba@email.com',
        'name': 'email'
    }))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'Subject',
        'name': 'subject'
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': "Your message here...",
        'name': 'message'
    }))
