from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import *

@admin.register(Carro)
class CarroAdmin(ModelAdmin):
    list_display = ('placa', 'modelo')
    search_fields = ('placa', 'modelo')

class ContatoInline(TabularInline):
    model = Contato
    extra = 0
    tab = True

class ClienteCarroInline(TabularInline):
    model = ClienteCarro
    extra = 0
    tab = True

@admin.register(Cliente)
class ClienteAdmin(ModelAdmin):
    list_display = ('nome', 'saldo')
    search_fields = ('nome',)
    inlines = [ContatoInline, ClienteCarroInline]

@admin.register(Tipo)
class TipoAdmin(ModelAdmin):
    list_display = ('descricao', 'valor')
    search_fields = ('descricao',)

@admin.register(Vaga)
class VagaAdmin(ModelAdmin):
    list_display = ('numero', 'tipo')
    search_fields = ('numero',)

@admin.register(Estacionamento)
class EstacionamentoAdmin(ModelAdmin):
    list_display = ('cliente_carro', 'vaga', 'entrada', 'saida')
    list_filter = ('cliente_carro', 'vaga')
    ordering = ('-entrada',)
    date_hierarchy = 'entrada'