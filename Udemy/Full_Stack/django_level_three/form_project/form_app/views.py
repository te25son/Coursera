from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'form_app/index.html')


def forms_page(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation Success")
            print(
                'Name: ' + form.cleaned_data['name'] + '\n' +
                'Email: ' + form.cleaned_data['email'] + '\n' +
                'Text: ' + form.cleaned_data['text'] 
            )

    return render(request, 'form_app/forms.html', {'form': form})
