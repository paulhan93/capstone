from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>Home Page</h1>")  # string of HTML code

def about_view(*args, **kwargs):
    return HttpResponse("<h1>About Page</h1>")

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")  

def social_view(*args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")  