
from django.urls import path
from .views import GetHeroStats#, UpdateHeroStats

urlpatterns = [
    path('get', GetHeroStats.as_view()),
    # path('update', UpdateHeroStats.as_view()),
]


