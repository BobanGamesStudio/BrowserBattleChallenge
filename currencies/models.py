from django.db import models
from django.contrib.auth.models import User

class Currency(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gold = models.IntegerField(default=0)
    diamonds = models.IntegerField(default=0)

    class Meta:
        db_table = 'currencies'

    def __str__(self):
        return self.user.username
    
    def add_gold(self, amount):
        """Add the specified amount of gold."""
        if amount > 0:
            self.gold += amount
            self.save()

    def subtract_gold(self, amount):
        """Subtract the specified amount of gold if the user has enough."""
        if amount > 0 and self.gold >= amount:
            self.gold -= amount
            self.save()

    def add_diamonds(self, amount):
        """Add the specified amount of diamonds."""
        if amount > 0:
            self.diamonds += amount
            self.save()

    def subtract_diamonds(self, amount):
        """Subtract the specified amount of diamonds if the user has enough."""
        if amount > 0 and self.diamonds >= amount:
            self.diamonds -= amount
            self.save()

    def get_gold(self):
        """Return the current amount of gold."""
        return self.gold

    def get_diamonds(self):
        """Return the current amount of diamonds."""
        return self.diamonds