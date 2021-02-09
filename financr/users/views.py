from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm
from contasbanco.models import Contas_bancarias
from transacao.models import Categoria_transacao
 
 