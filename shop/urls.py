from django.urls import path
from .views import SellPlayerItem, LoadProductsData, BuyItem

urlpatterns = [
    path('sell_item', SellPlayerItem.as_view()),
    path('get', LoadProductsData.as_view()),
    path('buy_item', BuyItem.as_view())
]