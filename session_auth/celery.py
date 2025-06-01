# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Ustawienie domyślnego modułu ustawień Django dla Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'session_auth.settings')

app = Celery('session_auth')

# Konfiguracja Celery za pomocą ustawień z pliku settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodetekcja zadań we wszystkich zainstalowanych aplikacjach Django
app.autodiscover_tasks()

# Definicja harmonogramu zadań
app.conf.beat_schedule = {
    'heal-players-every-minute': {
        'task': 'hero_stats.tasks.heal_players',  
        'schedule': crontab(minute='*/1'),  # Uruchamiane co minutę
    },
}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
