import time
import random

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from .fight_types import FIGHT_INIT_ACTION, FIGHT_START_ACTION, FIGHT_OVER_LOSE_ACTION, FIGHT_OVER_WIN_ACTION, FIGHT_OVER_RETREAT_ACTION, FIGHT_HIT_ACTION
from .fight_types import FIGHT_LEAVE_ACTION, FIGHT_REWARD_ACTION

from .fight_types import SERVER_BATTLE_MESSAGE_START, SERVER_BATTLE_MESSAGE_ALLY, SERVER_BATTLE_MESSAGE_ENEMY, SERVER_BATTLE_MESSAGE_END
from .fight_types import SERVER_BATTLE_MESSAGE_EXP_REWARD, SERVER_BATTLE_MESSAGE_GOLD_REWARD, SERVER_BATTLE_MESSAGE_ITEM_REWARD, SERVER_BATTLE_MESSAGE_LEAVE

from .fight_types import ALL_POSSIBLE_REWARD_MESSAGES, ALL_POSSIBLE_ITEM_REWARD_MESSAGES, ALL_POSSIBLE_MULTIPLE_ITEMS_REWARD_MESSAGES, ALL_POSSIBLE_EXPERIENCE_MESSAGES 
from .fight_types import ALL_POSSIBLE_EXPERIENCE_LOSS_MESSAGES

class FightMessageManager:
    def __init__(self, fight_cache_id):
        self.fight_cache_id = fight_cache_id

        self.InitChannelGroupName()

        self.fightHistory = []

    def InitChannelGroupName(self):
        self.channel_group_name = 'user_' + str(self.fight_cache_id)

    def WaitForChannelsGroup(self, max_attempts=50, poll_interval=0.2):
        channel_layer = get_channel_layer()
        attempts = 0
        
        while attempts < max_attempts:
            if self.channel_group_name in channel_layer.groups:
                return True
            else:
                time.sleep(poll_interval)
                attempts += 1
        else:
            print(f"Group '{self.channel_group_name}' was not found after {max_attempts} attempts")
            return False
    
        
    def CurrentLifePercentStr(self, combatant_stats, decimal_places=1):
        if combatant_stats["current_health"] <= 0:
            return "(0%)"

        percentage = (combatant_stats["current_health"] / combatant_stats["max_health"]) * 100.0
        if percentage % 1 != 0:
            life_percent_string = "{:.{}f}%".format(percentage, decimal_places)
        else:
            life_percent_string = "{:.0f}%".format(percentage)

        return "(" + life_percent_string + ")"


    def SendBattleMessage(self, action, messages, update= {}, save_history=True):
        channel_layer = get_channel_layer()

        if save_history:
            self.fightHistory.extend(messages)

        async_to_sync(channel_layer.group_send)(
        self.channel_group_name,
            {'type': 'server_battle_message', 
            'action': action,
            'messages': messages,
            'update': update}
        )

    def SendInitData(self, fight_data):
        initial_data_to_update = {
            "name_1"           : fight_data["heroStats"]["name"],
            "min_damage_1"     : fight_data["heroStats"]["min_dmg"],
            "max_damage_1"     : fight_data["heroStats"]["max_dmg"],
            "current_health_1" : fight_data["heroStats"]["current_health"],
            "max_health_1"     : fight_data["heroStats"]["max_health"],
            "armor_1"          : fight_data["heroStats"]["armor"],
            "speed_1"          : fight_data["heroStats"]["speed"],

            "name_2"           : fight_data["monsterStats"]["name"],
            "min_damage_2"     : fight_data["monsterStats"]["min_dmg"],
            "max_damage_2"     : fight_data["monsterStats"]["max_dmg"],
            "current_health_2" : fight_data["monsterStats"]["current_health"],
            "max_health_2"     : fight_data["monsterStats"]["max_health"],
            "armor_2"          : fight_data["monsterStats"]["armor"],
            "speed_2"          : fight_data["monsterStats"]["speed"],
            "image_path_2"     : fight_data["monsterStats"]["image_path"],

            "fight_is_over_3" : fight_data['fightIsOver']
        }
        
        self.SendBattleMessage(FIGHT_INIT_ACTION, self.fightHistory, initial_data_to_update, save_history= False)

    def SendStartMessage(self, combatant_1_name, combatant_2_name):
        start_message = 'Battle started between ' + combatant_1_name + ' and ' + combatant_2_name

        self.SendBattleMessage(FIGHT_START_ACTION, [{ 'message_type': SERVER_BATTLE_MESSAGE_START, 'message': start_message }])

    def SendNormalAttackMessage(self, combatant_1_stats, combatant_2_stats, combatant_1_dmg_dealt, combatant_2_dmg_taken, whos_hit):
        hitsLine    = combatant_1_stats['name'] + ' ' + self.CurrentLifePercentStr(combatant_1_stats) + ' hits with ' + str(combatant_1_dmg_dealt) + ' damage.\n'
        recivesLine = combatant_2_stats['name'] + ' ' + self.CurrentLifePercentStr(combatant_2_stats) + ' takes ' + str(combatant_2_dmg_taken) + ' damage.'
        
        hit_message = hitsLine + recivesLine

        if whos_hit == 'ally_hit':
            self.SendBattleMessage(FIGHT_HIT_ACTION, [{ 'message_type': SERVER_BATTLE_MESSAGE_ALLY, 'message': hit_message }], {"current_health_2": combatant_2_stats['current_health']})
        elif whos_hit == 'enemy_hit':
            self.SendBattleMessage(FIGHT_HIT_ACTION, [{ 'message_type': SERVER_BATTLE_MESSAGE_ENEMY, 'message': hit_message }], {"current_health_1": combatant_2_stats['current_health']})

    def SendFightOverMessage(self, winner_name, loser_name, reason):
        if reason == 'monster_win':
            lose_message = winner_name + " won the fight with weak " + loser_name + "!"
            self.SendBattleMessage(FIGHT_OVER_LOSE_ACTION, [{ 'message_type': SERVER_BATTLE_MESSAGE_END, 'message': lose_message }], {"fight_is_over_3" : True})
        elif reason == 'player_win':
            win_message = winner_name + " won the fight with filthy " + loser_name + "!"
            self.SendBattleMessage(FIGHT_OVER_WIN_ACTION, [{ 'message_type': SERVER_BATTLE_MESSAGE_END, 'message': win_message }], {"fight_is_over_3" : True})
        elif reason == 'player_retreat':
            retreat_message = loser_name + " escaped from the fight like a coward!"
            self.SendBattleMessage(FIGHT_OVER_RETREAT_ACTION, [{ 'message_type': SERVER_BATTLE_MESSAGE_END, 'message': retreat_message }], {"fight_is_over_3" : True})
    
    def SendGoldRewardMessage(self, monsterName, goldReward):
        random_message = random.choice(ALL_POSSIBLE_REWARD_MESSAGES)
        reward_message = random_message.replace("[Enemy Name]", monsterName)
        reward_message = reward_message.replace("[Gold Number]", goldReward)
    
        self.SendBattleMessage(FIGHT_REWARD_ACTION, [{ 'message_type': SERVER_BATTLE_MESSAGE_GOLD_REWARD, 'message': reward_message }])
    
    def SendItemRewardMessage(self, items):
        if len(items) == 1:
            random_message = random.choice(ALL_POSSIBLE_ITEM_REWARD_MESSAGES)
            reward_message = random_message.replace("[Item Name]", items[0])
        elif len(items) > 1:
            random_message = random.choice(ALL_POSSIBLE_MULTIPLE_ITEMS_REWARD_MESSAGES)
            items_str = ", ".join(items)  # Łączy przedmioty przecinkami
            
            reward_message = random_message.replace("[Item Names]", items_str)
        
        self.SendBattleMessage(FIGHT_REWARD_ACTION, [{ 'message_type': SERVER_BATTLE_MESSAGE_ITEM_REWARD, 'message': reward_message }])

    def SendExpGainedMessage(self, monsterName, expGained):
        random_message = random.choice(ALL_POSSIBLE_EXPERIENCE_MESSAGES)
        reward_message = random_message.replace("[Enemy Name]", monsterName)
        reward_message = reward_message.replace("[XP Number]", expGained)
    
        self.SendBattleMessage(FIGHT_REWARD_ACTION, [{ 'message_type': SERVER_BATTLE_MESSAGE_EXP_REWARD, 'message': reward_message }])
    
    def SendExpLostMessage(self, monsterName, expLost):
        random_message = random.choice(ALL_POSSIBLE_EXPERIENCE_LOSS_MESSAGES)
        reward_message = random_message.replace("[Enemy Name]", monsterName)
        reward_message = reward_message.replace("[XP Number]", expLost)
    
        self.SendBattleMessage(FIGHT_REWARD_ACTION, [{ 'message_type': SERVER_BATTLE_MESSAGE_EXP_REWARD, 'message': reward_message }])

    def SendLeaveMessage(self):
        self.SendBattleMessage(FIGHT_LEAVE_ACTION, [{ 'message_type': SERVER_BATTLE_MESSAGE_LEAVE, 'message': '' }])


        