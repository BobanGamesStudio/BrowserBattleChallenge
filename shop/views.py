from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import sell_player_item, get_products_data, buy_item
from inventory.models import PlayerInventory
from inventory.serializers import PlayerInventorySerializer
from currencies.models import Currency

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class SellPlayerItem(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = self.request.user
        player_inventory = PlayerInventory.objects.get(user=user)
        player_currencies = Currency.objects.get(user=user)

        item_id = request.data.get('item_id')

        if item_id not in player_inventory.items:
            return Response({'error': 'Item not found in inventory'}, status=status.HTTP_400_BAD_REQUEST)

        gold_received = sell_player_item(player_inventory, player_currencies, item_id)

        player_inventory_data = PlayerInventorySerializer(player_inventory)
        currencies_data = {
            'gold': player_currencies.gold,
            'diamonds': player_currencies.diamonds,
        }

        return Response({'player_inventory': player_inventory_data.data, 'player_currencies': currencies_data, 'gold_received': gold_received})
    
class LoadProductsData(APIView):
    def get(self, request, format=None):
        try:
            products_data = get_products_data()

            return Response({ 'products_data': products_data })
        except PlayerInventory.DoesNotExist:
            return Response({ 'error': 'Products data not found' })
        except Exception as e:
            return Response({ 'error': 'Something went wrong when retrieving products data' })
        
class BuyItem(APIView):
    def post(self, request, format=None):
        try:
            user = self.request.user
            player_inventory = PlayerInventory.objects.get(user=user)
            player_currencies = Currency.objects.get(user=user)

            gold_spent = buy_item(player_inventory, player_currencies, request.data.get('item_name'))

            player_inventory_data = PlayerInventorySerializer(player_inventory)
            currencies_data = {
                'gold': player_currencies.gold,
                'diamonds': player_currencies.diamonds,
            }

            return Response({'player_inventory': player_inventory_data.data, 'player_currencies': currencies_data, 'gold_spent': gold_spent})
        except PlayerInventory.DoesNotExist:
            return Response({ 'error': 'Products data not found' })
        except Exception as e:  # Capture other exceptions
            return Response({'fightStarted': False, 'message': f'Something went wrong when retrieving products data {str(e)}'})