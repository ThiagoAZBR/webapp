from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from contasbanco.models import Contas_bancarias
from transacao.models import Categoria_transacao
from django.http import HttpResponse
from .forms import CreateUserForm
from django.forms import ModelForm
from faleconosco.models import Faleconosco
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView, TemplateView


from django.views.generic.edit import CreateView
from users.forms import CreateUserForm

class HomePageView(forms.ModelForm):
    class Meta:
        model = Faleconosco
        fields = ['nome', 'email', 'mensagem']



    def verificador(self):



        if 'login_sub' in self.data:

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
        
        elif 'mensagem_sub' in self.data:

            def fale_conosco(request):

                if request.method == "POST":
                    nome_completo = request.POST.get('nome')
                    email = request.POST.get('email')
                    mensagem = request.POST.get('mensagem')
                    
                    a =Faleconosco(None, nome_completo, email, mensagem)
                    a.save()
                    
                    return render(request, 'templates/home_fora_do_webapp/home_page.html')

                return render(request, 'templates/home_fora_do_webapp/home_page.html')

        elif 'register_sub' in self.data:

            def registerPage(self, request):
                form = CreateUserForm()

                if request.method == 'POST':
                    form = CreateUserForm(request.POST)
                    if form.is_valid():
                        form.save()

                context={'form':form}
                return render(request, 'templates/home_fora_do_webapp/home_page.html', context)

