from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world! <a href=\"/rango/about\">About Page</a>")

def about(request):
	return HttpResponse("Rango says here is the about page. <a href=\"/rango/\">Index</a>")	