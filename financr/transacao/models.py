from django.db import models
from django.contrib.auth.models import User
from contasbanco.models import Contas_bancarias

class Categoria_transacao(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=20, blank=False, null=False, unique=True)
    ativo = models.BooleanField(max_length=1, default=1)
    
    
class Transacao(models.Model):
    CLASSE_TRANSACAO_CHOICES =  (
        ("1", "Receita"),
        ("2", "Despesa"),
        ("3", "Transferencia"),
    )
    
    TIPO_TRANSACAO_CHOICES = (
        ("1", "Pontual"),
        ("2", "Fixa"),
        ("3", "Parcelada"),
    )
    
    REGULARIDADE_CHOICES = (
        ("1", "Diário"),
        ("2", "Semanal"),
        ("3", "Mensal"),
    )
    
    CONTAS_CHOICES = Contas_bancarias.objects.all()
    CATEGORIA_TRANSACAO_CHOICES = Categoria_transacao.objects.all()

    
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    classe_transacao = models.CharField(max_length=1, choices=CLASSE_TRANSACAO_CHOICES, blank=False, null=False)
    descricao = models.CharField(max_length=50, blank=False, null=False)
    valor = models.DecimalField(max_digits=20, decimal_places=2,  blank=False, null=False)
    data_transacao = models.DateField(blank=False, null=False)
    conta = models.OneToOneField(Contas_bancarias, choices=CONTAS_CHOICES, on_delete=models.RESTRICT, blank=False, null=False)
    categoria_transacao = models.OneToOneField(Categoria_transacao, choices=CATEGORIA_TRANSACAO_CHOICES, on_delete=models.RESTRICT, blank=False, null=False)
    tipo_transacao = models.CharField(max_length=1, choices=TIPO_TRANSACAO_CHOICES, default="Pontual", null=False, blank=False)
    regularidade = models.CharField(max_length=1, choices=REGULARIDADE_CHOICES, default="Mensal", null=False, blank=False)
    num_parcelas = models.IntegerField(blank=False, null=False, default=1)
    observacoes = models.CharField(max_length=500, blank=False, null=False)
    data_criacao = models.DateField(auto_now=True, blank=False, null=False)
    
    
class Transferencia(Transacao):
    CONTAS_CHOICES = Contas_bancarias.objects.all()

    
    conta_destino = models.OneToOneField(Contas_bancarias, choices=CONTAS_CHOICES, on_delete=models.RESTRICT, blank=False, null=False)
    descricao = "Transferência para conta própria"
