from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=20, default='')
    email = models.CharField(max_length=40, default='')

    class Meta:
        db_table = 'user_profile_data'

    def __str__(self):
        return self.first_name
    
