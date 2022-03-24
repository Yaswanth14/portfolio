from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is my homepage (/)")

def about(request):
    return HttpResponse("This is my aboutpage (/about)")

def projects(request):
    return HttpResponse("This is my projectspage (/projects)")

def contact(request):
    return HttpResponse("This is my contactpage (/contact)")
