from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PlayerInventory
from .serializers import PlayerInventorySerializer

import traceback

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class GetPlayerInventory(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            player_inventory = PlayerInventory.objects.get(user=user)
            player_inventory_data = PlayerInventorySerializer(player_inventory)

            return Response({ 'player_inventory': player_inventory_data.data })
        except PlayerInventory.DoesNotExist:
            return Response({ 'error': 'Player inventory not found for this user' })
        except Exception as e:
            return Response({ 'error': 'Something went wrong when retrieving player inventory' })

class MoveItemInInventory(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # try:
        user = self.request.user
        player_inventory = PlayerInventory.objects.get(user=user)

        # Parse data sent from the frontend
        item_id = request.data.get('item_id')
        new_position = request.data.get('new_position')

        # Verify that the item_id exists in the user's inventory
        if item_id not in player_inventory.items:
            return Response({'error': 'Item not found in inventory'}, status=status.HTTP_400_BAD_REQUEST)

        # Update the inventory grid with the new position
        player_inventory.move_item(item_id, new_position)  # Implement this method in your model

        # Serialize the updated inventory and send it back to the frontend
        player_inventory_data = PlayerInventorySerializer(player_inventory)
        return Response({'player_inventory': player_inventory_data.data})

        # except PlayerInventory.DoesNotExist:
        #     return Response({'error': 'Player inventory not found for this user'}, status=status.HTTP_404_NOT_FOUND)
        # except Exception as e:
        #     return Response({'error': 'Something went wrong when moving the item'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UseInventoryItem(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = self.request.user
            player_inventory = PlayerInventory.objects.get(user=user)

            # Parse data sent from the frontend
            item_id   = request.data.get('item_id')
            drop_side = request.data.get('drop_side')

            # Verify that the item_id exists in the user's inventory
            if str(item_id) not in player_inventory.items:
                return Response({'error': 'Item not found in inventory'}, status=status.HTTP_400_BAD_REQUEST)

            item_type = player_inventory.use_item(item_id, drop_side)

            # Serialize the updated inventory and send it back to the frontend
            player_inventory_data = PlayerInventorySerializer(player_inventory)
            return Response({'player_inventory': player_inventory_data.data, 'item_used': item_type})
        except PlayerInventory.DoesNotExist:
            return Response({'error': 'Player inventory not found for this user'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Get the traceback and format it as a string
            tb_str = traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__)
            return Response({
                'error': 'Something went wrong when using the item',
                'details': ''.join(tb_str)  # Join the traceback lines into a single string
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)