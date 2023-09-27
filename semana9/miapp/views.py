from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    title = "Inicio"
    return render(request, 'miapp/index.html')

def carreras(request):
    title = "carreras"
    return render(request, 'miapp/carreras.html')