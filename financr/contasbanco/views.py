from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import Criar_ContaBanco_Form
from .models import Contas_bancarias
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


@login_required(login_url='home')
def criar_conta(request):
    #Cria o o form de criar conta bancária e renderiza na página. Envia também a lista de bancos
    # que a pessoa já tem cadastrado. (Não implementado esta lista)
    if request.method == "GET":
        form = Criar_ContaBanco_Form()
        
        usuario = request.user
        lista_bancos = Contas_bancarias.objects.filter(user_id=usuario.id)
        
        return render(request, 'templates/tela_de_criar_conta/premissa.html', {'form': form, 'lista_bancos': lista_bancos})
    
    elif request.method == "POST":
        usuario = request.user
        classe_criar_conta=(Contas_bancarias(user_id=usuario))
        form = Criar_ContaBanco_Form(request.POST, instance=classe_criar_conta)
        
        if form.is_valid():
            filtro_bancos = Contas_bancarias.objects.filter(user_id=usuario.id)
            nome_banco_novo = form['nome_banco'].data
            
            try:
                form.save()
                return redirect(reverser('app_home'))
            
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


#Função que permite buscar a conta bancária selecionada quando o usuário clica em uma das contas cadastradas
# apresentadas na tela de criação de conta bancária.
# def editar_conta(request, pk):
#     if request.method == "GET":
        # contas_bancarias = get_object_or_404(Contas_bancarias, pk=pk) #Caso usuário busque por um ID manualmente e inserir um id que não exista, retornará erro 404 - Página não encontrada.
        
#         #Valida se o usuário logado e o usuário da conta pesquisada
#         id_usuario_logado = request.user.id
#         conta_usuario = Contas_bancarias.objects.filter(id=pk)
#         id_usuario_conta = conta_usuario[0].user_id_id
        
#         if id_usuario_conta != id_usuario_logado:
#             raise PermissionDenied

#     return redirect(reverse('home'))


def TelacategoriaConta(request):
    return render(request, 'templates/tela_de_criar_conta/categoria.html')