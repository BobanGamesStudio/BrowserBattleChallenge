from rest_framework import serializers
from .models import PlayerInventory

class PlayerInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerInventory
        exclude = ('next_item_id', 'id', 'user')
