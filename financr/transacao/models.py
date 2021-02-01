from django.db import models
from django.contrib.auth.models import User
from contasbanco.models import Contas_bancarias
from django.core.validators import MinValueValidator
from decimal import Decimal



class Categoria_transacao(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=20, blank=False, null=False, unique=True)
    ativo = models.BooleanField(max_length=1, default=1)

    def __str__(self):
        return self.categoria


class Transacao(models.Model):
    CLASSE_TRANSACAO_CHOICES = (
    (1, "Receita"),
    (2, "Despesa"),
    (3, "Transferencia"),
    )

    TIPO_TRANSACAO_CHOICES = (
    (1, "Pontual"),
    (2, "Fixa"),
    (3, "Parcelada"),
    )

    REGULARIDADE_CHOICES = (
    (1, "Diário"),
    (2, "Semanal"),
    (3, "Mensal"),
    )


    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    classe_transacao = models.IntegerField(choices=CLASSE_TRANSACAO_CHOICES, blank=False, null=False)
    descricao = models.CharField(max_length=50, blank=False, null=False)
    valor = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))], blank=False, null=False)
    data_transacao = models.DateField(blank=False, null=False)
    conta = models.ForeignKey(Contas_bancarias, on_delete=models.RESTRICT, blank=False, null=False)
    categoria_transacao = models.ForeignKey(Categoria_transacao, on_delete=models.RESTRICT, blank=False, null=False)
    tipo_transacao = models.IntegerField(choices=TIPO_TRANSACAO_CHOICES, default="Pontual", null=False, blank=False)
    regularidade = models.IntegerField(choices=REGULARIDADE_CHOICES, default="Mensal", null=False, blank=False)
    num_parcelas = models.IntegerField(blank=False, null=False, default=1)
    observacoes = models.CharField(max_length=500, blank=False, null=False)
    data_criacao = models.DateField(auto_now=True, blank=False, null=False)


class Transferencia(Transacao):
    conta_destino = models.OneToOneField(Contas_bancarias, on_delete=models.RESTRICT, blank=False, null=False)
    descricao = "Transferência para conta própria"