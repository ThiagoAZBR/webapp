from django.shortcuts import render, redirect, reverse
from .forms import Criar_transacao_Form, Criar_transferencia_Form, Criar_categoria_Form
from contasbanco.models import Contas_bancarias
from transacao.models import Transacao, Categoria_transacao, Transferencia
from django.contrib.auth.models import User
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from datetime import *
from django.utils import formats
from django.db.models import Q



@login_required(login_url='home')
def receita(request):
    if request.method =="GET":
        usuario = request.user
        form = Criar_transacao_Form()
        form.fields["conta"].queryset = Contas_bancarias.objects.filter(user_id=usuario.id)
        form.fields["categoria_transacao"].queryset = Categoria_transacao.objects.filter(user_id=usuario.id).filter(classe_transacao=1)
        return render(request, 'templates/tela_de_transacoes/arkhe.html', {'form': form})
        
    elif request.method == "POST":
        usuario = request.user
        classe_transacao=(Transacao(classe_transacao=1, user_id=usuario, transacao_efetivada=False, transacao_fixa=False))
        form = Criar_transacao_Form(request.POST, instance=classe_transacao)
        
        if form.is_valid():
            instance = form.save(commit=False)
            
            #INFORMAÇÕES PARA FILTRAR DADOS NO BANCO DE DADOS
            tipo_transacao = int(form['tipo_transacao'].data)
            receita = Decimal(form['valor'].data)    
            id_banco = int(form['conta'].data)
            usuario_id = int(request.user.id)
            
            #INFORMAÇÕES DE DATA DE TRANSAÇÃO E REGULARIDADE
            try:
                regularidade = int(form['regularidade'].data)
            
            except:
                regularidade = 0
                instance.regularidade = 0
                
            data_atual = datetime.today()
            data_atual_formatada = data_atual.strftime("%Y-%m-%d")
            data_transacao_str = form['data_transacao'].data
            data_transacao_data =datetime(int(data_transacao_str[6:10]), int(data_transacao_str[3:5]),int(data_transacao_str[:2])) #ANO MES DIA

            if tipo_transacao == 1: #TRANSAÇÃO PONTUAL
                
                if  data_atual >= data_transacao_data: #Verifica se é uma transação atual ou futura
                    instance.transacao_efetivada = True 
                    
                    instance.save()
                    
                    conta_bancaria = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco)
                    novo_saldo = (conta_bancaria[0].saldo + receita)
                    
                    transacao = Contas_bancarias(id= conta_bancaria[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria[0].nome_banco, saldo= novo_saldo)
                    transacao.save()
                            
                else: #Caso seja uma transação futura o saldo não é atualizado (função de rotina verificará e atualizará o saldo em períodos de tempo fixo APScheduler)
                    instance.transacao_efetivada = False
                    instance.save()
            
            elif tipo_transacao == 2: #TRANSAÇÃO FIXA
                
                if regularidade == 1: #TRANSAÇÃO FIXA DIÁRIA
                    intervalo_transacao = timedelta(days=1)

                elif regularidade == 2: #TRANSAÇÃO FIXA SEMANAL
                    intervalo_transacao = timedelta(weeks=1)
                
                elif regularidade == 3: #TRANSAÇÃO FIXA MENSAL
                    intervalo_transacao = timedelta(days=30)
                
                else:
                    form.add_error('regularidade','Selecione uma opção de "Regularidade" válida para transação "Fixa".')
                    return render(request, 'templates/tela_de_transacoes/arkhe.html', {'form': form})
                
                while data_atual > data_transacao_data:
                    instance.pk = None
                    instance.data_transacao = data_transacao_data
                    instance.transacao_fixa = False #As parcelas passadas não terão o marcador de Transação fixa,
                    #somente as transações futuras. Assim facilita o programa a encontrar as transacoes fixas e atualizar e recriar outra transação futura no tempo certo
                    instance.transacao_efetivada = True
                    instance.save()
                    
                    conta_bancaria = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco)
                    novo_saldo = (conta_bancaria[0].saldo + receita)
                    
                    transacao = Contas_bancarias(id= conta_bancaria[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria[0].nome_banco, saldo= novo_saldo)
                    transacao.save()
                    data_transacao_data += intervalo_transacao
                
                #Criando transação futura sem alterar saldo
                instance.pk = None
                instance.data_transacao = data_transacao_data
                instance.transacao_fixa = True
                instance.transacao_efetivada = False
                instance.save()
                
                return redirect(request, './templates/tela_inicial_do_webapp/principia.html')
                ###
                #Criar Função para gerar uma transacao futura para continuar a conta fixa
                #Criar uma função para verificar se a transacao anterior está pronta para ser efetivada e
                #criar uma nova transacao para continuar o ciclo 
                ###
            
           
            elif tipo_transacao == 3:  #TRANSAÇÃO PARCELADA
                valor_transacao = Decimal(form['valor'].data)
                qtde_parcelas = int(form['num_parcelas'].data)
                valor_parcela = round(valor_transacao/qtde_parcelas, 2)
                dizima = False
                
                if regularidade == 1: #TRANSAÇÃO FIXA DIÁRIA
                    intervalo_transacao = timedelta(days=1)

                elif regularidade == 2: #TRANSAÇÃO FIXA SEMANAL
                    intervalo_transacao = timedelta(weeks=1)
                
                elif regularidade == 3: #TRANSAÇÃO FIXA MENSAL
                    intervalo_transacao = timedelta(days=30)
                
                else:
                    form.add_error('regularidade','Selecione uma opção de "Regularidade" válida para transação "Fixa".')
                    return render(request, 'templates/tela_de_transacoes/arkhe.html', {'form': form})
                
                if  valor_parcela * qtde_parcelas != valor_transacao:
                    dizima = True
                    valor_parcela_1 = valor_parcela
                    valor_parcela_1 += Decimal(0.01)
                    valor_parcela_1 = round(valor_parcela_1, 2)

                for parcela in range(qtde_parcelas):
                    if dizima:
                        if data_atual > data_transacao_data:
                            instance.pk = None
                            instance.data_transacao = data_transacao_data
                            instance.transacao_efetivada = True
                            instance.valor = valor_parcela_1
                            dizima = False
                            instance.save()
                            
                            conta_bancaria = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco)
                            novo_saldo = (conta_bancaria[0].saldo + valor_parcela_1)
                            
                            transacao = Contas_bancarias(id= conta_bancaria[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria[0].nome_banco, saldo= novo_saldo)
                            transacao.save()
                            
                        else:
                            instance.pk = None
                            instance.data_transacao = data_transacao_data
                            instance.transacao_efetivada = False
                            instance.valor = valor_parcela_1
                            dizima = False
                            instance.save()
                    
                    else:
                        if data_atual > data_transacao_data:    
                            instance.pk = None
                            instance.data_transacao = data_transacao_data
                            instance.transacao_efetivada = True
                            instance.valor = valor_parcela
                            dizima = False
                            instance.save()
                            
                            conta_bancaria = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco)
                            novo_saldo = (conta_bancaria[0].saldo + valor_parcela)
                            
                            transacao = Contas_bancarias(id= conta_bancaria[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria[0].nome_banco, saldo= novo_saldo)
                            transacao.save()
                        
                        else:
                            instance.pk = None
                            instance.data_transacao = data_transacao_data
                            instance.transacao_efetivada = False
                            instance.valor = valor_parcela
                            dizima = False
                            instance.save()
                    
                    data_transacao_data += intervalo_transacao

            return redirect(reverse('app_home'))
        
        return render(request, 'templates/tela_de_transacoes/arkhe.html', {'form': form})


@login_required(login_url='home')
def despesa(request):
    if request.method =="GET":
        usuario = request.user
        form = Criar_transacao_Form()
        form.fields["conta"].queryset = Contas_bancarias.objects.filter(user_id=usuario.id)
        form.fields["categoria_transacao"].queryset = Categoria_transacao.objects.filter(user_id=usuario.id).filter(classe_transacao=2)
        return render(request, 'templates/tela_de_transacoes/despesa.html', {'form': form})
        
    elif request.method == "POST":
        usuario = request.user
        classe_transacao=(Transacao(classe_transacao=2, user_id=usuario, transacao_efetivada=False, transacao_fixa=False))
        form = Criar_transacao_Form(request.POST, instance=classe_transacao)
        
        if form.is_valid():
            instance = form.save(commit=False)
            
            #INFORMAÇÕES PARA FILTRAR DADOS NO BANCO DE DADOS
            tipo_transacao = int(form['tipo_transacao'].data)
            despesa = Decimal(form['valor'].data)    
            id_banco = form['conta'].data
            usuario_id = request.user.id
            
            #INFORMAÇÕES DE DATA DE TRANSAÇÃO E REGULARIDADE
            try:
                regularidade = int(form['regularidade'].data)
            
            except:
                regularidade = 0
                instance.regularidade = 0
                
            data_atual = datetime.today()
            data_atual_formatada = data_atual.strftime("%Y-%m-%d")
            data_transacao_str = form['data_transacao'].data
            data_transacao_data =datetime(int(data_transacao_str[6:10]), int(data_transacao_str[3:5]),int(data_transacao_str[:2])) #ANO MES DIA
            
            # if novo_saldo < 0:
            #     form.add_error('valor','O valor da despesa é maior que o saldo disponível em conta.')
            #     return render(request, "testando.html", {'form': form})
            
            if tipo_transacao == 1: #TRANSAÇÃO PONTUAL
                if  data_atual >= data_transacao_data: #Verifica se é uma transação atual ou futura
                    instance.transacao_efetivada = True 
                    instance.save()
                    conta_bancaria = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco)
                    novo_saldo = (conta_bancaria[0].saldo - despesa)
                    
                    transacao = Contas_bancarias(id= conta_bancaria[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria[0].nome_banco, saldo= novo_saldo)
                    transacao.save()
                            
                else: #Caso seja uma transação futura o saldo não é atualizado (função de rotina verificará e atualizará o saldo em períodos de tempo fixo APScheduler)
                    instance.transacao_efetivada = False
                    instance.save()
                
            elif tipo_transacao == 2: #TRANSAÇÃO FIXA
                
                if regularidade == 1: #TRANSAÇÃO FIXA DIÁRIA
                    intervalo_transacao = timedelta(days=1)

                elif regularidade == 2: #TRANSAÇÃO FIXA SEMANAL
                    intervalo_transacao = timedelta(weeks=1)
                
                elif regularidade == 3: #TRANSAÇÃO FIXA MENSAL
                    intervalo_transacao = timedelta(days=30)
                
                else:
                    form.add_error('regularidade','Selecione uma opção de "Regularidade" válida para transação "Fixa".')
                    return render(request, 'templates/tela_de_transacoes/despesa.html', {'form': form})

                while data_atual > data_transacao_data:
                    instance.pk = None
                    instance.data_transacao = data_transacao_data
                    instance.transacao_fixa = False #As parcelas passadas não terão o marcador de Transação fixa,
                    #somente as transações futuras. Assim facilita o programa a encontrar as transacoes fixas e atualizar e recriar outra transação futura no tempo certo
                    instance.transacao_efetivada = True
                    instance.save()
                    
                    conta_bancaria = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco)
                    novo_saldo = (conta_bancaria[0].saldo - despesa)
                    
                    transacao = Contas_bancarias(id= conta_bancaria[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria[0].nome_banco, saldo= novo_saldo)
                    transacao.save()
                    data_transacao_data += intervalo_transacao
                
                #Criando transação futura sem alterar saldo
                instance.pk = None
                instance.data_transacao = data_transacao_data
                instance.transacao_fixa = True
                instance.transacao_efetivada = False
                instance.save()
                
                return render(request, './templates/tela_inicial_do_webapp/principia.html')
            
            elif tipo_transacao == 3: #TRANSAÇÃO PARCELADA
                valor_transacao = Decimal(form['valor'].data)
                qtde_parcelas = int(form['num_parcelas'].data)
                valor_parcela = round(valor_transacao/qtde_parcelas, 2)
                dizima = False
                
                if regularidade == 1: #TRANSAÇÃO FIXA DIÁRIA
                    intervalo_transacao = timedelta(days=1)

                elif regularidade == 2: #TRANSAÇÃO FIXA SEMANAL
                    intervalo_transacao = timedelta(weeks=1)
                
                elif regularidade == 3: #TRANSAÇÃO FIXA MENSAL
                    intervalo_transacao = timedelta(days=30)
                
                else:
                    form.add_error('regularidade','Selecione uma opção de "Regularidade" válida para transação "Fixa".')
                    return render(request, 'templates/tela_de_transacoes/despesa.html', {'form': form})
                
                if  valor_parcela * qtde_parcelas != valor_transacao:
                    dizima = True
                    valor_parcela_1 = valor_parcela
                    valor_parcela_1 += Decimal(0.01)
                    valor_parcela_1 = round(valor_parcela_1, 2)

                for parcela in range(qtde_parcelas):
                    if dizima:
                        if data_atual > data_transacao_data:
                            instance.pk = None
                            instance.data_transacao = data_transacao_data
                            instance.transacao_efetivada = True
                            instance.valor = valor_parcela_1
                            dizima = False
                            instance.save()
                            
                            conta_bancaria = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco)
                            novo_saldo = (conta_bancaria[0].saldo - valor_parcela_1)
                            
                            transacao = Contas_bancarias(id= conta_bancaria[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria[0].nome_banco, saldo= novo_saldo)
                            transacao.save()
                            
                        else:
                            instance.pk = None
                            instance.data_transacao = data_transacao_data
                            instance.transacao_efetivada = False
                            instance.valor = valor_parcela_1
                            dizima = False
                            instance.save()
                    
                    else:
                        if data_atual > data_transacao_data:    
                            instance.pk = None
                            instance.data_transacao = data_transacao_data
                            instance.transacao_efetivada = True
                            instance.valor = valor_parcela
                            dizima = False
                            instance.save()
                            
                            conta_bancaria = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco)
                            novo_saldo = (conta_bancaria[0].saldo - valor_parcela)
                            
                            transacao = Contas_bancarias(id= conta_bancaria[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria[0].nome_banco, saldo= novo_saldo)
                            transacao.save()
                        
                        else:
                            instance.pk = None
                            instance.data_transacao = data_transacao_data
                            instance.transacao_efetivada = False
                            instance.valor = valor_parcela
                            dizima = False
                            instance.save()
                    
                    data_transacao_data += intervalo_transacao

            return render(request, './templates/tela_inicial_do_webapp/principia.html')
        
        return render(request, 'templates/tela_de_transacoes/despesa.html', {'form': form})
    
    
@login_required(login_url='home')
def transferencia(request):
    if request.method =="GET":
        usuario = request.user
        classe_transacao=(Transferencia(descricao="Transferência para conta própria"))
        form = Criar_transferencia_Form(instance=classe_transacao)
        form.fields["conta"].queryset = Contas_bancarias.objects.filter(user_id=usuario.id)
        form.fields["conta_destino"].queryset = Contas_bancarias.objects.filter(user_id=usuario.id)
        form.fields["categoria_transacao"].queryset = Categoria_transacao.objects.filter(user_id=usuario.id, classe_transacao=3)
        
        return render(request, 'templates/tela_de_transacoes/transferir.html', {'form': form})
        
    elif request.method == "POST":
        usuario = request.user
        classe_transacao=(Transferencia(classe_transacao=3, user_id=usuario, transacao_efetivada=False, transacao_fixa=False))
        form = Criar_transferencia_Form(request.POST, instance=classe_transacao)
        
        if form.is_valid():
            instance = form.save(commit=False)
            
            #INFORMAÇÕES PARA FILTRAR DADOS NO BANCO DE DADOS
            tipo_transacao = int(form['tipo_transacao'].data)
            transferencia = Decimal(form['valor'].data)    
            id_banco_origem = form['conta'].data
            id_banco_destino = form['conta_destino'].data
            usuario_id = request.user.id

            #INFORMAÇÕES DE DATA DE TRANSAÇÃO E REGULARIDADE
            try:
                regularidade = int(form['regularidade'].data)
            
            except:
                regularidade = 0
                instance.regularidade = 0
            
            #INFORMAÇÕES PARA FILTRAR DADOS NO BANCO DE DADOS
            data_atual = datetime.today()
            data_atual_formatada = data_atual.strftime("%Y-%m-%d")
            data_transacao_str = form['data_transacao'].data
            data_transacao_data =datetime(int(data_transacao_str[6:10]), int(data_transacao_str[3:5]),int(data_transacao_str[:2])) #ANO MES DIA
            
            # if novo_saldo_origem < 0:
            #     form.add_error('valor','O valor da transferencia é maior que o saldo disponível em conta.')
            
            if form['conta'].data == form['conta_destino'].data:
                form.add_error('conta_destino','O banco destino não pode ser igual ao banco de origem.')
                       
            if form.errors:
                return render(request, 'templates/tela_de_transacoes/transferir.html', {'form': form})
            
            
            if tipo_transacao == 1: #TRANSAÇÃO PONTUAL
                if  data_atual >= data_transacao_data: #Verifica se é uma transação atual ou futura
                    instance.transacao_efetivada = True
                    instance.save()
                
                    conta_bancaria_origem = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco_origem)
                    
                    conta_bancaria_destino = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco_destino)
                    
                    novo_saldo_origem = (conta_bancaria_origem[0].saldo - transferencia)
                    
                    novo_saldo_destino = (conta_bancaria_destino[0].saldo + transferencia)
                    
                    transacao_saida = Contas_bancarias(id= conta_bancaria_origem[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria_origem[0].nome_banco, saldo= novo_saldo_origem)
            
                    transacao_entrada = Contas_bancarias(id= conta_bancaria_destino[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria_destino[0].nome_banco, saldo= novo_saldo_destino)
                    
                    transacao_saida.save()
                    transacao_entrada.save()
                    

                #Caso seja uma transação futura o saldo não é atualizado (função de rotina verificará e atualizará o saldo em períodos de tempo fixo APScheduler)
                else: 
                    instance.transacao_efetivada = False
                    instance.save()
            
            if tipo_transacao == 2: #TRANSAÇÃO FIXA
                
                if regularidade == 1: #TRANSAÇÃO FIXA DIÁRIA
                    intervalo_transacao = timedelta(days=1)

                elif regularidade == 2: #TRANSAÇÃO FIXA SEMANAL
                    intervalo_transacao = timedelta(weeks=1)
                
                elif regularidade == 3: #TRANSAÇÃO FIXA MENSAL
                    intervalo_transacao = timedelta(days=30)
                
                else:
                    form.add_error('regularidade','Selecione uma opção de "Regularidade" válida para transação "Fixa".')
                    return render(request, 'templates/tela_de_transacoes/transferir.html', {'form': form})
            
                while data_atual > data_transacao_data:
                    instance.pk = None
                    instance.data_transacao = data_transacao_data
                    instance.transacao_fixa = False #As parcelas passadas não terão o marcador de Transação fixa,
                    #somente as transações futuras. Assim facilita o programa a encontrar as transacoes fixas e atualizar e recriar outra transação futura no tempo certo
                    instance.transacao_efetivada = True
                    instance.save()
                    
                    conta_bancaria_origem = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco_origem)
                    
                    conta_bancaria_destino = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco_destino)
                    
                    novo_saldo_origem = (conta_bancaria_origem[0].saldo - transferencia)
                    
                    novo_saldo_destino = (conta_bancaria_destino[0].saldo + transferencia)
                    
                    transacao_saida = Contas_bancarias(id= conta_bancaria_origem[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria_origem[0].nome_banco, saldo= novo_saldo_origem)
            
                    transacao_entrada = Contas_bancarias(id= conta_bancaria_destino[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria_destino[0].nome_banco, saldo= novo_saldo_destino)
                    
                    transacao_saida.save()
                    transacao_entrada.save()

                    data_transacao_data += intervalo_transacao
                
                #Criando transação futura sem alterar saldo
                instance.pk = None
                instance.data_transacao = data_transacao_data
                instance.transacao_fixa = True
                instance.transacao_efetivada = False
                instance.save()
                
                return render(request, './templates/tela_inicial_do_webapp/principia.html')
                   
            if tipo_transacao == 3: #TRANSAÇÃO PARCELADA
                valor_transacao = Decimal(form['valor'].data)
                qtde_parcelas = int(form['num_parcelas'].data)
                valor_parcela = round(valor_transacao/qtde_parcelas, 2)
                dizima = False
                
                if regularidade == 1: #TRANSAÇÃO FIXA DIÁRIA
                    intervalo_transacao = timedelta(days=1)

                elif regularidade == 2: #TRANSAÇÃO FIXA SEMANAL
                    intervalo_transacao = timedelta(weeks=1)
                
                elif regularidade == 3: #TRANSAÇÃO FIXA MENSAL
                    intervalo_transacao = timedelta(days=30)
                
                else:
                    form.add_error('regularidade','Selecione uma opção de "Regularidade" válida para transação "Fixa".')
                    return render(request, 'templates/tela_de_transacoes/transferir.html', {'form': form})
                
                if  valor_parcela * qtde_parcelas != valor_transacao:
                    dizima = True
                    valor_parcela_1 = valor_parcela
                    valor_parcela_1 += Decimal(0.01)
                    valor_parcela_1 = round(valor_parcela_1, 2)

                for parcela in range(qtde_parcelas):
                    if dizima:
                        if data_atual > data_transacao_data:
                            instance.pk = None
                            instance.data_transacao = data_transacao_data
                            instance.transacao_efetivada = True
                            instance.valor = valor_parcela_1
                            dizima = False
                            instance.save()
            
                            conta_bancaria_origem = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco_origem)
                            conta_bancaria_destino = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco_destino)
                            novo_saldo_origem = (conta_bancaria_origem[0].saldo - valor_parcela_1)
                            novo_saldo_destino = (conta_bancaria_destino[0].saldo + valor_parcela_1)
                            
                            transacao_saida = Contas_bancarias(id= conta_bancaria_origem[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria_origem[0].nome_banco, saldo= novo_saldo_origem)
            
                            transacao_entrada = Contas_bancarias(id= conta_bancaria_destino[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria_destino[0].nome_banco, saldo= novo_saldo_destino)
                            transacao_saida.save()
                            transacao_entrada.save()
                        
                        else:
                            instance.pk = None
                            instance.data_transacao = data_transacao_data
                            instance.transacao_efetivada = False
                            instance.valor = valor_parcela_1
                            dizima = False
                            instance.save()
                    
                    else:
                        if data_atual > data_transacao_data:    
                            instance.pk = None
                            instance.data_transacao = data_transacao_data
                            instance.transacao_efetivada = True
                            instance.valor = valor_parcela
                            dizima = False
                            instance.save()

                            conta_bancaria_origem = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco_origem)
                            conta_bancaria_destino = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco_destino)
                            novo_saldo_origem = (conta_bancaria_origem[0].saldo - valor_parcela)
                            novo_saldo_destino = (conta_bancaria_destino[0].saldo + valor_parcela)
                            
                            transacao_saida = Contas_bancarias(id= conta_bancaria_origem[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria_origem[0].nome_banco, saldo= novo_saldo_origem)
            
                            transacao_entrada = Contas_bancarias(id= conta_bancaria_destino[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria_destino[0].nome_banco, saldo= novo_saldo_destino)
                            transacao_saida.save()
                            transacao_entrada.save()
                            
                        else:
                            instance.pk = None
                            instance.data_transacao = data_transacao_data
                            instance.transacao_efetivada = False
                            instance.valor = valor_parcela
                            dizima = False
                            instance.save()
                    
                    data_transacao_data += intervalo_transacao
            
            atualizar_saldos_transacoes()
            
            return render(request, './templates/tela_inicial_do_webapp/principia.html')
        
        return render(request, 'templates/tela_de_transacoes/transferir.html', {'form': form})
    


@login_required(login_url='home')
def categoria(request):
    if request.method =="GET":  
        usuario = request.user
        form = Criar_categoria_Form()
        return render(request, "templates/tela_de_criar_conta/categoria.html", {'form': form})
        
    elif request.method == "POST":
        usuario = request.user
        classe_categoria=(Categoria_transacao(user_id=usuario))
        form = Criar_categoria_Form(request.POST, instance=classe_categoria)
        
        if form.is_valid():
            try:
                form.save()
                return redirect('app_home')
            
            except:
                form.add_error('categoria','Esta categoria já existe.')
                return render(request, "templates/tela_de_criar_conta/categoria.html", {'form': form})
            
        else:
            return render(request, "templates/tela_de_criar_conta/categoria.html", {'form': form})
        
        return render(request, "templates/tela_de_criar_conta/categoria.html", {'form': form})



def sucesso(request):
    print("Deu boas!")
    return render(request, "sucesso.html")
    

#       ----     Views Do App Aquiiiii !!!!!!!!!!!!!!!!!!!!!!!!!!!!    ----


# from django.views.generic import TemplateView
# class TransactionScreenView(TemplateView):
#     template_name = './templates/tela_de_transacoes/arkhe.html'

# class TransactionScreen2View(TemplateView):
#     template_name = './templates/tela_de_transacoes/despesa.html'

# class TransactionScreen3View(TemplateView):
#     template_name = './templates/tela_de_transacoes/transferir.html'
    
def teste(request):
    atualizar_saldos_transacoes()
    return render(request, './templates/tela_inicial_do_webapp/principia.html')   
    

def atualizar_saldos_transacoes():

    total_transacao_nao_efetivada = Transacao.objects.filter(transacao_efetivada=0, data_transacao__day=datetime.now().day, data_transacao__month=datetime.now().month, data_transacao__year=datetime.now().year).filter(Q(classe_transacao=1) | Q(classe_transacao=2))
    # total_transacao_nao_efetivada = Transacao.objects.filter(transacao_efetivada=0).filter(Q(classe_transacao=1) | Q(classe_transacao=2))
    
    # Varre todas as transações não efetivadas e efetua a transação caso seja o dia da transação
    for transacao in total_transacao_nao_efetivada:
        transacao.transacao_efetivada = True
        id_banco = transacao.conta_id
        usuario_id = transacao.user_id_id
        valor = transacao.valor
        regularidade = transacao.regularidade

        if regularidade == 1: #TRANSAÇÃO FIXA DIÁRIA
            intervalo_transacao = timedelta(days=1)

        elif regularidade == 2: #TRANSAÇÃO FIXA SEMANAL
            intervalo_transacao = timedelta(weeks=1)
        
        elif regularidade == 3: #TRANSAÇÃO FIXA MENSAL
            intervalo_transacao = timedelta(days=30)

        
        #Receita
        if transacao.classe_transacao == 1:
            conta_bancaria = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco)
            novo_saldo = (conta_bancaria[0].saldo + valor)
                    
            efetivacao = Contas_bancarias(id= conta_bancaria[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria[0].nome_banco, saldo= novo_saldo)
            efetivacao.save()
        
            if transacao.transacao_fixa:
                transacao.transacao_fixa = False
                transacao.save()
                
                nova_transacao = transacao
                nova_transacao.pk = None
                nova_transacao.data_transacao += intervalo_transacao
                nova_transacao.transacao_fixa = True
                nova_transacao.save()
                
        #Despesa
        elif transacao.classe_transacao == 2:
            conta_bancaria = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco)
            novo_saldo = (conta_bancaria[0].saldo - valor)
                    
            efetivacao = Contas_bancarias(id= conta_bancaria[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria[0].nome_banco, saldo= novo_saldo)
            efetivacao.save()
            
            if transacao.transacao_fixa:
                transacao.transacao_fixa = False
                transacao.save()
                
                nova_transacao = transacao
                nova_transacao.pk = None
                nova_transacao.data_transacao += intervalo_transacao
                nova_transacao.transacao_fixa = True
                nova_transacao.save()
        
    #Transferência

    total_transacao_nao_efetivada_transferencia = Transacao.objects.filter(transacao_efetivada=0, data_transacao__day=datetime.now().day, data_transacao__month=datetime.now().month, data_transacao__year=datetime.now().year).filter(classe_transacao=3)
    # total_transacao_nao_efetivada_transferencia = Transferencia.objects.filter(classe_transacao=3, transacao_efetivada=0)
    
    for transacao in total_transacao_nao_efetivada_transferencia:
        transacao.transacao_efetivada = True
        id_banco = transacao.conta_id
        usuario_id = transacao.user_id_id
        valor = transacao.valor
        regularidade = transacao.regularidade
        if regularidade == 1: #TRANSAÇÃO FIXA DIÁRIA
            intervalo_transacao = timedelta(days=1)

        elif regularidade == 2: #TRANSAÇÃO FIXA SEMANAL
            intervalo_transacao = timedelta(weeks=1)
        
        elif regularidade == 3: #TRANSAÇÃO FIXA MENSAL
            intervalo_transacao = timedelta(days=30)
        
        conta_destino = Transferencia.objects.filter(transacao_ptr_id=transacao.id)
        id_conta_destino = conta_destino[0].conta_destino_id
        
        #Atualização da conta de Origem (Saída do dinheiro)
        conta_bancaria = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_banco)
        novo_saldo = (conta_bancaria[0].saldo - valor)
                
        efetivacao_origem = Contas_bancarias(id= conta_bancaria[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria[0].nome_banco, saldo= novo_saldo)
        efetivacao_origem.save()
        
        #Atualização da conta de Destino (Entrada do dinheiro)
        conta_bancaria = Contas_bancarias.objects.filter(user_id_id = usuario_id).filter(id = id_conta_destino)
        novo_saldo = (conta_bancaria[0].saldo + valor)
                
        efetivacao_destino = Contas_bancarias(id= conta_bancaria[0].id, user_id_id= usuario_id, nome_banco= conta_bancaria[0].nome_banco, saldo= novo_saldo)
        efetivacao_destino.save()
        
        if transacao.transacao_fixa:
            transacao.transacao_fixa = False
            transacao.save()
            
            nova_transacao = transacao
            nova_transacao.pk = None
            nova_transacao.id = None
            nova_transacao.data_transacao += intervalo_transacao
            nova_transacao.transacao_fixa = True
            nova_transacao.transacao_efetivada = False
            nova_transacao.conta_destino_id = id_conta_destino
            nova_transacao.transacao_ptr_id = nova_transacao.pk
            nova_transacao.save()
        
        else:
            transacao.save()
