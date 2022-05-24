from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=60)
    sobrenome = models.CharField(max_length=60)
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return self.nome




