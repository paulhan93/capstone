from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>")  # string of HTML code
    return render(request, "home.html", {})    # render page using a template file

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})