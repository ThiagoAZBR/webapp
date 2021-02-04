from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm
from contasbanco.models import Contas_bancarias
from transacao.models import Categoria_transacao
 
def dashboard(request):
    return render(request, "users/dashboard.html")
 
def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
            
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            login(request, user)
            
            
            conta_inicial = Contas_bancarias(None, user.id , "Carteira", 0)
            conta_inicial.save()
            
            categorias = ['Mercado', 'Restaurante', 'Lazer', 'Combustível', 'Cartão de Crédito']
            
            for categoria in categorias:
                categoria_inicial = Categoria_transacao(None, user.id, categoria)
                categoria_inicial.save()
               
            return redirect(reverse("dashboard"))
        else:
            return render(request, "users/error.html", {'form':form})