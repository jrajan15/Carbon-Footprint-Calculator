# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json


@csrf_exempt
def home(request):
    context = {}
    return render(request, 'home.html', context)

def calculate(request):
    context = {}
    return render(request, 'calculate.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)


def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode() == 200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData
