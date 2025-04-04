from celery import Celery
from celery.schedules import crontab

app = Celery(
    'tasks',
    broker='pyamqp://guest@localhost//',
    backend='rpc://'  # Backend para armazenar resultados
)
app.conf.update(
    result_backend='rpc://',
    beat_scheduler='sqlalchemy_celery_beat.schedulers:DatabaseScheduler',
    beat_dburi='sqlite:///schedule.db',  # Caminho para o banco de dados SQLite
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
)

