# fight/models.py
from django.db import models
from django.contrib.auth.models import User

class Fight(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hunt_levels_unlocked = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - Hunt Levels Unlocked: {self.hunt_levels_unlocked}"

    def can_start_fight(self, monster_lvl):
        """Check if the user has unlocked the required hunt level."""
        return 1 <= monster_lvl <= self.get_hunt_levels_unlocked()

    def increase_hunt_levels(self):
        """Increase the number of hunt levels unlocked by the specified amount."""
        self.hunt_levels_unlocked += 1
        self.save()

    def get_hunt_levels_unlocked(self):
        """Return the number of hunt levels unlocked."""
        return self.hunt_levels_unlocked