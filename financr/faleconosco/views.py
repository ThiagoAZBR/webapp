from django.views.generic.edit import CreateView
from .models import Faleconosco
from django.urls import reverse_lazy
from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required






       
# Talvez Esteja Errado Abaixo

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "./templates/home_fora_do_webapp/home_page.html"


class AppScreenView(TemplateView):
    template_name = './templates/tela_inicial_do_webapp/principia.html'
    

@login_required(login_url='/accounts/login/')
def app_home(request):
    if request.method == "GET":
        return render(request, './templates/tela_inicial_do_webapp/principia.html')
    

