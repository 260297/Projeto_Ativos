from django.db import models

class User(models.Model):
    username = models.TextField(unique=True)
    password = models.TextField()
    acesso = models.TextField()

class Ativos(models.Model):
    imob = models.IntegerField()
    local = models.TextField()
    setor = models.TextField()
    responsavel = models.TextField()
    tipo = models.TextField()
    modelo = models.TextField()
    win = models.TextField()
    chave_win = models.TextField(blank=True, null=True)
    mac = models.TextField()
    mac_wifi = models.TextField()
    office = models.TextField()
    chave_office = models.TextField(blank=True, null=True)
    obs = models.TextField(blank=True, null=True)

class Manutencoes(models.Model):
    imob = models.CharField(max_length=30)  
    ativo = models.ForeignKey(Ativos, on_delete=models.CASCADE)
    data_manutencao = models.TextField()
    descricao = models.TextField(blank=True, null=True)
    tecnico_responsavel = models.TextField()
