from django.shortcuts import render
from django.shortcuts import  render, redirect
from django.contrib import messages
from django.views import View
from .models import *



def home(request):

    projets = Projet.objects.all()
    print("projets ", projets)
    return render(request, 'index.html', context={"projets": projets})

def detail(request, id):
    try:
        projet = Projet.objects.get(id=id)
    except Exception as e:
        pass

    return render(request, 'projet-single.html', context={"projet":projet})

def projet(request):

	projets = Projet.objects.all()
	return render(request, 'projet.html', context={"projets": projets})



class Contact(View):


	def get(self, request):

		return render(request,'contact.html')
	
		