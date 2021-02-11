from django.conf.urls import url
from faleconosco.views import app_home, HomePageView
from django.urls import path
from django.contrib.auth.forms import UserCreationForm
from users.views import FunctionHomePage
from contasbanco.views import TelaCriarConta


urlpatterns = [
    path("", FunctionHomePage, name = 'home'),
    url(r'^app', app_home, name = 'app_home'),
    path('criar-conta', TelaCriarConta, name = 'criar-conta')

]