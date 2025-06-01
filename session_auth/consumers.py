import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from fight.fight_cache import fight_repo #put_player_decision_in_queue
from fight.fight_types import INIT_DECISION, ATTACK_DECISION, AUTO_DECISION, RETREAT_DECISION, LEAVE_DECISION  

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        
        user_id = self.scope["user"].id
        user_group_name = f"user_{user_id}"
        
        async_to_sync(self.channel_layer.group_add)(user_group_name, self.channel_name)

        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You are now connected!'
        }))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        if text_data_json['messageData']:
            if text_data_json['messageData']['type'] == 'userBattleAction':
                user_id = self.scope['user'].id

                if fight_repo.is_player_in_fight(user_id):
                    fight_cache = fight_repo.get_user_cache(user_id)

                    if text_data_json['messageData']['action'] == 'initialDataLoad':
                        fight_cache.put_player_decision_in_queue(INIT_DECISION)
                    elif text_data_json['messageData']['action'] == 'attack':
                        fight_cache.put_player_decision_in_queue(ATTACK_DECISION)
                    elif text_data_json['messageData']['action'] == 'auto':
                        fight_cache.put_player_decision_in_queue(AUTO_DECISION)
                    elif text_data_json['messageData']['action'] == 'retreat':
                        fight_cache.put_player_decision_in_queue(RETREAT_DECISION)
                    elif text_data_json['messageData']['action'] == 'leave':
                        fight_cache.put_player_decision_in_queue(LEAVE_DECISION)

    def server_battle_message(self, battle_message_data="Default message"):
        self.send(text_data=json.dumps({
            'action': battle_message_data['action'],
            'messages': battle_message_data['messages'],
            'update': battle_message_data['update'],
        }))

    def disconnect(self, close_code):
        self.close()

        user_id = self.scope["user"].id
        user_group_name = f"user_{user_id}"

        async_to_sync(self.channel_layer.group_discard)(user_group_name, self.channel_name)