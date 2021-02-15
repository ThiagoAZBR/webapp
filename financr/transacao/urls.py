from django.conf.urls import url
from transacao.views import TransactionScreenView, TransactionScreen2View, TransactionScreen3View
from transacao.views import receita, despesa, transferencia, sucesso, categoria, atualizar_saldos_transacoes
from django.urls import path

urlpatterns = [   
    # url(r"^nova_receita/", receita, name="nova_receita"),
    # url(r"^nova_despesa/", despesa, name="nova_despesa"),
    url(r"^transferencia/", transferencia, name="transferir"),
    url(r"^nova_entrada_sucesso/", sucesso, name="sucesso"),

    #           --- Acessar os Paths para Transações ---
    path('nova_receita', receita, name = 'adicionar'),
    path('nova_despesa', despesa, name = 'subtrair'),
    # path('transferencia', transferencia.as_view(), name = 'transferir')
]