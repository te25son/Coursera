from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'form_app/index.html')


def forms_page(request):
    form = forms.FormName()
    return render(request, 'form_app/forms.html', {'form': form})
