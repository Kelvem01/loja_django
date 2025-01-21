from django.db import models


class Categoria(models.Model):

    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descrição', blank=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    modificado_em = models.DateTimeField('Modificado em', auto_now=True)

    # CPF
    # localflavor
    # BRCPFField
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria de Produto'
        verbose_name_plural = 'Categorias de Produtos'
        ordering = ['nome']
        # db_table = 'categorias'


class Produto(models.Model):

    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descrição', blank=True)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, models.SET_NULL, null=True, blank=True, verbose_name='Categoria')
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    modificado_em = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']
