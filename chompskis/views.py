from audioop import avg
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddChompskiForm, AddSwarmForm
from .models import GnomeChompskis, Swarm
from django.db.models import Avg

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
 
def statistics(request):
    if request.user.is_authenticated:
        swarms = Swarm.objects.all()
        for swarm in swarms:
            quantity = GnomeChompskis.objects.filter(swarm_id=swarm.swarm_id).count()
            setattr(swarm, 'quantity', quantity)
        chompskis = GnomeChompskis.objects.all()
        total_chompskis = chompskis.count()
        total_swarms = swarms.count()
        average_age = chompskis.aggregate(Avg('age'))
        average_quantity = GnomeChompskis.objects.values('swarm_id').annotate(avg_quantity=Avg('swarm_id')).aggregate(Avg('avg_quantity'))        
        return render(request, "statistics.html", {'total_chompskis':total_chompskis, 'total_swarms':total_swarms, 'average_age':average_age, 'average_quantity':average_quantity})
    else:
        messages.error(request, "Must be logged in to delete.")
        return redirect('home')

def swarms(request):
    if request.user.is_authenticated:
        swarms = Swarm.objects.all()
        for swarm in swarms:
            quantity = GnomeChompskis.objects.filter(swarm_id=swarm.swarm_id).count()
            setattr(swarm, 'quantity', quantity)
        return render(request, "swarms.html", {'swarms':swarms})
    else:
        messages.error(request, "Must be logged in to delete.")
        return redirect('home')
    
def swarm_sortby_name(request):
    if request.user.is_authenticated:
        swarms = Swarm.objects.all().order_by('name')
        for swarm in swarms:
            quantity = GnomeChompskis.objects.filter(swarm_id=swarm.swarm_id).count()
            setattr(swarm, 'quantity', quantity)
        return render(request, "swarms.html", {'swarms':swarms})
    else:
        messages.error(request, "Must be logged in to delete.")
        return redirect('home')

def swarm_sortby_quantity(request):
    if request.user.is_authenticated:
        swarms = Swarm.objects.all()
        for swarm in swarms:
            quantity = GnomeChompskis.objects.filter(swarm_id=swarm.swarm_id).count()
            setattr(swarm, 'quantity', quantity)
        swarms = sorted(swarms, key=lambda x: x.quantity)
        return render(request, "swarms.html", {'swarms':swarms})
    else:
        messages.error(request, "Must be logged in to delete.")
        return redirect('home')

def swarm_sortby_latitude(request):
    if request.user.is_authenticated:
        swarms = Swarm.objects.all().order_by('latitude')
        for swarm in swarms:
            quantity = GnomeChompskis.objects.filter(swarm_id=swarm.swarm_id).count()
            setattr(swarm, 'quantity', quantity)
        return render(request, "swarms.html", {'swarms':swarms})
    else:
        messages.error(request, "Must be logged in to delete.")
        return redirect('home')


def swarm_sortby_longitude(request):
    if request.user.is_authenticated:
        swarms = Swarm.objects.all().order_by('longitude')
        for swarm in swarms:
            quantity = GnomeChompskis.objects.filter(swarm_id=swarm.swarm_id).count()
            setattr(swarm, 'quantity', quantity)
        return render(request, "swarms.html", {'swarms':swarms})
    else:
        messages.error(request, "Must be logged in to delete.")
        return redirect('home')

def delete_swarm(request, swarm_id):
    if request.user.is_authenticated:
        swarms = Swarm.objects.get(pk=swarm_id)
        swarms.delete()
        messages.success(request, "swarm 'deleted'")
        return redirect('swarms')
    else:
        messages.error(request, "Must be logged in to delete.")
        return redirect('home')
    
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
    
def add_swarm(request):
    form = AddSwarmForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST' and form.is_valid():
            swarm = form.save(commit=False)
            swarm.save()
            messages.success(request, "swarm added.")
            return redirect('swarms')
        return render(request, "add_swarm.html", {'form':form})
    else:
        messages.error(request, "Must be logged in to delete.")
        return redirect('home')

def update_swarm(request, swarm_id):
    if request.user.is_authenticated:
        current_details = Swarm.objects.get(pk=swarm_id)
        form = AddSwarmForm(request.POST or None, instance=current_details)
        if form.is_valid():
            form.save()
            messages.success(request, "Swarm updated.")
            return redirect('swarms')
        return render(request, "update_swarm.html", {'form':form})
    else:
        messages.error(request, "Must be logged in to update.")
        return redirect('home')

def update_chompski(request, chompskis_id):
    if request.user.is_authenticated:
        current_details = GnomeChompskis.objects.get(pk=chompskis_id)
        form = AddChompskiForm(request.POST or None, instance=current_details)
        if form.is_valid():
            form.save()
            messages.success(request, "Chompski updated.")
            return redirect('home')
        return render(request, "update_chompski.html", {'form':form})
    else:
        messages.error(request, "Must be logged in to update.")
        return redirect('home')

def details(request, chompskis_id):
    if request.user.is_authenticated:
        chompskis = GnomeChompskis.objects.get(pk=chompskis_id)
        return render(request, "details.html", {'chompskis':chompskis})
    else:
        messages.error(request, "Must be logged in to view details.")
        return redirect('home')

def chompski_sortby_swarm(request):
    chompskis = GnomeChompskis.objects.all().order_by('swarm_id')
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
    
def chompski_sortby_teeth(request):
    chompskis = GnomeChompskis.objects.all().order_by('no_teeth')
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

def chompski_sortby_weight(request):
    chompskis = GnomeChompskis.objects.all().order_by('weight')
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

def chompski_sortby_height(request):
    chompskis = GnomeChompskis.objects.all().order_by('height')
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

def chompski_sortby_age(request):
    chompskis = GnomeChompskis.objects.all().order_by('age')
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
    
def chompski_sortby_name(request):
    chompskis = GnomeChompskis.objects.all().order_by('name')
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

def swarm_details(request, swarm_id):
    if request.user.is_authenticated:
        swarm = Swarm.objects.get(pk=swarm_id)
        quantity = GnomeChompskis.objects.filter(swarm_id=swarm_id).count()
        return render(request, "swarm_details.html", {'swarm':swarm, 'quantity':quantity})
    else:
        messages.error(request, "Must be logged in to view details.")
        return redirect('home')
    
def logout_user(request):
    logout(request)
    messages.success(request, "Logout successful.")
    return redirect('home')

def menu(request):
    return render(request, "menu.html")

def functions(request):
    return render(request, "functions.html")
