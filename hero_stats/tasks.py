# tasks.py w jednej z aplikacji, np. 'game'

from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Player  # Zakładając, że masz model Player

@shared_task
def heal_players():
    # players = Player.objects.all()
    # for player in players:
    #     max_health = player.max_health
    #     heal_amount = max_health * 0.05
    #     player.current_health = min(player.current_health + heal_amount, max_health)
    #     player.save()
    print(f"Healed players at {timezone.now()}")
