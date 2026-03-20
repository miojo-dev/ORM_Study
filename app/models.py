from django.db import models


class Carro(models.Model):
    placa = models.CharField(unique=True, max_length=7)
    modelo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carro'

    def __str__(self):
        return self.placa


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cliente'

    def __str__(self):
        return self.nome


class ClienteCarro(models.Model):
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    carro = models.ForeignKey(Carro, models.DO_NOTHING)
    ativo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cliente_carro'
        unique_together = (('cliente', 'carro'),)

    def __str__(self):
        return f"{self.carro} ({self.cliente})"


class Contato(models.Model):
    contatos = (
        ('CELULAR', 'CELULAR'),
        ('EMAIL', 'EMAIL'),
        ('WHATSAPP', 'WHATSAPP'),
    )
    tipo_contato = models.CharField(max_length=10, choices=contatos, default='Celular')
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    informacao = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'contato'
        unique_together = (('tipo_contato', 'cliente'),)

    def __str__(self):
        return self.informacao


class Tipo(models.Model):
    descricao = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo'

    def __str__(self):
        return self.descricao


class Vaga(models.Model):
    numero = models.CharField(max_length=3)
    tipo = models.ForeignKey(Tipo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vaga'

    def __str__(self):
        return self.numero


class Estacionamento(models.Model):
    cliente_carro = models.ForeignKey(ClienteCarro, models.DO_NOTHING)
    vaga = models.ForeignKey(Vaga, models.DO_NOTHING)
    entrada = models.DateTimeField()
    saida = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'estacionamento'
        unique_together = (('cliente_carro', 'vaga', 'entrada'),)