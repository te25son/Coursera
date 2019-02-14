from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse('<em>This is my second app</em>')

# Create your views here.
