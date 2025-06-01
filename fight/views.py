from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .fight_logic import Fight

from .fight_cache import fight_repo #is_in_fight
from .models import Fight as FightModel

class StartFight(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            player_id = request.user.id
            fight_in_progress = fight_repo.is_player_in_fight(player_id) #is_in_fight(player_id)

            if not fight_in_progress:
                monster_lvl = int(request.data.get("monster_lvl"))

                try:
                    Fight(request.user, "NPC", monster_lvl)
                    return Response({'fightStarted': True, 'message': 'Fight started successfully'})
                except ValueError as e:
                    return Response({'fightStarted': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'fightStarted': False, 'message': 'You are already in a fight.'})
        except ValueError:
            return Response({'fightStarted': False, 'message': 'Invalid input'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:  # Capture other exceptions
            return Response({'fightStarted': False, 'message': f'Something went wrong when trying to start fight: {str(e)}'})

class FightStatus(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            player_id = request.user.id
            fight_in_progress = fight_repo.is_player_in_fight(player_id) 

            response_data = {
                'playerId': player_id,
                'inFight': fight_in_progress,
            }

            return Response(response_data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class GetHuntLevelsUnlocked(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            player_fight_stats = FightModel.objects.get(user=user)
            
            response_data = {
                'hunt_levels_unlocked': player_fight_stats.get_hunt_levels_unlocked()
            }
            return Response(response_data)
        except FightModel.DoesNotExist:
            return Response({'error': 'Fight stats not found for user'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)