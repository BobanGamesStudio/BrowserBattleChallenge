from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Currency  # Import your Currency model

class GetUserCurrenciesView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user  # Get the current user
            username = user.username

            # Retrieve the user's currency data from the Currency model
            currencies = Currency.objects.get(user=user)

            # Create a dictionary to represent the user's currencies
            currencies_data = {
                'gold': currencies.gold,
                'diamonds': currencies.diamonds,
            }

            return Response({ 'currencies': currencies_data, 'username': str(username) })
        except Exception as e:
            return Response({ 'error': 'Something went wrong when retrieving currencies', 'details': str(e) })
