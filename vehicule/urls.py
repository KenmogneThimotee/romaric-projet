from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name= "logout"),
    path('reservation/<int:id>', Reservation.as_view(), name='reservation'),
    #path('reservation', Reservation.as_view(), name='reservation_post'),
    path('detail/<int:id>', detail, name='detail'),
    path('contact', Contact.as_view(), name='contact'),
    path('car', car, name='car')
]