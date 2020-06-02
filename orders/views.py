from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Category, Menu_Item

#@login_required
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'accounts/login.html', {"message": None})
    context = {
        "user": request.user,
        "menu_headings": Category.objects.filter(menu_heading=True)
    }
    return render(request, "orders/index.html", context)

    #return HttpResponse("Project 3: TODO")


def category(request, category_name):
    
    context = {
        "menu_items": Menu_Item.objects.filter(category__name=category_name, active=True),
    }
    return render(request, "orders/category.html", context)
