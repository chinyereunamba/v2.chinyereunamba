from django.db import models
from django.utils.text import slugify

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

import PIL

# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.tag


class Project(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    headline = models.TextField(max_length=250, blank=True, null=True)
    image = models.ImageField(default="work-1.jpg", blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    active = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    github = models.URLField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.title)

            has_slug = Project.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count)
                has_slug = Project.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)
