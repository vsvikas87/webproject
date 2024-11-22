from django.http import HttpResponse
from django.shortcuts import render as rander

def home(request):
    return rander(request, 'index.html')

def about(request):
    return HttpResponse("<h1>Welcome to Vikas's Django Project: About page</h1>")

def contact(request):
    return HttpResponse("<h1>Welcome to Vikas's Django Project: Contact page</h1>")