from django.urls import path
from .views import StartFight, FightStatus, GetHuntLevelsUnlocked

urlpatterns = [
    path('start_fight', StartFight.as_view()),
    path('fight_status', FightStatus.as_view()),
    path('hunt_level_unlocked/', GetHuntLevelsUnlocked.as_view()),
]