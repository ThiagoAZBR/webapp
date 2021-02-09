from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from contasbanco.models import Contas_bancarias
from transacao.models import Categoria_transacao
from django.http import HttpResponse
from .forms import CreateUserForm
from django.forms import ModelForm

 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView, TemplateView

from faleconosco.models import Faleconosco

class Functions:

    def registerPage(self, request):
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

        context={'form':form}
        return render(request, 'templates/home_fora_do_webapp/home_page.html', context)

    def LoginPage(self, request):

        if request.method == 'POST':
            username = request.POST.get('username_login')
            password = request.POST.get('password_login')

            user = authenticate(request, password = password, username = username)

            if user is not None:
                login(request, user)
                return redirect('app_home')
            
        context = {}
        return render(request, 'templates/home_fora_do_webapp/home_page.html', context)