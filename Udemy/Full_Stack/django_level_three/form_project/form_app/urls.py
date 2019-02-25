from django.urls import path
from . import views

app_name = 'form_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('forms/', views.forms, name='forms'),
]
