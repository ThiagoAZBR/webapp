from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from contasbanco.models import Contas_bancarias
from transacao.models import Categoria_transacao
from django.http import HttpResponse
from .forms import CreateUserForm
from django.forms import ModelForm
from faleconosco.models import Faleconosco
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView, TemplateView


from django.views.generic.edit import CreateView
from users.forms import CreateUserForm


def LoginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username_login')
        password = request.POST.get('password_login')

        user = authenticate(request, password = password, username = username)

        if user is not None:
            login(request, user)
            return redirect('app_home')
        
    context = {}
    return render(request, 'templates/home_fora_do_webapp/home_page.html', context)
    

def FunctionHomePage(request):

    if request.method == 'POST':
        username = request.POST.get('username_login')
        password = request.POST.get('password_login')

        user = authenticate(request, password = password, username = username)

        if user is not None:
            login(request, user)
            return redirect('app_home')
            
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            
        #     conta_inicial = Contas_bancarias(None, user.id , "Carteira", 0)
        #     conta_inicial.save()
            
        #     categorias_despesa = ['Mercado', 'Restaurante', 'Lazer', 'Combustível', 'Cartão de Crédito',]
        #     categorias_receita = ['Salário', 'Vendas', 'Aluguel_terceiro', 'investimentos']
        #     categoria_transferência = "Transferência"
            
        #     for categoria in categorias_receita:
        #         categoria_inicial = Categoria_transacao(id=None, user_id_id=user.id, categoria=categoria, ativo=1, classe_transacao=1)
        #         categoria_inicial.save() 
                
        #     for categoria in categorias_despesa:
        #         categoria_inicial = Categoria_transacao(id=None, user_id_id=user.id, categoria=categoria, ativo=1, classe_transacao=2)
        #         categoria_inicial.save()
                
        #     #Categoria Transferência    
        #     categoria_inicial = Categoria_transacao(id=None, user_id_id=user.id, categoria=categoria_transferência, ativo=1, classe_transacao=3)
        #     categoria_inicial.save()
               
        #     return redirect(reverse("dashboard"))
        # else:
        #     return render(request, "users/error.html", {'form':form})
        #     pass

    context = {'form':form}
    return render(request, 'templates/home_fora_do_webapp/home_page.html', context) 
