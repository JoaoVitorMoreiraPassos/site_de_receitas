from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from receitas.views import home


urlpatterns = [
    path("", home)
]