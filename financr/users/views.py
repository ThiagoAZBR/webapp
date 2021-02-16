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


#imports para a função dashboard
from transacao.models import Transacao
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Count
from django.db.models import Avg, Max, Min
import json

def FunctionHomePage(request):
    if request.method == "GET":
        form = CreateUserForm()
        context = {'form':form}
        return render(request, 'templates/home_fora_do_webapp/home_page.html', context) 

    if request.method == 'POST':
        username = request.POST.get('username_login')
        password = request.POST.get('password_login')

        user = authenticate(request, password = password, username = username)

        if user is not None:
            login(request, user)
            return redirect(reverse('app_home'))   
        
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            form.save()
            
            login(request, user)
            
            conta_inicial = Contas_bancarias(None, user.id , "Carteira", 0)
            conta_inicial.save()
            
            categorias_despesa = ['Mercado', 'Restaurante', 'Lazer', 'Combustível', 'Cartão de Crédito', 'Curso', 'Academia',]
            categorias_receita = ['Salário', 'Vendas', 'Aluguel Terceiro', 'Investimentos',]
            categoria_transferência = ["Transferência", "Portabilidade"]
            
            for categoria in categorias_receita:
                categoria_inicial = Categoria_transacao(id=None, user_id_id=user.id, categoria=categoria, ativo=1, classe_transacao=1)
                categoria_inicial.save() 
                
            for categoria in categorias_despesa:
                categoria_inicial = Categoria_transacao(id=None, user_id_id=user.id, categoria=categoria, ativo=1, classe_transacao=2)
                categoria_inicial.save()
                
            #Categoria Transferência    
            categoria_inicial = Categoria_transacao(id=None, user_id_id=user.id, categoria=categoria_transferência, ativo=1, classe_transacao=3)
            categoria_inicial.save()
            
            return redirect(reverse("app_home"))

        
        else:
            return render(request, "templates/home_fora_do_webapp/home_page.html", {'form':form})

    
@login_required(login_url='home')
def dashboard(request):
    if request.method == "GET":
        usuario = request.user
        contas = Contas_bancarias.objects.all().filter(user_id_id = usuario.id)
        
        #filtro contas
        contagem_contas = Contas_bancarias.objects.all().filter(user_id_id = usuario.id).count()

        #filtro ultimas receitas
        ultimas_receitas = Transacao.objects.all().filter(user_id_id = usuario.id, classe_transacao = 1).order_by("data_transacao")[:3]

        #filtro ultimas despesas
        ultimas_despesas = Transacao.objects.all().filter(user_id_id = usuario.id, classe_transacao = 2).order_by("data_transacao")[:3]

        #categorias para mostrar na hora de criar categoria de receita
        categorias_receitas = Categoria_transacao.objects.filter(user_id_id = usuario.id, classe_transacao = 1)

        #categorias para mostrar na hora de criar categoria de despesa
        categorias_despesas = Categoria_transacao.objects.filter(user_id_id = usuario.id, classe_transacao = 2)

        #dados grafico saldos nos bancos
        filtrograficocontas = Contas_bancarias.objects.all().filter(user_id_id = usuario.id)
        graficobancos = [['Banco', 'Saldo'],]
        for conta in filtrograficocontas:
            nome = conta.nome_banco
            saldo = float(conta.saldo)
            dadosgraficobancos = [nome,saldo]
            graficobancos.append(dadosgraficobancos)
            print(json.dumps(graficobancos))

        #dados para gráfico de despesas
        filtrograficodespesas = Transacao.objects.all().filter(user_id_id = usuario, classe_transacao = 2).order_by("data_transacao")[:3] 
        graficodespesas = [['Data' , 'Valor']]
        for contadespesas in filtrograficodespesas:
            data = str(contadespesas.data_transacao)
            valor = float(contadespesas.valor)
            x = [data,valor]
            graficodespesas.append(x)
            print('até aqui foi')
            print(graficodespesas)


        #dados para grafico de receitas
        filtrograficoreceitas = Transacao.objects.all().filter(user_id_id = usuario, classe_transacao = 1).order_by("data_transacao")[:3] 
        graficoreceitas = [['Data' , 'Valor']]
        for contareceitas in filtrograficoreceitas:
            data = str(contareceitas.data_transacao)
            valor = float(contareceitas.valor)
            x = [data,valor]
            graficoreceitas.append(x)
            print('até aqui foi')
            print(graficoreceitas)

        #historico de receitas, despesas, transferencias
        lista_transacoes = Transacao.objects.filter(user_id_id = usuario.id)
        lista_transacoes_receitas = []
        lista_transacoes_despesas = []
        lista_transacoes_transferencias = []
        for i in lista_transacoes:
            if i.classe_transacao == 1:
                lista_transacoes_receitas.append(i)
            elif i.classe_transacao == 2:
                lista_transacoes_despesas.append(i)
            elif i.classe_transacao == 3:
                lista_transacoes_transferencias.append(i)
        print('lista_transacoes_receitas')                
        print(lista_transacoes_receitas)
        print('lista_transacoes_despesas')
        print(lista_transacoes_despesas)
        print('lista_transacoes_transferencias')
        print(lista_transacoes_transferencias)

        return render(request, "templates/tela_inicial_do_webapp/principia.html",
            {'contas':(contas),
            'ultimas_receitas':(ultimas_receitas),
            'ultimas_despesas':(ultimas_despesas),
            'categorias_receitas':(categorias_receitas),
            'categorias_despesas':(categorias_despesas),
            'contagem_contas':(contagem_contas),
            'lista_transacoes_receitas':(lista_transacoes_receitas),
            'lista_transacoes_despesas':(lista_transacoes_despesas),
            'lista_transacoes_transferencias':(lista_transacoes_transferencias),
            'graficobancos':(json.dumps(graficobancos)),
            'graficodespesas':(json.dumps(graficodespesas)),
            'graficoreceitas':(json.dumps(graficoreceitas))})