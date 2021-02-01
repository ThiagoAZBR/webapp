from django.db import models

class Faleconosco(models.Model):
    nome = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    mensagem = models.CharField(max_length = 4000)
