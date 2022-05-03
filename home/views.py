from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    restaurant_list = Restaurant.objects.all()
    context = {'restaurant_list':restaurant_list}
    return render(request, 'home/index.html', context)

def my_login(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, "home/login.html", {
                "error": "Invalid username and/or password."
            })
    else:
        return render(request, "home/login.html")

def my_logout(request):
    logout(request)
    return redirect("/")

def my_signup(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["password2"]
        if password != confirmation:
            return render(request, "home/signup.html", {
                "error": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.set_password(password)
            user.is_active=True
            user.is_staff=True
            user.save()
        except IntegrityError:
            return render(request, "home/signup.html", {
                "error": "Username already taken."
            })
        login(request, user)
        return redirect("/")
    else:
        return render(request, "home/signup.html")

def view_profile(request):
    return render(request, 'home/view_profile.html')

def edit_profile(request):
    return render(request, 'home/edit_profile.html')

def delete_profile(request):
    # return render(request, 'home/delete_profile.html')
    pass