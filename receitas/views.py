from django.shortcuts import render
from django.http import HttpResponse
from utils.receitas.factory import make_recipe

# Create your views here.


def home(request):
    return render(request, "receitas/pages/home.html", context={
            "receitas": [make_recipe() for _ in range(10)]
        }
    )


def receitas(request, id):
    return render(request, "receitas/pages/receitas-view.html", context={
            "receita": make_recipe(),
            "is_detail_page": True
        }
    )
