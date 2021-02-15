from django.conf.urls import url
from transacao.views import receita, despesa, transferencia, sucesso, categoria, atualizar_saldos_transacoes, teste
from django.urls import path

urlpatterns = [   
    # url(r"^nova_receita/", receita, name="nova_receita"),
    # url(r"^nova_despesa/", despesa, name="nova_despesa"),
    # url(r"^transferencia/", transferencia, name="transferir"),
    url(r"^criar_categoria/", categoria, name="criar_categoria"),
    url(r"^nova_entrada_sucesso/", sucesso, name="sucesso"),

    #           --- Acessar os Paths para Transações ---
    path('nova_receita/', receita, name = 'adicionar'),
    path('nova_despesa/', despesa, name = 'subtrair'),
    path('transferencia/', transferencia, name = 'transferir'),
    path('teste/', teste, name='teste'),
]