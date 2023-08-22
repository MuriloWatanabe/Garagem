from django.db import models
from .marca import Marca
from .modelo import Modelo
from .categoria import Categoria
from .acessorio import Acessorio
from .cor import Cor

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculo")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculo")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculo")
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=100, decimal_places=2, null=True, default=0)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculo")
    acessorio = models.ManyToManyField(Acessorio, related_name="Acessórios")

    def __str__(self):
        return f"Modelo:{self.modelo} - Cor:{self.cor} - Ano:{self.ano} -  Marca:{self.marca} {self.id}"