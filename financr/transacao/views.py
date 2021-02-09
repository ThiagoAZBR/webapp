from django.shortcuts import render
from .forms import Criar_transacao_Form, Criar_transferencia_Form, Criar_categoria_Form
from contasbanco.models import Contas_bancarias
from transacao.models import Transacao, Categoria_transacao
from django.contrib.auth.models import User
from decimal import Decimal
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def receita(request):
    if request.method =="GET":
        usuario = request.user
        form = Criar_transacao_Form()
        form.fields["conta"].queryset = Contas_bancarias.objects.filter(user_id=usuario.id)
        form.fields["categoria_transacao"].queryset = Categoria_transacao.objects.filter(user_id=usuario.id).filter(classe_transacao=2)
        return render(request, "testando.html", {'form': form})
        
    elif request.method == "POST":
        usuario = request.user
        classe_transacao=(Transacao(classe_transacao=1, user_id=usuario))
        form = Criar_transacao_Form(request.POST, instance=classe_transacao)
        
        if form.is_valid():
            form.save()
            receita = Decimal(form['valor'].data)    
            id_banco = form['conta'].data
            usuario_id = request.user.id
            
            conta_bancaria = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco)
            novo_saldo = (conta_bancaria[0].saldo + receita)
            
            # transacao = Contas_bancarias(1, usuario_id, conta_bancaria[0].nome_banco, conta_bancaria[0].saldo + receita)
            transacao = Contas_bancarias(id= conta_bancaria[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria[0].nome_banco, saldo= novo_saldo)
            transacao.save()            
            
            return render(request, "users/dashboard.html")
        
        return render(request, "testando.html", {'form': form})


@login_required(login_url='/accounts/login/')
def despesa(request):
    if request.method =="GET":
        usuario = request.user
        form = Criar_transacao_Form()
        form.fields["conta"].queryset = Contas_bancarias.objects.filter(user_id=usuario.id)
        form.fields["categoria_transacao"].queryset = Categoria_transacao.objects.filter(user_id=usuario.id).filter(classe_transacao=1)
        return render(request, "testando.html", {'form': form})
        
    elif request.method == "POST":
        usuario = request.user
        classe_transacao=(Transacao(classe_transacao=2, user_id=usuario))
        form = Criar_transacao_Form(request.POST, instance=classe_transacao)
        
        if form.is_valid():
            form.save(commit=False)
            
            despesa = Decimal(form['valor'].data)    
            id_banco = form['conta'].data
            usuario_id = request.user.id
            conta_bancaria = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco)
            novo_saldo = (conta_bancaria[0].saldo - despesa)
            
            if novo_saldo < 0:
                form.add_error('valor','O valor da despesa é maior que o saldo disponível em conta.')
                return render(request, "testando.html", {'form': form})
                       
            form.save()
            
            # transacao = Contas_bancarias(1, usuario_id, conta_bancaria[0].nome_banco, conta_bancaria[0].saldo + despesa)
            transacao = Contas_bancarias(id= conta_bancaria[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria[0].nome_banco, saldo= novo_saldo)
            transacao.save()            
            
            return render(request, "users/dashboard.html")
        
        return render(request, "testando.html", {'form': form})
    
    
@login_required(login_url='/accounts/login/')
def transferencia(request):
    if request.method =="GET":
        usuario = request.user
        classe_transacao=(Transacao(descricao="Transferência para conta própria"))
        form = Criar_transferencia_Form(instance=classe_transacao)
        form.fields["conta"].queryset = Contas_bancarias.objects.filter(user_id=usuario.id)
        form.fields["conta_destino"].queryset = Contas_bancarias.objects.filter(user_id=usuario.id)
        form.fields["categoria_transacao"].queryset = Categoria_transacao.objects.filter(user_id=usuario.id)
        
        return render(request, "testando.html", {'form': form})
        
    elif request.method == "POST":
        
        usuario = request.user
        classe_transacao=(Transacao(classe_transacao=3, user_id=usuario))
        form = Criar_transferencia_Form(request.POST, instance=classe_transacao)
        
        if form.is_valid():
            form.save(commit=False)
            
            transferencia = Decimal(form['valor'].data)    
            id_banco_origem = form['conta'].data
            id_banco_destino = form['conta_destino'].data
            usuario_id = request.user.id
            conta_bancaria_origem = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco_origem)
            conta_bancaria_destino = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco_destino)
            novo_saldo_origem = (conta_bancaria_origem[0].saldo - transferencia)
            novo_saldo_destino = (conta_bancaria_destino[0].saldo + transferencia)
            
            if novo_saldo_origem < 0:
                form.add_error('valor','O valor da transferencia é maior que o saldo disponível em conta.')
            
            if form['conta'].data == form['conta_destino'].data:
                form.add_error('conta_destino','O banco destino não pode ser igual ao banco de origem.')
                       
            if form.errors:
                return render(request, "testando.html", {'form': form})
            form.save()
            
            # transacao = Contas_bancarias(1, usuario_id, conta_bancaria_origem[0].nome_banco, conta_bancaria_origem[0].saldo + transferencia)
            transacao_saida = Contas_bancarias(id= conta_bancaria_origem[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria_origem[0].nome_banco, saldo= novo_saldo_origem)
            
            transacao_entrada = Contas_bancarias(id= conta_bancaria_destino[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria_destino[0].nome_banco, saldo= novo_saldo_destino)
            transacao_saida.save()
            transacao_entrada.save()            
            
            return render(request, "users/dashboard.html")
        
        return render(request, "testando.html", {'form': form})
    


@login_required(login_url='/accounts/login/')
def categoria(request):
    if request.method =="GET":
        usuario = request.user
        form = Criar_categoria_Form()
        return render(request, "testando.html", {'form': form})
        
    elif request.method == "POST":
        usuario = request.user
        classe_categoria=(Categoria_transacao(user_id=usuario))
        form = Criar_categoria_Form(request.POST, instance=classe_categoria)
        
        if form.is_valid():
            try:
                form.save()
                return render(request, "users/dashboard.html", {'form': form})
            
            except:
                form.add_error('categoria','Esta categoria já existe.')
                return render(request, "testando.html", {'form': form})
            
        else:
            return render(request, "fracasso.html", {'form': form})
        
        return render(request, "fracasso.html", {'form': form})


def sucesso(request):
    print("Deu boas!")
    return render(request, "sucesso.html")
    

#       ----     Views Do App Aquiiiii !!!!!!!!!!!!!!!!!!!!!!!!!!!!    ----


from django.views.generic import TemplateView
class TransactionScreenView(TemplateView):
    template_name = './templates/tela_de_transacoes/arkhe.html'

class TransactionScreen2View(TemplateView):
    template_name = './templates/tela_de_transacoes/despesa.html'

class TransactionScreen3View(TemplateView):
    template_name = './templates/tela_de_transacoes/transferir.html'