from django.views.generic.edit import CreateView
from .models import Faleconosco
from django.urls import reverse_lazy
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserAuthenticationForm

#imports para a função dashboard
from contasbanco.models import Contas_bancarias
from transacao.models import Categoria_transacao
from transacao.models import Transacao
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Count
from django.db.models import Avg, Max, Min
import json

@login_required(login_url='home')
def app_home(request):
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
            print(graficodespesas)


        #dados para grafico de receitas
        filtrograficoreceitas = Transacao.objects.all().filter(user_id_id = usuario, classe_transacao = 1).order_by("data_transacao")[:3] 
        graficoreceitas = [['Data' , 'Valor']]
        for contareceitas in filtrograficoreceitas:
            data = str(contareceitas.data_transacao)
            valor = float(contareceitas.valor)
            x = [data,valor]
            graficoreceitas.append(x)
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

        
    # if request.method == "GET":
    #     return render(request, './templates/tela_inicial_do_webapp/principia.html')
    

def home_page(request):
    if request.method == "GET":
        form = CustomUserAuthenticationForm()
        return render(request, './templates/home_fora_do_webapp/home_page.html')
    
    elif request.method == "POST":
        form = CustomUserAuthenticationForm(request.POST)
        user = form
        
        if form.is_valid():
            login(request, user)
        return render(request, './templates/home_fora_do_webapp/home_page.html')

def fale_conosco(request):

    if request.method == "POST":
        nome_completo = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        
        a =Faleconosco(None, nome_completo, email, mensagem)
        a.save()
        
        return redirect(reverse("home"))

    return render(request, 'templates/home_fora_do_webapp/home_page.html')
