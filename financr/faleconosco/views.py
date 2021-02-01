from django.views.generic.edit import CreateView
from .models import Faleconosco
from django.urls import reverse_lazy

class Formulario(CreateView):
    model = Faleconosco
    fields = ['nome', 'email', 'mensagem']
    template_name = "faleconosco/contato.html"
    success_url = reverse_lazy('fale_conosco')