from django.shortcuts import render
from .forms import Criar_transacao_Form

def receita(Request):
    form = Criar_transacao_Form()
    return render(request, "testando.html", {'form': form})


def despesa(Request):
    return render(request, "despesa.html")


def transferencia(Request):
    return render(request, "transferencia.html")


def sucesso(Request):
    return render(request, "sucesso.html")