from django.db import models
from .marca import Marca
from .categoria import Categoria
class Modelo(models.Model):
    descricao = models.CharField(max_length=100)
    marca = models.ForeignKey(
        Marca , on_delete=models.PROTECT, related_name="modelo")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculo")

    
    
    def __str__(self):
        return f"{self.descricao} | {self.marca} | {self.categoria}"   