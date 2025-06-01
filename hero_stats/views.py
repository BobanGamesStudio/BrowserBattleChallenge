from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HeroStats
from .serializers import HeroStatsSerializer

class GetHeroStats(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            username = user.username

            user_hero_stats = HeroStats.objects.get(user=user)
            user_hero_stats = HeroStatsSerializer(user_hero_stats)

            return Response({ 'hero_stats': user_hero_stats.data, 'username': str(username) })
        except HeroStats.DoesNotExist:
            return Response({ 'error': 'Hero stats not found for this user' })
        except Exception as e:
            return Response({ 'error': 'Something went wrong when retrieving hero stats' })