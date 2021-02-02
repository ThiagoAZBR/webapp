from django.views.generic.edit import CreateView
from .models import Faleconosco
from django.urls import reverse_lazy
from django.shortcuts import render, reverse

class Formulario(CreateView):
    model = Faleconosco
    fields = ['nome', 'email', 'mensagem']
    template_name = "faleconosco/contato.html"
    success_url = reverse_lazy('fale_conosco')


def fale_conosco(request):

    if request.method == "POST":
        nome_completo = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        
        a =Faleconosco(None, nome_completo, email, mensagem)
        a.save()
        
        return render(request, 'templates/home_fora_do_webapp/home_page.html')

    return render(request, 'templates/home_fora_do_webapp/home_page.html')
    
    
    
    
    
# Talvez Esteja Errado Abaixo

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "./templates/home_fora_do_webapp/home_page.html"

class AppScreenView(TemplateView):
    template_name = './templates/tela_inicial_do_webapp/principia.html'