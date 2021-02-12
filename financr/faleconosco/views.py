from django.views.generic.edit import CreateView
from .models import Faleconosco
from django.urls import reverse_lazy
from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from .forms import CustomUserAuthenticationForm

@login_required(login_url='home')
def app_home(request):
    if request.method == "GET":
        return render(request, './templates/tela_inicial_do_webapp/principia.html')
    

def home_page(request):
    if request.method == "GET":
        form = CustomUserAuthenticationForm()
        return render(request, './templates/home_fora_do_webapp/home_page.html')
    
    elif request.method == "POST":
        form = CustomUserAuthenticationForm(request.POST)
        user = form
        
        if form.is_valid():
            login(request, user)
        return render(request, './templates/home_fora_do_webapp/home_page.html')

def fale_conosco(request):

    if request.method == "POST":
        nome_completo = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        
        a =Faleconosco(None, nome_completo, email, mensagem)
        a.save()
        
        return render(request, 'templates/home_fora_do_webapp/home_page.html')

    return render(request, 'templates/home_fora_do_webapp/home_page.html')
