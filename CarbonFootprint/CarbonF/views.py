# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {}
    return render(request, 'home.html', context)

def calculate(request):
    context = {}
    return render(request, 'calculate.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)
