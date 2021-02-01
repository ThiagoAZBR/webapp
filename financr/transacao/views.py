from django.shortcuts import render
from .forms import Criar_transacao_Form

def receita(request):
    form = Criar_transacao_Form()
    return render(request, "testando.html", {'form': form})


def despesa(request):
    return render(request, "despesa.html")


def transferencia(request):
    return render(request, "transferencia.html")


def sucesso(request):
    return render(request, "sucesso.html")