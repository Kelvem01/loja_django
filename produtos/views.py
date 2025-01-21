from django.shortcuts import render, redirect

from produtos.models import Categoria
from produtos.forms import CategoriaForm


def categoria_lista(request):
    categorias = Categoria.objects.all()
    contexto = {
        'categoria_lista': categorias,
    }
    return render(request, 'categoria_list.html', contexto)


def criar_categoria(request):
    form = CategoriaForm(request.POST or None)
    contexto = {}
    if form.is_valid():
        form.save()
        return redirect('produtos:categoria_lista')
    contexto["form"] = form
    return render(request, "categoria_form.html", contexto)


def atualizar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    form = CategoriaForm(request.POST or None, instance=categoria)
    contexto = {}
    if form.is_valid():
        form.save()
        return redirect('produtos:categoria_lista')
    contexto["form"] = form
    contexto["categoria"] = categoria
    return render(request, "categoria_form.html", contexto)
