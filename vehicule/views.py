from traceback import print_tb
from django.shortcuts import render
from django.shortcuts import  render, redirect
from .forms import ContactForm, NewUserForm, LocationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate #add this
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate, logout #add this
from django.views import View
from .models import *
from django.contrib.auth.decorators import login_required


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, str(form.errors))
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def home(request):

    vehicules = Vehicule.objects.all()
    return render(request, 'index.html', context={"vehicules": vehicules})

def detail(request, id):
    try:
        vehicule = Vehicule.objects.get(id=id)
    except Exception as e:
        pass

    return render(request, 'car-single.html', context={"vehicule":vehicule})

def car(request):

	vehicules = Vehicule.objects.all()
	return render(request, 'car.html', context={"vehicules": vehicules})


class Reservation(View):


	def get(self, request, id):

		return render(request,'reservation.html' ,context={"id":id})
		pass 
	
	@login_required(login_url='/login')
	def post(self, request, id=0):
		
		print(request.POST)
		form = LocationForm(request.POST)
		user = request.user
		print(user)
		vehicule = Vehicule.objects.get(id=request.POST['id'])

		if form.is_valid():
			location = form.save(commit=False)
			location.user = user 
			location.vehicule= vehicule
			print("Not ull")
			location.save()
			messages.success(request, "Registration successful." )
			return redirect('/')
		else:
			print(form.errors)
			messages.error(request, str(form.errors))
			return redirect("/reservation/"+str(id))


class Contact(View):


	def get(self, request):

		return render(request,'contact.html')
		 

	def post(self, request):
		
		print(request.POST)
		form = ContactForm(request.POST)

		if form.is_valid():
			contact = form.save(commit=True)
			messages.success(request, "Operation successful !" )
			return redirect('/contact')
		else:
			print(form.errors)
			messages.error(request, str(form.errors))
			return redirect("/contact")