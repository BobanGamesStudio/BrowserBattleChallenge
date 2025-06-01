import threading
import random
import asyncio
import copy
import math

from hero_stats.models import HeroStats
from hero_stats.serializers import HeroStatsSerializer
from user_profile.models import UserProfile  # Import the UserProfile model
from currencies.models import Currency
from inventory.models import PlayerInventory
from inventory.random_inventory_creator import create_random_item
from inventory.constant_item_creator import create_constant_item

from .models import Fight as FightModel
from .monsters import MONSTERS
from .fight_cache import fight_repo
from .fight_messages import FightMessageManager

from .fight_types import INIT_DECISION, ATTACK_DECISION, RETREAT_DECISION, LEAVE_DECISION  

class Fight:
    def __init__(self, combatant_1, combatant_2, enemy_lvl):
        # Check if the user has unlocked the required hunt level
        self.user_fight_model = FightModel.objects.get(user=combatant_1)
        if not self.user_fight_model.can_start_fight(enemy_lvl):
            raise ValueError("User has not unlocked the required hunt level.")
        
        self.combatant_1_stats = self._extract_combatant_stats_player(combatant_1)

        if combatant_2 == "NPC":
            self.combatant_2_stats = self._extract_combatant_stats_NPC(enemy_lvl)

        self.fight_cache_id = self.combatant_1_stats['id']
        time_for_turn = 10
        self.fight_cache    = fight_repo.create_user_cache(self.fight_cache_id, time_for_turn, self.combatant_1_stats, self.combatant_2_stats)
        self.fight_data     = self.fight_cache.get_fight_data()
        self.fight_data["enemy_lvl"] = enemy_lvl
        self.fight_message_manager = FightMessageManager(self.fight_cache_id)
        
        self.thread = threading.Thread(target=self.fight_loop)
        self.thread.start()

    def _extract_combatant_stats_player(self, combatant):
        combatant_id   = combatant.id
        combatant_name = UserProfile.objects.get(user=combatant).nick_name 

        combatant_stats = HeroStats.objects.get(user=combatant)
        combatant_stats = HeroStatsSerializer(combatant_stats).data

        combatant_stats['id'] = combatant_id
        combatant_stats['name'] = combatant_name
        combatant_stats['combatant_type'] = 'user'

        combatant_stats['fight_time'] = 0

        return combatant_stats
    
    def _extract_combatant_stats_NPC(self, enemy_lvl):
        monster_stats = random.choice(MONSTERS[enemy_lvl])
        monster_stats_template = copy.deepcopy(monster_stats)

        monster_stats = {}
        monster_stats["name"]           = monster_stats_template["name"]
        monster_stats["min_dmg"]        = random.randint(monster_stats_template["min_dmg"][0], monster_stats_template["min_dmg"][1])
        monster_stats["max_dmg"]        = random.randint(monster_stats_template["max_dmg"][0], monster_stats_template["max_dmg"][1])
        monster_stats["current_health"] = random.randint(monster_stats_template["min_health"], monster_stats_template["max_health"])
        monster_stats["max_health"]     = monster_stats["current_health"]
        monster_stats["armor"]          = random.randint(monster_stats_template["min_armor"], monster_stats_template["max_armor"])
        monster_stats["speed"]          = round(random.uniform(monster_stats_template["min_speed"], monster_stats_template["max_speed"]), 1)
        monster_stats["image_path"]     = monster_stats_template["image_path"]

        monster_stats["rewards"]        = monster_stats_template["rewards"]
        monster_stats["exp"]            = monster_stats_template["exp"]

        monster_stats['combatant_type'] = 'NPC'

        monster_stats['fight_time'] = 0

        return monster_stats


    def _should_fight_end(self):
        fight_data = self.fight_data

        fight_should_end = False
        
        monster_name = fight_data["monsterStats"]["name"]
        player_name  = fight_data["heroStats"]["name"]

        if fight_data["heroStats"]["current_health"] <= 0:
            fight_should_end = True

            self.fight_message_manager.SendFightOverMessage(monster_name, player_name, 'monster_win')
            self._take_player_lost_exp()

        elif fight_data["monsterStats"]["current_health"] <= 0:
            fight_should_end = True
            
            self.fight_message_manager.SendFightOverMessage(player_name, monster_name, 'player_win')
            self._give_player_win_exp()
            self._give_fight_reward()
            
        elif fight_data["playerRetreat"] == True:
            fight_should_end = True
            
            self.fight_message_manager.SendFightOverMessage(monster_name, player_name, 'player_retreat')

        return fight_should_end

    #region Player decision
    def _wait_for_player_decision(self, expected_decisions):
        playerDecision = asyncio.run(self._get_player_decision(expected_decisions))

        if playerDecision == INIT_DECISION:
            self.fight_message_manager.SendInitData(self.fight_data)

        if playerDecision in expected_decisions:
            return playerDecision
        
    async def _get_player_decision(self, expected_decisions):
        player_decision = await self.fight_cache.wait_for_player_decision(expected_decisions)

        return player_decision
    #endregion

    #region Normal attack
    def _deal_normal_attack(self, combatant_1_stats, combatant_2_stats):
        combatant_1_dmg_dealt = self._calculate_base_attack_damage(combatant_1_stats)
        combatant_2_dmg_taken = self._calculate_received_damage(combatant_1_dmg_dealt, combatant_2_stats)

        combatant_2_stats["current_health"] = max(combatant_2_stats["current_health"] - combatant_2_dmg_taken, 0)

        if combatant_1_stats['combatant_type'] == 'user':
            self.fight_message_manager.SendNormalAttackMessage(combatant_1_stats, combatant_2_stats, combatant_1_dmg_dealt, combatant_2_dmg_taken, 'ally_hit')
        if combatant_2_stats['combatant_type'] == 'user':
            self.fight_message_manager.SendNormalAttackMessage(combatant_1_stats, combatant_2_stats, combatant_1_dmg_dealt, combatant_2_dmg_taken, 'enemy_hit')

        hero_attack_time = 1 / combatant_1_stats['speed']
        combatant_1_stats = combatant_1_stats['fight_time'] + hero_attack_time

        return combatant_1_stats
        
    def _calculate_base_attack_damage(self, unit_data):
        damage = random.randint(unit_data["min_dmg"], unit_data["max_dmg"])

        return damage

    def _calculate_received_damage(self, raw_damage, hit_unit_data):
        armor = hit_unit_data["armor"] 

        relative_damage_reduction = armor / (armor + 5 * raw_damage)
        reduced_damage = raw_damage * (1 - relative_damage_reduction)

        damage_taken = round(reduced_damage)

        return damage_taken
    #endregion


    def _retreat_from_fight(self):
        self.fight_data['playerRetreat'] = True


    def _calculate_Who_Next_Turn(self):
        fight_data = self.fight_data

        # Obliczanie czasów pierwszych tur
        hero_attack_time = 1 / fight_data['heroStats']['speed']
        monster_attack_time = 1 / fight_data['monsterStats']['speed']

        # Obliczanie przewidywanych czasów trwania tur
        hero_after_move_time    = fight_data['heroStats']['fight_time']    + hero_attack_time
        monster_after_move_time = fight_data['monsterStats']['fight_time'] + monster_attack_time

        if hero_after_move_time <= monster_after_move_time:
            fight_data['whosRound'] = 'combatant_1'
            
        else:
            fight_data['whosRound'] = 'combatant_2'

        return fight_data['whosRound']


    def _update_hero_stats(self, stats_to_update, typeOfUpdate='set'):
        user_id = self.fight_data['heroStats']['id']

        try:
            hero_stats_model = HeroStats.objects.get(user_id=user_id)

            if typeOfUpdate == 'set':
                hero_stats_model.modify_stats(stats_to_update)
            elif typeOfUpdate == 'add':
                hero_stats_model.increment_stats(stats_to_update)

        except HeroStats.DoesNotExist:
            print("HeroStats update fail.")

    def _update_hero_hunt_unlocked(self, monster_lvl):
        if monster_lvl == self.user_fight_model.get_hunt_levels_unlocked():
            self.user_fight_model.increase_hunt_levels()

    def _update_hero_currencies(self, currencies_to_update):
        user_id = self.fight_data['heroStats']['id']

        try:
            
            hero_currencies = Currency.objects.get(user_id=user_id)

            if 'gold' in currencies_to_update:
                hero_currencies.add_gold(currencies_to_update['gold'])

        except HeroStats.DoesNotExist:
            print("HeroStats update fail.")

    def _give_fight_reward(self):
        monster_stats = copy.deepcopy(self.fight_data['monsterStats'])

        lootedItems = []
        for reward_name, reward_info in monster_stats['rewards'].items():
            if reward_name == 'gold':
                gold_reward_number = random.randint(monster_stats['rewards']['gold']['min'], monster_stats['rewards']['gold']['max'])

                self._update_hero_currencies({'gold' : gold_reward_number})
                self.fight_message_manager.SendGoldRewardMessage(monster_stats['name'], str(gold_reward_number))

            else: 
                user_id = self.fight_data['heroStats']['id']
                player_inventory = PlayerInventory.objects.get(user_id=user_id)

                if reward_name == 'random_item':
                    chance = reward_info / 100
                    while random.random() <= chance:
                        new_item = create_random_item(self.fight_data["enemy_lvl"])

                        if player_inventory.add_new_item_to_inventory(new_item):
                            lootedItems.append(new_item['name'])
                            chance /= 2
                        else:
                            print("Za mało miejsca w plecaku, przedmiot nie został dodany")
                else:
                    chance = reward_info / 100
                    while random.random() <= chance:
                        new_item = create_constant_item(reward_name)

                        if player_inventory.add_new_item_to_inventory(new_item):
                            lootedItems.append(new_item['name'])
                            chance /= 2
                        else:
                            print("Za mało miejsca w plecaku, przedmiot nie został dodany")
                    
        if len(lootedItems) > 0:    
            self.fight_message_manager.SendItemRewardMessage(lootedItems)


    def _give_player_win_exp(self):
        monster_exp = self.fight_data['monsterStats']['exp']
        monster_lvl = self.fight_data['enemy_lvl']
        hero_lvl = self.fight_data['heroStats']['level']

        exp_value = random.randint(monster_exp['min'], monster_exp['max'])

        # Calculate level difference
        level_difference = monster_lvl - hero_lvl

        # Apply level difference modifier
        if level_difference > 5:
            # Player level is more than 3 levels below monster level (no experience gain)
            exp_value = 0
        elif level_difference > 0:
            # Player level is lower than monster level, apply bonus
            exp_value = int(exp_value * (1 + level_difference * 0.1))  # 10% bonus per level difference
        elif level_difference < 0:
            # Player level is higher than monster level, apply penalty
            exp_value = int(exp_value * (1 - abs(level_difference) * 0.2))  # 10% penalty per level difference
        
        self._update_hero_stats({'current_experience': exp_value}, 'add')

        self.fight_message_manager.SendExpGainedMessage(self.fight_data['monsterStats']['name'], str(exp_value))

    def _take_player_lost_exp(self):
        hero_level = self.fight_data['heroStats']['level']
        hero_current_exp = self.fight_data['heroStats']['current_experience']
        next_level_experience = self.fight_data['heroStats']['next_level_experience']
        
        hero_stats_model = HeroStats.objects.get(user_id=self.fight_data['heroStats']['id'])
        hero_min_exp = hero_stats_model.calculate_exp_for_next_level(hero_level - 1)

        hero_exp_decreased = min( math.floor(0.2 * (next_level_experience - hero_min_exp)), (hero_current_exp - hero_min_exp) )
        self._update_hero_stats({'current_experience': -hero_exp_decreased}, 'add')

        self.fight_message_manager.SendExpLostMessage(self.fight_data['monsterStats']['name'], str(hero_exp_decreased))
        
    def fight_loop(self):
        if self.fight_message_manager.WaitForChannelsGroup():
            self._wait_for_player_decision([INIT_DECISION])
            self.fight_message_manager.SendStartMessage(self.combatant_1_stats['name'], self.combatant_2_stats['name'])

            while not self._should_fight_end():
                if self._calculate_Who_Next_Turn() == 'combatant_1':
                    playerDecision = self._wait_for_player_decision([ATTACK_DECISION, RETREAT_DECISION])
                    
                    if playerDecision == ATTACK_DECISION:
                        self.fight_data['heroStats']['fight_time'] = self._deal_normal_attack(self.fight_data['heroStats'], self.fight_data['monsterStats'])
                    elif playerDecision == RETREAT_DECISION:
                        self._retreat_from_fight()
                else:
                    self.fight_data['monsterStats']['fight_time'] = self._deal_normal_attack(self.fight_data['monsterStats'], self.fight_data['heroStats'])

            self.fight_data['fightIsOver'] = True

            self._update_hero_stats({'current_health': self.fight_data["heroStats"]["current_health"]}, 'set')
            self._update_hero_hunt_unlocked(self.fight_data["enemy_lvl"])
            playerDecision = self._wait_for_player_decision([LEAVE_DECISION])

            self.fight_data['inFight'] = False
            self.fight_message_manager.SendLeaveMessage()
            
            fight_repo.delete_user_cache(self.fight_cache_id)