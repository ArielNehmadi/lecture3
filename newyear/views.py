from tkinter.messagebox import NO, YES
from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    if now.month == 10 and now.day == 24:
        is_newyear = YES
    else:
        is_newyear = NO
    return render(request,"newyear/index.html",{
        "now" : is_newyear
    }) 