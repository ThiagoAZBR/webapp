from django.conf.urls import url
from contasbanco.views import criar_conta, contas, sucesso

urlpatterns = [    
    url(r"^criar_conta/", criar_conta, name="criar_conta"),
    url(r"^contas/", contas, name="contas"),
    # url(r"^nova_conta_sucesso/", sucesso, name="sucesso"),
]