from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from contasbanco.models import Contas_bancarias
from transacao.models import Categoria_transacao
from django.http import HttpResponse
from .forms import CreateUserForm

 
from django.contrib.auth.forms import UserCreationForm

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request, 'templates/home_fora_do_webapp/home_page.html', context)
