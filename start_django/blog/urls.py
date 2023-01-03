# there is no Admin in here
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]