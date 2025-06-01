# monsters.py

MONSTERS = {
    # {'name': 'Rabbit',
    #     'min_dmg': 1,
    #     'max_dmg': 2,
    #     'current_health': 5,
    #     'max_health': 5,
    #     'armor': 0,
    #     'image_path': 'Images/Enemies/Rabbit.png',

    #     'rewards': {'chances' : {'gold' : 1,
    #                              'random_item' : 10000,
    #                              'nothing' : 100},
    #                 'gold' : {'min' : 1, 'max' : 2},
    #                 }
    # },
    # {'name': 'Wolf',
    #     'min_dmg': 1,
    #     'max_dmg': 3,
    #     'current_health': 8,
    #     'max_health': 8,
    #     'armor': 0,
    #     'image_path': 'Images/Enemies/Wolf.png',

    #     'rewards': {'chances' : {'gold' : 1,
    #                              'random_item' : 15000,
    #                              'nothing' : 100},
    #                 'gold' : {'min' : 1, 'max' : 5},
    #                 }
    # },

    1 : [
        {'name': 'Buttercup Bunny',
            'min_dmg': (1, 1),
            'max_dmg': (1, 1),
            'min_health': 3,
            'max_health': 6,
            'min_armor': 0,
            'max_armor': 0,
            'min_speed': 1,
            'max_speed': 1.2,

            'image_path': 'Images/Enemies/0101ButtercupBunny.png',

            'rewards': {'gold'        : {'min' : 1, 'max' : 5},
                        'random_item' : 40,
                        'meat'        : 40
                       },
            'exp': {'min' : 1, 'max' : 1}
        },
        {'name': 'Meadow Lark',
            'min_dmg': (1, 1),
            'max_dmg': (1, 2),
            'min_health': 2,
            'max_health': 6,
            'min_armor': 0,
            'max_armor': 1,
            'min_speed': 1,
            'max_speed': 1.3,

            'image_path': 'Images/Enemies/0101MeadowLark.png',

            'rewards': {'gold'        : {'min' : 2, 'max' : 10},
                        'random_item' : 40,
                       },
            'exp': {'min' : 1, 'max' : 2}
        }
    ],
    2 : [
        {'name': 'Poppy Troll',
            'min_dmg': (1, 2),
            'max_dmg': (2, 3),
            'min_health': 4,
            'max_health': 10,
            'min_armor': 0,
            'max_armor': 2,
            'min_speed': 0.8,
            'max_speed': 1.0,

            'image_path': 'Images/Enemies/0102PoppyTroll.jpeg',
            
            'rewards': {'gold'        : {'min' : 5, 'max' : 12},
                        'random_item' : 40,
                       },
            'exp': {'min' : 1, 'max' : 3}
        },
        {'name': 'Snuggle Bug',
            'min_dmg': (1, 2),
            'max_dmg': (2, 2),
            'min_health': 3,
            'max_health': 6,
            'min_armor': 1,
            'max_armor': 1,
            'min_speed': 1.1,
            'max_speed': 1.2,

            'image_path': 'Images/Enemies/0102SnuggleBug.jpeg',

            'rewards': {'gold'        : {'min' : 8, 'max' : 8},
                        'random_item' : 40,
                        'meat'        : 40
                       },
            'exp': {'min' : 1, 'max' : 3}
        },
    ],
    3 : [
        {'name': 'Cherry Lurker',
            'min_dmg': (1, 2),
            'max_dmg': (2, 6),
            'min_health': 6,
            'max_health': 12,
            'min_armor': 1,
            'max_armor': 2,
            'min_speed': 1.1,
            'max_speed': 1.3,

            'image_path': 'Images/Enemies/0103CherryLurker.png',

            'rewards': {'gold'        : {'min' : 5, 'max' : 15},
                        'random_item' : 40,
                       },
            'exp': {'min' : 2, 'max' : 4}
        },
        {'name': 'Cherry Sprite',
            'min_dmg': (2, 3),
            'max_dmg': (3, 6),
            'min_health': 6,
            'max_health': 10,
            'min_armor': 1,
            'max_armor': 2,
            'min_speed': 1.2,
            'max_speed': 1.5,

            'image_path': 'Images/Enemies/0103CherrySprite.png',

            'rewards': {'gold'        : {'min' : 5, 'max' : 12},
                        'random_item' : 40,
                       },
            'exp': {'min' : 2, 'max' : 5}
        },
    ],
    4 : [
        {'name': 'Dew Winged',
            'min_dmg': (2, 4),
            'max_dmg': (4, 6),
            'min_health': 8,
            'max_health': 14,
            'min_armor': 2,
            'max_armor': 4,
            'min_speed': 1.1,
            'max_speed': 1.3,

            'image_path': 'Images/Enemies/0104DewWinged.png',

            'rewards': {'gold'        : {'min' : 10, 'max' : 15},
                        'random_item' : 40,
                       },
            'exp': {'min' : 3, 'max' : 5}
        },
        {'name': 'Honey Dripper',
            'min_dmg': (4, 6),
            'max_dmg': (6, 10),
            'min_health': 6,
            'max_health': 8,
            'min_armor': 1,
            'max_armor': 2,
            'min_speed': 1.1,
            'max_speed': 1.5,

            'image_path': 'Images/Enemies/0104HoneyDripper.png',

            'rewards': {'gold'        : {'min' : 10, 'max' : 20},
                        'random_item' : 40,
                       },
            'exp': {'min' : 3, 'max' : 6}
        },
    ],
    5 : [
        {'name': 'Snicker Beast',
            'min_dmg': (5, 6),
            'max_dmg': (6, 8),
            'min_health': 10,
            'max_health': 12,
            'min_armor': 2,
            'max_armor': 3,
            'min_speed': 1.2,
            'max_speed': 1.6,

            'image_path': 'Images/Enemies/0105SnickerBeast.png',

            'rewards': {'gold'        : {'min' : 12, 'max' : 15},
                        'random_item' : 40,
                       },
            'exp': {'min' : 4, 'max' : 6}
        },
        {'name': 'Sylvan Watcher',
            'min_dmg': (7, 8),
            'max_dmg': (8, 10),
            'min_health': 15,
            'max_health': 20,
            'min_armor': 4,
            'max_armor': 6,
            'min_speed': 1,
            'max_speed': 1.2,

            'image_path': 'Images/Enemies/0105SylvanWatcher.png',

            'rewards': {'gold'        : {'min' : 8, 'max' : 12},
                        'random_item' : 40,
                        'small life potion' : 10,
                       },
            'exp': {'min' : 4, 'max' : 7}
        },
    ],
    6 : [
        {'name': 'Mistveil Specter',
            'min_dmg': (12, 14),
            'max_dmg': (14, 18),
            'min_health': 14,
            'max_health': 25,
            'min_armor': 5,
            'max_armor': 8,
            'min_speed': 1.2,
            'max_speed': 1.5,

            'image_path': 'Images/Enemies/0106MistveilSpecter.png',

            'rewards': {'gold'        : {'min' : 15, 'max' : 25},
                        'random_item' : 40,
                        'medium life potion' : 10,
                       },
            'exp': {'min' : 5, 'max' : 9}
        },
        {'name': 'Silentclaw Sentinel',
            'min_dmg': (10, 13),
            'max_dmg': (13, 15),
            'min_health': 20,
            'max_health': 35,
            'min_armor': 8,
            'max_armor': 12,
            'min_speed': 1.3,
            'max_speed': 1.6,

            'image_path': 'Images/Enemies/0106SilentclawSentinel.png',

            'rewards': {'gold'        : {'min' : 20, 'max' : 30},
                        'random_item' : 40,
                       },
            'exp': {'min' : 6, 'max' : 8}
        },
    ],
    7 : [
        {'name': 'Canyon Crest Eagle',
            'min_dmg': (14, 16),
            'max_dmg': (16, 20),
            'min_health': 16,
            'max_health': 28,
            'min_armor': 6,
            'max_armor': 12,
            'min_speed': 1.3,
            'max_speed': 1.5,

            'image_path': 'Images/Enemies/0107CanyonCrestEagle.png',

            'rewards': {'gold'        : {'min' : 25, 'max' : 35},
                        'random_item' : 40,
                       },
            'exp': {'min' : 6, 'max' : 9}
        },
        {'name': 'Mysticbloom Nymph',
            'min_dmg': (18, 24),
            'max_dmg': (24, 30),
            'min_health': 15,
            'max_health': 20,
            'min_armor': 4,
            'max_armor': 8,
            'min_speed': 1.4,
            'max_speed': 1.7,

            'image_path': 'Images/Enemies/0107MysticbloomNymph.png',

            'rewards': {'gold'        : {'min' : 30, 'max' : 50},
                        'random_item' : 40,
                       },
            'exp': {'min' : 7, 'max' : 9}
        },
    ],
    8 : [
        {'name': 'Crystal Hummingbird',
            'min_dmg': (18, 24),
            'max_dmg': (24, 28),
            'min_health': 18,
            'max_health': 24,
            'min_armor': 6,
            'max_armor': 9,
            'min_speed': 1.5,
            'max_speed': 1.8,

            'image_path': 'Images/Enemies/0108CrystalHummingbird.png',

            'rewards': {'gold'        : {'min' : 35, 'max' : 45},
                        'random_item' : 40,
                       },
            'exp': {'min' : 8, 'max' : 11}
        },
        {'name': 'Garden Elf',
            'min_dmg': (18, 20),
            'max_dmg': (20, 22),
            'min_health': 20,
            'max_health': 26,
            'min_armor': 10,
            'max_armor': 14,
            'min_speed': 1.3,
            'max_speed': 1.6,

            'image_path': 'Images/Enemies/0108GardenElf.png',

            'rewards': {'gold'        : {'min' : 40, 'max' : 60},
                        'random_item' : 40,
                       },
            'exp': {'min' : 8, 'max' : 12}
        },
        {'name': 'Verdant Serpent',
            'min_dmg': (20, 22),
            'max_dmg': (22, 24),
            'min_health': 22,
            'max_health': 28,
            'min_armor': 8,
            'max_armor': 12,
            'min_speed': 1.4,
            'max_speed': 1.7,

            'image_path': 'Images/Enemies/0108VerdantSerpent.png',

            'rewards': {'gold'        : {'min' : 35, 'max' : 50},
                        'random_item' : 40,
                       },
            'exp': {'min' : 8, 'max' : 14}
        },
    ],
    9 : [
        {'name': 'Hushwing Nightingale',
            'min_dmg': (24, 28),
            'max_dmg': (28, 32),
            'min_health': 20,
            'max_health': 28,
            'min_armor': 10,
            'max_armor': 12,
            'min_speed': 1.5,
            'max_speed': 1.8,

            'image_path': 'Images/Enemies/0109HushwingNightingale.png',

            'rewards': {'gold'        : {'min' : 45, 'max' : 65},
                        'random_item' : 40,
                       },
            'exp': {'min' : 9, 'max' : 13}
        },
        {'name': 'Moon Moth',
            'min_dmg': (26, 28),
            'max_dmg': (30, 36),
            'min_health': 20,
            'max_health': 26,
            'min_armor': 6,
            'max_armor': 12,
            'min_speed': 1.8,
            'max_speed': 2.0,

            'image_path': 'Images/Enemies/0109MoonMoth.png',

            'rewards': {'gold'        : {'min' : 35, 'max' : 65},
                        'random_item' : 40,
                       },
            'exp': {'min' : 9, 'max' : 13}
        },
        {'name': 'Slumbering Grove Guardian',
            'min_dmg': (22, 24),
            'max_dmg': (26, 30),
            'min_health': 30,
            'max_health': 40,
            'min_armor': 15,
            'max_armor': 20,
            'min_speed': 1.2,
            'max_speed': 1.4,

            'image_path': 'Images/Enemies/0109SlumberingGroveGuardian.png',

            'rewards': {'gold'        : {'min' : 40, 'max' : 65},
                        'random_item' : 40,
                       },
            'exp': {'min' : 9, 'max' : 14}
        },
        {'name': 'Starlight Stag',
            'min_dmg': (20, 22),
            'max_dmg': (22, 24),
            'min_health': 22,
            'max_health': 28,
            'min_armor': 8,
            'max_armor': 12,
            'min_speed': 1.5,
            'max_speed': 1.8,

            'image_path': 'Images/Enemies/0109StarlightStag.png',

            'rewards': {'gold'        : {'min' : 50, 'max' : 80},
                        'random_item' : 40,
                       },
            'exp': {'min' : 9, 'max' : 13}
        },
    ],
    10 : [
        {'name': 'Blossom Whisper Fae',
            'min_dmg': (30, 34),
            'max_dmg': (36, 40),
            'min_health': 30,
            'max_health': 40,
            'min_armor': 15,
            'max_armor': 20,
            'min_speed': 2.2,
            'max_speed': 3,

            'image_path': 'Images/Enemies/0110BlossomWhisperFae.png',

            'rewards': {'gold'        : {'min' : 80, 'max' : 100},
                        'random_item' : 40,
                       },
            'exp': {'min' : 12, 'max' : 20}
        },
        {'name': 'Butterfly princess',
            'min_dmg': (26, 28),
            'max_dmg': (28, 30),
            'min_health': 26,
            'max_health': 32,
            'min_armor': 12,
            'max_armor': 16,
            'min_speed': 1.8,
            'max_speed': 2.2,

            'image_path': 'Images/Enemies/0110ButterflyPrincess.png',

            'rewards': {'gold'        : {'min' : 60, 'max' : 80},
                        'random_item' : 40,
                       },
            'exp': {'min' : 10, 'max' : 15}
        },
        {'name': 'Dewdrop Sprite',
            'min_dmg': (22, 26),
            'max_dmg': (26, 30),
            'min_health': 26,
            'max_health': 30,
            'min_armor': 6,
            'max_armor': 16,
            'min_speed': 1.4,
            'max_speed': 2.0,

            'image_path': 'Images/Enemies/0110DewdropSprite.png',

            'rewards': {'gold'        : {'min' : 50, 'max' : 80},
                        'random_item' : 40,
                       },
            'exp': {'min' : 10, 'max' : 14}
        },
        {'name': 'Gossamer Dreamweaver',
            'min_dmg': (24, 28),
            'max_dmg': (28, 32),
            'min_health': 24,
            'max_health': 32,
            'min_armor': 12,
            'max_armor': 16,
            'min_speed': 1.8,
            'max_speed': 2.0,

            'image_path': 'Images/Enemies/0110GossamerDreamweaver.png',

            'rewards': {'gold'        : {'min' : 50, 'max' : 80},
                        'random_item' : 40,
                       },
            'exp': {'min' : 10, 'max' : 16}
        },
        {'name': 'Luminescent Firefly',
            'min_dmg': (26, 30),
            'max_dmg': (30, 36),
            'min_health': 22,
            'max_health': 28,
            'min_armor': 8,
            'max_armor': 12,
            'min_speed': 1.9,
            'max_speed': 2.3,

            'image_path': 'Images/Enemies/0110LuminescentFirefly.png',

            'rewards': {'gold'        : {'min' : 50, 'max' : 80},
                        'random_item' : 40,
                       },
            'exp': {'min' : 10, 'max' : 14}
        },
    ]
}
