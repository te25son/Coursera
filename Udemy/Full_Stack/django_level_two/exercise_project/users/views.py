from django.shortcuts import render
from users.models import User


def home(request):
    return render(request, 'users/index.html')


def users(request):
    users_list = User.objects.order_by('first_name')
    users_dict = {
        'site_users': users_list,
    }
    return render(request, 'users/users.html', context=users_dict)
