from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "receitas/pages/home.html")

def receitas(request, id):
    return render(request, "receitas/pages/receitas-view.html")