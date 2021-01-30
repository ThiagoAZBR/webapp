from django.conf.urls import url
from transacoes.views import receita, despesa, transferencia, sucesso


urlpatterns = [   
    url(r"^nova_receita/", receita, name="nova_receita"),
    url(r"^nova_despesa/", despesa, name="nova_despesa"),
    url(r"^transferencia/", transferencia, name="transferencia"),
    url(r"^nova_entrada_sucesso/", sucesso, name="sucesso"),
]