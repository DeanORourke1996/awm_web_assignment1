from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Welcome, this is the homepage. Please log in or sign up...")


def detail(request, username):
    response = "Welcome %s to the HotLocations Web App."
    HttpResponse(response % username)


