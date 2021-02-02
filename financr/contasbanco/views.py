from django.shortcuts import render
from .forms import Criar_ContaBanco_Form

def criar_conta(request):
    if request.method == "GET":
        form = Criar_ContaBanco_Form()
        return render(request, 'criar_conta.html', {'form': form})
    
    elif request.method == "POST":
        form = Criar_ContaBanco_Form(Request.POST)
        
        if form.is_valid():
            pass
        else:    
            return render(request, 'criar_conta.html', {'form': form})
    
    else:
        return render(request, 'fracasso.html')


def contas(request):
    return render(request, "contas.html")


def sucesso(request):
    return render(request, "sucesso.html")
    
