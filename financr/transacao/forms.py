from django import forms
from .models import Transacao, Transferencia, Categoria_transacao
from contasbanco.models import Contas_bancarias
from datetime import date

class  DateInput(forms.DateInput):
    input_type = 'date'

class Criar_transacao_Form(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ('descricao', 'valor','data_transacao','conta','categoria_transacao','tipo_transacao','regularidade','num_parcelas','observacoes')
        widgets = {
            'data_transacao': DateInput(format='%d/%m/%Y'),
        }


class Criar_transferencia_Form(forms.ModelForm):
    class Meta:
        model = Transferencia
        fields = ('descricao', 'valor','data_transacao','conta','categoria_transacao','tipo_transacao','regularidade','num_parcelas','observacoes','conta_destino')
        widgets = {
            'data_transacao': DateInput(format='%d/%m/%Y'),
        }


class Criar_categoria_Form(forms.ModelForm):
    class Meta:
        model = Categoria_transacao
        fields = ('categoria','classe_transacao')
