from django.shortcuts import render
from users.models import User
from users.forms import NewUserForm


def home(request):
    return render(request, 'users/index.html')


def users(request):
    form = NewUserForm()

    if request.method == "POST":                # if the user hits submit on form
        form = NewUserForm(request.POST)

        if form.is_valid():                     # and if that form is valid...
            form.save(commit=True)
            return home(request)

        else:
            print("ERROR: Form invalid.")

    return render(request, 'users/users.html', {'form': form})
