from apscheduler.schedulers.background import BackgroundScheduler
from .views import atualizar_saldos_transacoes

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(atualizar_saldos_transacoes, 'interval', days=1)
    # scheduler.add_job(gerar_transacao, 'interval', days=1)
    scheduler.start()
    
