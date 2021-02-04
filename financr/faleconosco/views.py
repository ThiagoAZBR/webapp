from django.views.generic.edit import CreateView
from .models import Faleconosco
from django.urls import reverse_lazy

class Formulario(CreateView):
    model = Faleconosco
    fields = ['nome', 'email', 'mensagem']
    template_name = "faleconosco/contato.html"
    success_url = reverse_lazy('fale_conosco')



# Talvez Esteja Errado Abaixo

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "./templates/home_fora_do_webapp/home_page.html"

class AppScreenView(TemplateView):
    template_name = './templates/tela_inicial_do_webapp/principia.html'

class TransactionScreenView(TemplateView):
    template_name = './templates/tela_de_transacoes/arkhe.html'