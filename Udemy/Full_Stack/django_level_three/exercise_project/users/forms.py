from . import models
from django import forms
from django.core import validators


class NewUserForm(forms.ModelForm):

    class Meta():
        model = models.User
        fields = '__all__'
