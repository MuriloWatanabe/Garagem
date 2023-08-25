from django.db import models
from .modelo import Modelo
from .categoria import Categoria
from .acessorio import Acessorio
from .cor import Cor
from uploader.models import Image


class Veiculo(models.Model):
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculo")
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=100, decimal_places=2, null=True, default=0)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculo")
    acessorio = models.ManyToManyField(Acessorio, related_name="Acessórios")
    imagem = models.ManyToManyField(Image, related_name="Imagem")
    def __str__(self):
        return f"Modelo:{self.modelo} - Cor:{self.cor} - Ano:{self.ano} -  {self.id}"