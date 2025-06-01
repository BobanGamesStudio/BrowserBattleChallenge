from django.urls import path
from .views import GetPlayerInventory, MoveItemInInventory, UseInventoryItem

urlpatterns = [
    path('get', GetPlayerInventory.as_view()),
    path('move_in_bag', MoveItemInInventory.as_view()),
    path('use_item', UseInventoryItem.as_view())
]