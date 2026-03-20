from django.contrib import admin

from .models import *

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('placa', 'modelo')
    search_fields = ('placa', 'modelo')

class ContatoInline(admin.TabularInline):
    model = Contato
    extra = 0

class ClienteCarroInline(admin.TabularInline):
    model = ClienteCarro
    extra = 0

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'saldo')
    search_fields = ('nome',)
    inlines = [ContatoInline, ClienteCarroInline]

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor')
    search_fields = ('descricao',)

@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo')
    search_fields = ('numero',)

@admin.register(Estacionamento)
class EstacionamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente_carro', 'vaga', 'entrada', 'saida')
    list_filter = ('cliente_carro', 'vaga')
    ordering = ('-entrada',)
    date_hierarchy = 'entrada'