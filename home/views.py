from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from home.models import Contact 

# Create your views here.
def home(request):
    # return HttpResponse("This is my homepage (/)")
    context = {'Name':'Yash', 'Course':'Django'}
    return render(request, 'home.html', context)

def about(request):
    # return HttpResponse("This is my aboutpage (/about)")
    return render(request, 'home.html')

def projects(request):
    # return HttpResponse("This is my projectspage (/projects)")
    return render(request, 'projects.html')

def contact(request):
    if request.method == "POST":
        
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name, email, phone, desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("The data has been written to the db")
    # return HttpResponse("This is my contactpage Thank you! (/contact)")
    return render(request, 'contact.html')
