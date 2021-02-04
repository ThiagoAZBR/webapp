from django.conf.urls import url
from transacao.views import receita, despesa, transferencia, sucesso
from faleconosco.views import TransactionScreenView
from django.urls import path

urlpatterns = [   
    url(r"^nova_receita/", receita, name="nova_receita"),
    url(r"^nova_despesa/", despesa, name="nova_despesa"),
    url(r"^transferencia/", transferencia, name="transferencia"),
    url(r"^nova_entrada_sucesso/", sucesso, name="sucesso"),
    path('transactions', TransactionScreenView.as_view(), name = 'transaction-screen'),
]