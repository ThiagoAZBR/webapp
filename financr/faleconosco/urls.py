from django.conf.urls import url
from faleconosco.views import app_home, fale_conosco
from django.urls import path
from django.contrib.auth.forms import UserCreationForm
from users.views import FunctionHomePage
from contasbanco.views import criar_conta, TelacategoriaConta
from transacao.views import categoria


urlpatterns = [
    path("", FunctionHomePage, name = 'home'),
    path('app/', app_home, name = 'app_home'),
    path('criar-conta/', criar_conta, name = 'criar-conta'),
    # path('conta/<int:pk>',editar_conta, name="editar_conta"),
    path('categoria-conta/', categoria, name = 'categoria-conta'),
    path('faleconosco/', fale_conosco, name="faleconosco"),

]