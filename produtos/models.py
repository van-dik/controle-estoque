from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=100, unique=True)
    quantidade = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['criado_em']

    def __str__(self):
        return f'{self.codigo} - {self.nome}'
