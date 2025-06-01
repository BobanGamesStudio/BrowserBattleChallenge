#######################################
from rest_framework import serializers
from .models import HeroStats

class HeroStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroStats
        exclude = (
            'base_health',
            'base_damage',
            'base_armor',
            'base_speed',
            'base_strength',
            'base_agility',
            'base_intelligence',
        )