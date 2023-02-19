from django.shortcuts import render
from utils.receitas.factory import make_recipe
from .models import Receita
# Create your views here.

app_name = "receitas"


def home(request):
    receitas = Receita.objects.all().order_by("-id")
    print("receitas: ", receitas)
    return render(request, "receitas/pages/home.html", context={
        "receitas": receitas
    }
    )


def category(request, category_id):
    receitas = Receita.objects.filter(
        category__id=category_id
    ).order_by("-id")
    print("receitas: ", receitas)
    return render(request, "receitas/pages/home.html", context={
        "receitas": receitas
    }
    )


def receitas(request, id):
    return render(request, "receitas/pages/receitas-view.html", context={
        "receita": make_recipe(),
        "is_detail_page": True
    }
    )
