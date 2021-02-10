from django.conf.urls import url
from contasbanco.views import criar_conta, contas_banco, sucesso

urlpatterns = [    
    url(r"^criar_conta/", criar_conta, name="criar_conta"),
    url(r"^contas/", contas_banco, name="contas"),
]