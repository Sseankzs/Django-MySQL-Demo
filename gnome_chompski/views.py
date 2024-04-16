from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#request handler

def home(request):
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
        return render(request, 'home.html')
        
        


def logout_user(request):
    logout(request)
    messages.success(request, "Logout successful.")
    return redirect('home')

def menu(request):
    return render(request, "menu.html")

def functions(request):
    return render(request, "functions.html")
