from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    dict = {'insert_me': 'This text is brought to you by hello/views.py'}
    return render(request, 'hello/index.html', context=dict)
