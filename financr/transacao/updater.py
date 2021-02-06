from apscheduler.schedulers.background import BackgroundScheduler
from .views import atualizar_saldo

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(atualizar_saldo, 'interval', minutes=60)
    scheduler.start()