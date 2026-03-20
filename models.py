# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Carro(models.Model):
    placa = models.CharField(unique=True, max_length=7)
    modelo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carro'


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cliente'


class ClienteCarro(models.Model):
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    carro = models.ForeignKey(Carro, models.DO_NOTHING)
    ativo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cliente_carro'
        unique_together = (('cliente', 'carro'),)


class Contato(models.Model):
    tipo_contato = models.TextField()  # This field type is a guess.
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    informacao = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'contato'
        unique_together = (('tipo_contato', 'cliente'),)


class Estacionamento(models.Model):
    cliente_carro = models.ForeignKey(ClienteCarro, models.DO_NOTHING)
    vaga = models.ForeignKey('Vaga', models.DO_NOTHING)
    entrada = models.DateTimeField()
    saida = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'estacionamento'
        unique_together = (('cliente_carro', 'vaga', 'entrada'),)


class Tipo(models.Model):
    descricao = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo'


class Vaga(models.Model):
    numero = models.CharField(max_length=3)
    tipo = models.ForeignKey(Tipo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vaga'
