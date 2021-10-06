from django.http import HttpResponse 
from django.shortcuts import render

def head(request):
    return HttpResponse("<h1>Hello World</h1>")

def homepage(request):
    return render(request, 'index.html')