from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    return render(request, "movie/home.html", {"name": "Jeronimo"})

def about(request):
    return render(request, "movie/about.html")
