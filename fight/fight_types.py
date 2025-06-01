# decision types
INIT_DECISION    = 'init_decisions'
ATTACK_DECISION  = 'attack_decisions'
AUTO_DECISION    = 'auto_decisions'
RETREAT_DECISION = 'retreat_decisions'
LEAVE_DECISION   = 'leave_decisions'

# battle messages actions
FIGHT_INIT_ACTION         = 'fight_init'
FIGHT_START_ACTION        = 'fight_start'
FIGHT_OVER_LOSE_ACTION    = 'fight_over_lose'
FIGHT_OVER_WIN_ACTION     = 'fight_over_win'
FIGHT_OVER_RETREAT_ACTION = 'fight_over_retreat'
FIGHT_HIT_ACTION          = 'fight_hit'
FIGHT_LEAVE_ACTION        = 'fight_leave'
FIGHT_REWARD_ACTION       = 'fight_reward'

# battle messages types
#sbm - server battle message
SERVER_BATTLE_MESSAGE_START  = 'sbm_start' 
SERVER_BATTLE_MESSAGE_ALLY   = 'sbm_ally'
SERVER_BATTLE_MESSAGE_ENEMY  = 'sbm_enemy'
SERVER_BATTLE_MESSAGE_END    = 'sbm_end'
SERVER_BATTLE_MESSAGE_EXP_REWARD = 'sbm_exp_reward'
SERVER_BATTLE_MESSAGE_GOLD_REWARD = 'sbm_gold_reward'
SERVER_BATTLE_MESSAGE_ITEM_REWARD = 'sbm_item_reward'
SERVER_BATTLE_MESSAGE_LEAVE  = 'sbm_none'




# gold reward message
ALL_POSSIBLE_REWARD_MESSAGES = ["After defeating the [Enemy Name], you discover [Gold Number] gold among its possessions.",
                                "Upon searching the defeated [Enemy Name], you find [Gold Number] gold hidden away.",
                                "Scouring the battlefield, you come across [Gold Number] gold as your spoils from the [Enemy Name].",
                                "Your victorious battle against the [Enemy Name] reveals a cache of [Gold Number] gold.",
                                "The fallen [Enemy Name]'s belongings yield [Gold Number] gleaming gold.",
                                "Among the remnants of your battle with the [Enemy Name], you uncover [Gold Number] gold.",
                                "Your triumph over the [Enemy Name] is rewarded with [Gold Number] gold.",
                                "As you loot the defeated [Enemy Name], [Gold Number] gold catch your eye.",
                                "In the aftermath of your encounter with the [Enemy Name], you collect [Gold Number] gold as your share.",
                                "Congratulations, your victory against the [Enemy Name] earns you [Gold Number] gold."]

# item reward message
ALL_POSSIBLE_ITEM_REWARD_MESSAGES = ["As you sift through the loot, a splendid [Item Name] catches your eye. A true treasure!",
                                     "Amidst the spoils of battle, you stumble upon a [Item Name]. How fortuitous!",
                                     "Rummaging through the treasure, you discover a [Item Name]. A fine addition!",
                                     "To your delight, you find a [Item Name] hidden among the spoils. A worthy find!",
                                     "Among the plunder, you unearth a [Item Name]. A valuable prize!",
                                     "Sifting through the remains, you discover a [Item Name]. This will surely aid your quest!",
                                     "As you gather your loot, a [Item Name] gleams enticingly. A fine reward!",
                                     "In the midst of the treasure, you spot a [Item Name]. Fortune smiles upon you!",
                                     "Your careful search reveals a [Item Name]. Time to celebrate your luck!",
                                     "Amidst the chaos, a [Item Name] finds its way into your hands. A fortunate discovery!"
                                    ]

# multiple items reward message
ALL_POSSIBLE_MULTIPLE_ITEMS_REWARD_MESSAGES = [
    "As you rummage through the loot, you uncover not just one, but several treasures! [Item Names] glisten among the spoils.",
    "Amidst the chaos, you find an array of items! Your haul includes [Item Names]. Truly a bountiful find!",
    "To your delight, you discover multiple items hidden among the spoils: [Item Names]. Fortune favors the bold!",
    "Among the plunder, you unearth a collection of valuable items: [Item Names]. What a day!",
    "Sifting through the remains, you discover a trove of items: [Item Names]. A hero's bounty!",
    "As you gather your loot, a multitude of treasures reveal themselves. You find [Item Names]. An impressive haul!",
    "In the midst of the treasure, you spot several gleaming items: [Item Names]. Luck is on your side!",
    "Your careful search reveals an array of items: [Item Names]. Time to celebrate your fortune!",
    "Amidst the battlefield spoils, you collect various items: [Item Names]. A fortunate discovery indeed!",
    "Your victory is sweetened by a trove of items: [Item Names]. A fitting reward for your efforts!"
]


# experience reward message
ALL_POSSIBLE_EXPERIENCE_MESSAGES = [
    "Haha! The defeated [Enemy Name] couldn't handle your might. You gain [XP Number] experience points!",
    "The [Enemy Name] falls before your prowess. You earn [XP Number] experience points!",
    "With a swift strike, you defeat the [Enemy Name] and earn [XP Number] experience points!",
    "You've bested the [Enemy Name]! [XP Number] experience points are yours to claim!",
    "The [Enemy Name] underestimated you. Now you've earned [XP Number] experience points!",
    "Your victory over the [Enemy Name] is celebrated! You gain [XP Number] experience points!",
    "As the [Enemy Name] retreats in defeat, you gain [XP Number] experience points!",
    "The [Enemy Name] cowers in the face of your strength. [XP Number] experience points are yours!",
    "The [Enemy Name] regrets challenging you. [XP Number] experience points are your reward!"
]

# experience loss message
ALL_POSSIBLE_EXPERIENCE_LOSS_MESSAGES = [
    "In your struggle against [Enemy Name], a fatal mistake costs you [XP Number] experience points.",
    "Facing the mighty [Enemy Name], you lose [XP Number] experience points in a moment of weakness.",
    "The [Enemy Name]'s relentless assault leaves you wounded and down [XP Number] experience points.",
    "A desperate retreat from the [Enemy Name] costs you [XP Number] experience points in your haste.",
    "Engaged in fierce combat with [Enemy Name], you lose [XP Number] experience points in the fray.",
    "A cunning maneuver by the [Enemy Name] leaves you vulnerable, losing [XP Number] experience points.",
    "The shadowy presence of [Enemy Name] siphons [XP Number] experience points from your being.",
    "The relentless pursuit of the [Enemy Name] wears you down, costing [XP Number] experience points.",
    "A critical error in judgment against the [Enemy Name] costs you [XP Number] experience points."
]
