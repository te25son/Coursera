from django.shortcuts import render


def index(request):
    return render(request, 'form_app/index.html')


def forms(request):
    return render(request, 'form_app/forms.html')
