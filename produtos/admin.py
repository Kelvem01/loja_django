from django.contrib import admin

from produtos.models import Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

    list_display = ['nome', 'criado_em', 'modificado_em']
    search_fields = ['nome', 'descricao']


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):

    list_display = ['nome', 'categoria', 'criado_em', 'modificado_em']
    search_fields = ['nome', 'descricao']

