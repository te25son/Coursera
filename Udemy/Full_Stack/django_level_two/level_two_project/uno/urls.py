from django.urls import path
from uno import views

urlpatterns = [
    path('', views.index, name='index'),
]
