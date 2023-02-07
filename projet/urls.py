from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:id>', detail, name='detail'),
    path('contact', Contact.as_view(), name='contact'),
    path('projets', projet, name='projets')
]