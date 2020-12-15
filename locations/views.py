from django.shortcuts import render
from django.http import HttpResponse
from .models import WorldBorder, ToDoList


# Create your views here.
def index(response, _id):
    ls = ToDoList.objects.get(id=_id)
    return render(response, "locations/base.html", {})


def home(response):
    return render(response, "locations/home.html", {})

