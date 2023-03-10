from django.db import models

class Marca(models.Model):
 Nome =models.CharField(max_length=50)
 Nacionalidade = models.CharField(max_length=50)

 def _str_(self):
  return self.Nome,self.Nacionalidade   
