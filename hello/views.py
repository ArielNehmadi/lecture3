
import http
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("hello world!")

def ariel(request):
    return render(request,"hello/index.html")
def greet(request,name):
    return render(request,"hello/greet.html",{
        "name":name.capitalize()
        })