from django.db import models
from django.contrib.auth.models import User


class Contas_bancarias(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_banco = models.CharField(max_length=20, null=False, blank=False)
    saldo = models.DecimalField(max_digits=20, decimal_places=2, null=False, default=0)
    

    def __str__(self):
        return self.nome_banco
    
    
