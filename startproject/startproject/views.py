from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello Wrold!,Welcome to Django Home Page")
    return render(request,'website/home.html')


def about(request):
    # return HttpResponse("Hello Wrold!,Welcome to Django About Page")
    return render(request,'website/about.html')

def contact(request):
    # return HttpResponse("Hello Wrold!,Welcome to Django Contact Page")
    return render(request,'website/contact.html')