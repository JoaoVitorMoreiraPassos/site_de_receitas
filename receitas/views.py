from django.shortcuts import render
from utils.receitas.factory import make_recipe
from .models import Receita
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404
# Create your views here.

app_name = "receitas"


def home(request):
    receitas = Receita.objects.filter(
        is_posted=True
    ).order_by("-id")
    print("receitas: ", receitas)
    return render(request, "receitas/pages/home.html", context={
        "receitas": receitas
    }
    )


def category(request, category_id):
    receitas = get_list_or_404(Receita.objects.filter(
        id=id,
        is_posted=True
    ).order_by("-id"))

    category = receitas[0].category.name
    return render(request, "receitas/pages/category.html", context={
        "receitas": receitas,
        "title": category
    }
    )


def receitas(request, id):
    receita = Receita.objects.filter(
        id=id,
        is_posted=True
    ).order_by("-id").first()
    
    return render(request, "receitas/pages/receitas-view.html", context={
        "receita": receita,
        "is_detail_page": True
    }
    )
