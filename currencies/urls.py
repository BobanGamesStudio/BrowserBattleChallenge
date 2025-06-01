from django.urls import path
from .views import GetUserCurrenciesView

urlpatterns = [
    path('get_user_currencies', GetUserCurrenciesView.as_view()),
]