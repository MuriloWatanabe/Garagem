from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome.upper()


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Cor(models.Model):
    descricao = models.CharField(max_length=100)
    
    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name_plural = 'Cores'

class Modelo(models.Model):
    descricao = models.Charfield(max_length=100)
    marca = models.ForeignKey(
        Marca , on_delete=models.PROTECT, related_name="modelo")
    
    def __str__(self):
        return f"{self.descricao} | {self.marca}"         

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculo")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculo")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculo")
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=100, decimal_places=2, null=True, default=0)
    modelo = models.CharField(max_length=50)

    def __str__(self):
        return f"Modelo:{self.modelo} - Cor:{self.cor} - Ano:{self.ano} -  Marca:{self.marca}"