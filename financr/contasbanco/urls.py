from django.conf.urls import url
from contasbanco.views import criar_conta, contas_banco, sucesso
from django.urls import path


urlpatterns = [    
    url(r"^criar_conta/", criar_conta, name="criar_conta"),
    url(r"^contas/", contas_banco, name="contas"),
    # url(r"^nova_conta_sucesso/", sucesso, name="sucesso"),
]