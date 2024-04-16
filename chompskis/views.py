from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddChompskiForm
from .models import GnomeChompskis, Swarm
#request handler

def home(request):
    chompskis = GnomeChompskis.objects.all()
    
    #check if user is logged in
    if request.method == 'POST':
        # Process login form data
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('home')
    else:
        
        return render(request, 'home.html', {'chompskis': chompskis})
        
def swarms(request):
    swarms = Swarm.objects.all()
    return render(request, "swarms.html", {'swarms':swarms} )

def delete_chompski(request, chompskis_id):
    if request.user.is_authenticated:
        chompskis = GnomeChompskis.objects.get(pk=chompskis_id)
        chompskis.delete()
        messages.success(request, "Chompski 'deleted'")
        return redirect('home')
    else:
        messages.error(request, "Must be logged in to delete.")
        return redirect('home')

def add_chompski(request):
    form = AddChompskiForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST' and form.is_valid():
            chompski = form.save(commit=False)
            chompski.save()
            messages.success(request, "Chompski added.")
            return redirect('home')
        return render(request, "add_chompski.html", {'form':form})
    else:
        messages.error(request, "Must be logged in to delete.")
        return redirect('home')

def details(request, chompskis_id):
    if request.user.is_authenticated:
        chompskis = GnomeChompskis.objects.get(pk=chompskis_id)
        return render(request, "details.html", {'chompskis':chompskis})
    else:
        messages.error(request, "Must be logged in to view details.")
        return redirect('home')
    
def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def logout_user(request):
    logout(request)
    messages.success(request, "Logout successful.")
    return redirect('home')

def menu(request):
    return render(request, "menu.html")

def functions(request):
    return render(request, "functions.html")
