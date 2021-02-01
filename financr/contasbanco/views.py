from django.shortcuts import render

def nova_conta(request):
    return render(request, "nova_conta.html")


def contas(request):
    return render(request, "contas.html")


def sucesso(request):
    return render(request, "sucesso.html")
    
