from django import forms

from produtos.models import Categoria


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = [
            'nome',
            'descricao',
        ]

