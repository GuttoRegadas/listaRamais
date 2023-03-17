from django.db import models

# Create your models here.
class Ramais(models.Model):
    class Meta:
        verbose_name = "Lista de Ramais"
        verbose_name_plural = "Lista de Ramais"
    colaborador = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    ramal = models.CharField(max_length=100)
    area = models.CharField(max_length=30)
    sala = models.CharField(max_length=30)
    andarBloco = models.CharField(max_length=30)