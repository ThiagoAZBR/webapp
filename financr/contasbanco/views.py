from django.shortcuts import render

def nova_conta(Request):
    return render(request, "nova_conta.html")


def contas(Request):
    return render(request, "contas.html")


def sucesso(Request):
    return render(request, "sucesso.html")
    
