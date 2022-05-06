from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request,"home/home.html")


def about_us(request):
    return render(request,"home/about_us.html")


def awards(request):
    return render(request,"home/awards.html")

def contact_us(request):
    return render(request,"home/contact_us.html")

def gallery(request):
    return render(request,"home/gallery.html")

def projects(request):
    return render(request,"home/projects.html")

def login(request):
    return render(request,"home/login.html")