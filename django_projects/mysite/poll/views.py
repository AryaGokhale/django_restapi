from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return (HttpResponse("Hello this is pole index."))

def greet(request, name):
    return (HttpResponse(f"Hello,{name}."))