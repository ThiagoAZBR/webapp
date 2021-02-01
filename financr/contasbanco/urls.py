from django.conf.urls import url
from contasbanco.views import nova_conta, contas, sucesso

urlpatterns = [    
    url(r"^nova_conta/", nova_conta, name="nova_conta"),
    url(r"^contas/", contas, name="contas"),
    url(r"^nova_conta_sucesso/", sucesso, name="sucesso"),
]