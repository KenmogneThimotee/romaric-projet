from distutils.command.upload import upload
from operator import mod
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class Projet(models.Model):

    name = models.CharField(max_length=50)
    description = RichTextField()
    shorter_description = models.CharField(max_length=45)
    image = models.ImageField(upload_to="media")

    def __str__(self) -> str:
        return self.name + " -- " + self.shorter_description

class Contact(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()