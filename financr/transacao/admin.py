from django.contrib import admin
from transacao.models import Categoria_transacao, Transacao, Transferencia

# Register your models here.

admin.site.register(Categoria_transacao)
admin.site.register(Transacao)
admin.site.register(Transferencia)