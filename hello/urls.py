
from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index, name = "index"),
    path("ariel",views.ariel,name= 'ariel'),
    path("<str:name>",views.greet,name= 'greet')
]