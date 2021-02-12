from django.shortcuts import render
from .forms import Criar_ContaBanco_Form
from .models import Contas_bancarias
from django.contrib.auth.decorators import login_required


@login_required(login_url='home')
def criar_conta(request):
    if request.method == "GET":
        form = Criar_ContaBanco_Form()
        return render(request, 'templates/tela_de_criar_conta/premissa.html', {'form': form})
    
    elif request.method == "POST":
        usuario = request.user
        classe_criar_conta=(Contas_bancarias(user_id=usuario))
        form = Criar_ContaBanco_Form(request.POST, instance=classe_criar_conta)
        
        if form.is_valid():
            filtro_bancos = Contas_bancarias.objects.filter(user_id=usuario.id)
            nome_banco_novo = form['nome_banco'].data
            
            try:
                form.save()
                return render(request, './templates/tela_inicial_do_webapp/principia.html', {'form': form})
            
            except:
                form.add_error('nome_banco','Este Banco já existe.')
                return render(request, 'templates/tela_de_criar_conta/premissa.html', {'form': form})
            
        else:    
            return render(request, 'templates/tela_de_criar_conta/premissa.html', {'form': form})
    
    else:
        return render(request, 'fracasso.html')


@login_required(login_url='home')
def contas_banco(request):
    if request.method == "GET":
        usuario = request.user 
        contas_banco_usuario = Contas_bancarias.objects.all().filter(user_id_id = usuario.id)
        return render(request, 'contas.html', {'lista_contas_banco': contas_banco_usuario})
    

def sucesso(request):
    return render(request, "sucesso.html")


def TelaEditarConta(request):
    return render(request, 'templates/tela_de_criar_conta/modify.html')


def TelaExcluirConta(request):
    return render(request, 'templates/tela_de_criar_conta/excluir.html')