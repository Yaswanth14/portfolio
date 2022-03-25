from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("This is my homepage (/)")
    context = {'Name':'Yash', 'Course':'Django'}
    return render(request, 'home.html', context)

def about(request):
    # return HttpResponse("This is my aboutpage (/about)")
    return render(request, 'about.html')

def projects(request):
    # return HttpResponse("This is my projectspage (/projects)")
    return render(request, 'projects.html')

def contact(request):
    # return HttpResponse("This is my contactpage (/contact)")
    return render(request, 'contact.html')
