from django.shortcuts import render
from django.http import HttpResponse

def app(request):
    return HttpResponse('<em>This is my second app</em>')

def help(request):
    help_dict = {'get_help': 'Help Page'}
    return render(request, 'app/help.html', context=help_dict)

# Create your views here.
