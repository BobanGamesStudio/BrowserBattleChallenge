from django.db import models
from django.contrib.auth.models import User

class HeroStats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Base stats
    base_health = models.IntegerField(default=20)
    base_damage = models.IntegerField(default=2)
    base_armor  = models.IntegerField(default=0)
    base_speed  = models.IntegerField(default=1)
    
    base_strength     = models.IntegerField(default=0)
    base_agility      = models.IntegerField(default=0)
    base_intelligence = models.IntegerField(default=0)

    # Current stats
    level                 = models.IntegerField(default=1)
    prev_level_experience = models.IntegerField(default=30)
    current_experience    = models.IntegerField(default=0)
    next_level_experience = models.IntegerField(default=30)

    current_health = models.IntegerField(default=20)
    max_health     = models.IntegerField(default=20)
    min_dmg        = models.IntegerField(default=2)
    max_dmg        = models.IntegerField(default=2)
    armor          = models.IntegerField(default=0)
    speed          = models.FloatField(default=1.0)

    strength     = models.IntegerField(default=0)
    agility      = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)


    class Meta:
        db_table = 'hero_stats'

    def __str__(self):
        return self.user.username
    
    def get_stats(self):
        stats = {
            'user': self.user.username,

            'base_health': self.base_health, # Shouldn't modify this with modify_stats
            'base_damage': self.base_damage, # Shouldn't modify this with modify_stats
            'base_armor': self.base_armor,   # Shouldn't modify this with modify_stats
            'base_speed': self.base_speed,   # Shouldn't modify this with modify_stats

            'base_strength': self.base_strength,         # Shouldn't modify this with modify_stats
            'base_agility': self.base_agility,           # Shouldn't modify this with modify_stats
            'base_intelligence': self.base_intelligence, # Shouldn't modify this with modify_stats

            'level': self.level,
            'prev_level_experience' : self.prev_level_experience,
            'current_experience': self.current_experience,
            'next_level_experience': self.next_level_experience,

            'current_health': self.current_health,
            'max_health': self.max_health,
            'min_dmg': self.min_dmg,
            'max_dmg': self.max_dmg,
            'armor': self.armor,
            'speed': self.speed,

            'strength': self.strength,
            'agility': self.agility,
            'intelligence': self.intelligence,
        }

        return stats

    def modify_stats(self, stat_updates):
        for stat_name, modified_value in stat_updates.items():
            setattr(self, stat_name, modified_value)

        self.update_current_stats()

    def increment_stats(self, stat_increments):
        for stat_name, incremented_value in stat_increments.items():
            current_value = getattr(self, stat_name, 0)

            if stat_name == 'current_health':
                new_health_value = min(current_value + incremented_value, getattr(self, 'max_health'))
                setattr(self, stat_name, new_health_value)
            else:
                setattr(self, stat_name, current_value + incremented_value)
        
        self.update_current_stats()



    def update_current_stats(self):
        from inventory.models import PlayerInventory

        hero_inventory_model = PlayerInventory.objects.get(user=self.user)
        accumulated_inventory_stats = hero_inventory_model.get_accumulated_stats()

        self.update_current_level()
        self.update_current_attributes(accumulated_inventory_stats)
        self.update_current_health(accumulated_inventory_stats)
        self.update_current_damage(accumulated_inventory_stats)
        self.update_current_armor(accumulated_inventory_stats)
        self.update_current_speed(accumulated_inventory_stats)
        
        self.save()
        
    def update_current_level(self):
        exp_needed_for_next_level = self.calculate_exp_for_next_level(self.level)

        while self.current_experience >= exp_needed_for_next_level:
            self.level += 1
            self.prev_level_experience = self.next_level_experience
            exp_needed_for_next_level = self.calculate_exp_for_next_level(self.level)
            self.next_level_experience = exp_needed_for_next_level

    def calculate_exp_for_next_level(self, current_level):
        if current_level == 1:
            return 30  # Starting level, 30 experience needed to reach level 2
        
        base_exp = 30  # Experience needed to reach level 2
        growth_rate = 1.2  # 20% increase for each level
        
        exp_needed     = base_exp
        exp_difference = base_exp
        for _ in range(2, current_level + 1):
            exp_difference = int(exp_difference * growth_rate)
            exp_needed = exp_needed + exp_difference
        
        return exp_needed

    def update_current_attributes(self, inventory_data):
        self.strength     = self.base_strength     + self.level * 5 + inventory_data["strength"]
        self.agility      = self.base_agility      + self.level * 5 + inventory_data["agility"]
        self.intelligence = self.base_intelligence + self.level * 5 + inventory_data["intelligence"]

    def update_current_health(self, inventory_data):
        hp_percent = self.current_health/self.max_health

        hp_from_strength    = self.strength/5
        self.max_health     = round((self.base_health + hp_from_strength) * (1 + inventory_data["health_percent"]))
        self.current_health = round(self.max_health * hp_percent)

    def update_current_damage(self, inventory_data):
        dmg_from_strength = self.strength/10
        self.min_dmg = round((self.base_damage + dmg_from_strength + inventory_data["min_physical_dmg"]) * (1 + inventory_data["damage_percent"]))
        self.max_dmg = round((self.base_damage + dmg_from_strength + inventory_data["max_physical_dmg"]) * (1 + inventory_data["damage_percent"]))

    def update_current_armor(self, inventory_data):
        dmg_from_strength_agility = min(self.strength/10, self.agility/5)
        self.armor = round((self.base_armor + dmg_from_strength_agility + inventory_data["armor"]) * (1 + inventory_data["armor_percent"]))

    def update_current_speed(self, inventory_data):
        speed_from_agility = self.agility/200
        final_speed = self.base_speed + speed_from_agility + inventory_data["speed"]
        self.speed = round(final_speed, 2)