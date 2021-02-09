from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {

            'username': forms.TextInput(attrs={'placeholder' : ' Nome de Usuário:'}),
            'email' : forms.EmailInput(attrs={'placeholder' : ' E-mail:'}),
            'password1' : forms.PasswordInput(attrs={'placeholder' : ' Senha:'}),
            'password2' : forms.PasswordInput(attrs={'placeholder' : ' Repita a Senha:'}),

        }