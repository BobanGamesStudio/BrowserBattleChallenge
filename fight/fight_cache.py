from collections import deque
import asyncio
from .fight_types import INIT_DECISION, ATTACK_DECISION, AUTO_DECISION, RETREAT_DECISION, LEAVE_DECISION  

class FightRepository:
    def __init__(self):
        self.active_fights = {}

    def create_user_cache(self, user_id, time_for_turn, hero_stats, monster_stats):
        if not self.is_player_in_fight(user_id):
            new_user_cache = FightCache(time_for_turn, hero_stats, monster_stats)

            self._add_user_cache_to_repo(user_id, new_user_cache)

            return new_user_cache
        
    def delete_user_cache(self, user_id):
        if self.is_player_in_fight(user_id):
            self._remove_user_cache_from_repo(user_id)
        else:
            return False

    def _add_user_cache_to_repo(self, user_id, user_fight_cache):
        self.active_fights[user_id] = user_fight_cache

    def _remove_user_cache_from_repo(self, user_id):
        del self.active_fights[user_id]

    def is_player_in_fight(self, user_id):
        return (user_id is not None) and (user_id in self.active_fights)

    def get_user_cache(self, user_id):
        return self.active_fights[user_id]

fight_repo = FightRepository()

class FightCache:
    def __init__(self, time_for_turn, hero_stats, monster_stats):
        self.inFight = True
        self.fightIsOver = False
        self.playerRetreat = False
        self.autoFight = False
        
        self.heroStats = hero_stats
        self.monsterStats = monster_stats

        self.time_for_turn = time_for_turn

        self.decision_queue = deque()

    def is_in_fight(self):
        return self.inFight

    def get_fight_data(self):
        return {
            'inFight': self.inFight,
            'fightIsOver': self.fightIsOver,
            'playerRetreat': self.playerRetreat,
            'whosRound': None,

            'heroStats': self.heroStats,
            'monsterStats': self.monsterStats,

            'decision_queue': list(self.decision_queue),
        }

    async def wait_for_player_decision(self, expected_decisions):
        wait_time = 0
        while not self.decision_queue and wait_time < self.time_for_turn:

            if ATTACK_DECISION in expected_decisions:
                if not self.autoFight:
                    await asyncio.sleep(0.2)  
                    wait_time += 0.2
                else:
                    wait_time = self.time_for_turn
            elif LEAVE_DECISION in expected_decisions:
                await asyncio.sleep(0.2)  
                wait_time += 0.04

        if self.decision_queue:
            decision = self.decision_queue.popleft()
            if decision == AUTO_DECISION:
                self.autoFight = True
                decision = ATTACK_DECISION
        else:
            if ATTACK_DECISION in expected_decisions:
                decision = ATTACK_DECISION
            elif LEAVE_DECISION in expected_decisions:
                decision = LEAVE_DECISION
        
        return decision

    def put_player_decision_in_queue(self, decision):
        self.decision_queue.append(decision)