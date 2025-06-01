from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib import auth
from rest_framework.response import Response
from user_profile.models import UserProfile
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from .serializers import UserSerializer
from django.db import IntegrityError, transaction

from hero_stats.models import HeroStats
from currencies.models import Currency
from inventory.models import PlayerInventory
from fight.models import Fight

class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        user = self.request.user

        try:
            isAuthenticated = user.is_authenticated

            if isAuthenticated:
                return Response({ 'isAuthenticated': 'success' })
            else:
                return Response({ 'isAuthenticated': 'error' })
        except:
            return Response({ 'error': 'Something went wrong when checking authentication status' })

@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        username = data['username']
        password = data['password']
        re_password  = data['re_password']

        try:
            if password == re_password:
                if User.objects.filter(username=username).exists():
                    return Response({ 'error': 'Username already exists' })
                else:
                    if len(password) < 6:
                        return Response({ 'error': 'Password must be at least 6 characters' })
                    else:
                        with transaction.atomic():
                            try:
                                user = User.objects.create_user(username=username, password=password)

                                user_profile = UserProfile.objects.create(user=user, nick_name='New user', email='')
                                user_stats = HeroStats.objects.create(user=user)

                                player_inventory = PlayerInventory.objects.create(user=user)
                                player_inventory.initialize_inventory_grid()
                                player_inventory.update_hero_inventory_stats()

                                currencies = Currency.objects.create(user=user, gold=0, diamonds=0)
                                player_fight_stats = Fight.objects.create(user=user)
                                
                                return Response({ 'success': 'User created successfully' })
                            except Exception as e:  # Capture IntegrityError
                                return Response({'error': f'Integrity error: {str(e)}'})  # Return the specific error message
            else:
                return Response({ 'error': 'Passwords do not match' })
        except IntegrityError as e:  # Capture IntegrityError
            return Response({'error': f'Integrity error: {str(e)}'})  # Return the specific error message
        except Exception as e:  # Capture other exceptions
            return Response({'error': f'Something went wrong when registering account: {str(e)}'})

@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        username = data['username']
        password = data['password']

        try:
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return Response({ 'success': 'User authenticated' })
            else:
                return Response({ 'error': 'Error Authenticating' })
        except:
            return Response({ 'error': 'Something went wrong when logging in' })

class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            auth.logout(request)
            return Response({ 'success': 'Loggout Out' })
        except:
            return Response({ 'error': 'Something went wrong when logging out' })

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        return Response({ 'success': 'CSRF cookie set' })

class DeleteAccountView(APIView):
    def delete(self, request, format=None):
        user = self.request.user

        try:
            User.objects.filter(id=user.id).delete()

            return Response({ 'success': 'User deleted successfully' })
        except:
            return Response({ 'error': 'Something went wrong when trying to delete user' })
        
class GetUsersView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        users = User.objects.all()

        users = UserSerializer(users, many=True)

        return Response(users.data)