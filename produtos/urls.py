from django.urls import path

from produtos.views import categoria_lista, criar_categoria, atualizar_categoria


app_name = 'produtos'


urlpatterns = [
    path('categorias/', categoria_lista, name='categoria_lista'),
    path('categorias/nova/', criar_categoria, name='criar_categoria'),
    path('categorias/<int:id>/', atualizar_categoria, name='atualizar_categoria'),
]
