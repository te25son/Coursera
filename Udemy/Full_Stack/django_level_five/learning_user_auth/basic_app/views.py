from django.shortcuts import render


def index(request):
    return render(request, 'basic_app/index.html')


def register(request):
    return render(request, 'basic_app/registration.html')
