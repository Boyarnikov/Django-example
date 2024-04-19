from django.contrib import admin
from django.urls import path

from . import views

app_name = "vote"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:_id>/', views.question, name="question"),
    path('<int:_id>/result', views.result, name="result"),
    path('<int:_id>/vote', views.vote, name="vote")
]
