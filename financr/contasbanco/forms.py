from django import forms
from .models import Contas_bancarias


class Criar_ContaBanco_Form(forms.ModelForm):
    class Meta:
        model = Contas_bancarias
        exclude = ['user_id']