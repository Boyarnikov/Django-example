from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.example, name="vote"),
    path('2', views.example2, name="vote2")
]
