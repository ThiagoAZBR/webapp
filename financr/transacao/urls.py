from django.conf.urls import url
from transacao.views import receita, despesa, transferencia, sucesso, categoria, TransactionScreenView, TransactionScreen2View, TransactionScreen3View
from django.urls import path

urlpatterns = [   
    url(r"^nova_receita/", receita, name="nova_receita"),
    url(r"^nova_despesa/", despesa, name="nova_despesa"),
    url(r"^transferencia/", transferencia, name="transferencia"),
    url(r"^criar_categoria/", categoria, name="criar_categoria"),
    url(r"^nova_entrada_sucesso/", sucesso, name="sucesso"),

    #           --- Acessar os Paths para Transações ---
    path('adicionar', TransactionScreenView.as_view(), name = 'adicionar'),
    path('subtrair', TransactionScreen2View.as_view(), name = 'subtrair'),
    path('transferir', TransactionScreen3View.as_view(), name = 'transferir')
]