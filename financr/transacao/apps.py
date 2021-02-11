from django.apps import AppConfig


class TransacaoConfig(AppConfig):
    name = 'transacao'
    
    def ready(self):
        from transacao import updater
        updater.start()