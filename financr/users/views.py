from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm
from contasbanco.models import Contas_bancarias
from transacao.models import Categoria_transacao, Transacao
from django.contrib.auth.decorators import login_required
import json


# def dashboard(request):
#     if request.method == "GET":
#         usuario = request.user
#         contas = Contas_bancarias.objects.all().filter(user_id_id = usuario.id)
#         contas_json = []
#         for banco in contas.banco:
#             contas[banco.nome] = banco.saldo
        
#     return render(request, "users/dashboard.html", {'contas': (contas)})
#usar dumps



def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
            
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            login(request, user)
            
            
            conta_inicial = Contas_bancarias(None, user.id , "Carteira", 0)
            conta_inicial.save()
            
            categorias_despesa = ['Mercado', 'Restaurante', 'Lazer', 'Combustível', 'Cartão de Crédito',]
            categorias_receita = ['Salário', 'Vendas', 'Aluguel_terceiro', 'investimentos']
            
            for categoria in categorias_despesa:
                categoria_inicial = Categoria_transacaocategoria_inicial = Categoria_transacao(id=None, user_id_id=user.id, categoria=categoria, ativo=1, classe_transacao=1)
                categoria_inicial.save()
                
            for categoria in categorias_receita:
                categoria_inicial = Categoria_transacao(id=None, user_id_id=user.id, categoria=categoria, ativo=1, classe_transacao=2)
                categoria_inicial.save() 
               
            return redirect(reverse("dashboard"))
        else:
            return render(request, "users/error.html", {'form':form})


@login_required(login_url='/accounts/login/')
def dashboard(request):
    if request.method == "GET":
        usuario = request.user
        contas = Contas_bancarias.objects.all().filter(user_id_id = usuario.id)
        contagem_contas = Contas_bancarias.objects.all().filter(user_id_id = usuario.id).count()
        ultimas_transacoes = Transacao.objects.all().filter(user_id_id = usuario).order_by("-data_transacao")[:3]
        return render(request, "users/dashboard.html", {'contas':(contas),'ultimas_transacoes':(ultimas_transacoes),'contagem_contas':(contagem_contas)})

