from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def login_view(request):

    if request.method == 'GET':
        return render(request, "accounts/login.html", {"message": None})


    elif request.method == 'POST':
        # AUTHENTICATE & LOGIN USER
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # THIS WILL ALSO START A SESSION
            # Redirect to a success page.
            return HttpResponseRedirect(reverse("index")) # DOES THIS NEED TO BE FIXED?

        else:
            # Return an 'invalid login' error message.
            return render(request, "accounts/login.html", {"message": "Invalid credentials."})


def logout_view(request):
    logout(request) # COMPLETELY CLEANS OUT SESSION DATA
    # Redirect to a success page.
    return render(request, "accounts/login.html", {"message": "Logged out."})


def register_view(request):
    
    if request.method == 'GET':
        return render(request, "accounts/register.html", {'message': None})

    elif request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']

        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            return render(request, "accounts/register.html", {'message': 'Username already exists'})

        if password1 != password2:
            return render(request, "accounts/register.html", {'message': 'Passwords do not match'})

        user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
        user.save()
        
        return render(request, "accounts/login.html", {"message": "Registration Successful!"})
