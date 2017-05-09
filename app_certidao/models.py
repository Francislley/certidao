from __future__ import unicode_literals
from django.db import models

class Pessoa(models.Model):
    pessoa_cpf = models.CharField('CPF do Proprietario', max_length=14)
    pessoa_nome = models.CharField('Nome do Proprietario', max_length=150)
    
class Veiculo(models.Model):
    veiculo_is_regular = models.BooleanField()
    veiculo_placa = models.CharField('Placa do Veiculo', max_length=8)
    tributo_is_pago = models.BooleanField()
    pessoas = models.ForeignKey(Pessoa)
    
class Certidao(models.Model):
    numero_certidao = models.IntegerField()
    status_certidao = models.BooleanField()
    
    def __str__(self):
         return '{} - {}'. format(self.id, self.numero_certidao, self.status_certidao)
