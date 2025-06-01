INVENTORY_BAG_WIDTH  = 8
INVENTORY_BAG_HEIGHT = 10

ALL_ITEMS_TYPES = ['weapon_left', 'weapon_right', 'body_armor', 'gloves', 'boots', 'helmet', 'belt', 'amulet', 'ring']

ALL_ITEMS_SIZES_EQUIPMENT = {'weapon_left'  : '2_3',
                             'weapon_right' : '2_3',
                             'body_armor'   : '2_3',
                             'gloves'       : '2_2',
                             'boots'        : '2_2',
                             'helmet'       : '2_2',
                             'belt'         : '2_2',
                             'amulet'       : '1_1',
                             'ring'         : '1_1'
                            }

ALL_ITEMS_DROP_CHANCES = {'weapon_left'  : 300,
                          'weapon_right' : 350,
                          'body_armor'   : 350,
                          'gloves'       : 600,
                          'boots'        : 600,
                          'helmet'       : 600,
                          'belt'         : 200,
                          'amulet'       : 100,
                          'ring'         : 150
                        }

ITEMS_POSSIBLE_BASE_STATS = {
    'weapon_left' : {'dagger' : {'physical_damage' : {'stat_type' : 'double_value',
                                                      'min_low_value' : lambda item_lvl: round(item_lvl * 1),
                                                      'max_low_value' : lambda item_lvl: round(item_lvl * 1.6),
                                                      'min_high_value' : lambda item_lvl: round(item_lvl * 1.8),
                                                      'max_high_value' : lambda item_lvl: round(item_lvl * 2.6)}
                                },
                    'jagged sword' : {'physical_damage' : {'stat_type' : 'double_value',
                                                      'min_low_value' : lambda item_lvl: round(item_lvl * 1),
                                                      'max_low_value' : lambda item_lvl: round(item_lvl * 1.7),
                                                      'min_high_value' : lambda item_lvl: round(item_lvl * 2),
                                                      'max_high_value' : lambda item_lvl: round(item_lvl * 2.7)}
                                },
                    'rusty sword' : {'physical_damage' : {'stat_type' : 'double_value',
                                                      'min_low_value' : lambda item_lvl: round(item_lvl * 1),
                                                      'max_low_value' : lambda item_lvl: round(item_lvl * 1.5),
                                                      'min_high_value' : lambda item_lvl: round(item_lvl * 2),
                                                      'max_high_value' : lambda item_lvl: round(item_lvl * 3)}
                                },
                    'silver sword' : {'physical_damage' : {'stat_type' : 'double_value',
                                                      'min_low_value' : lambda item_lvl: round(item_lvl * 1.1),
                                                      'max_low_value' : lambda item_lvl: round(item_lvl * 2),
                                                      'min_high_value' : lambda item_lvl: round(item_lvl * 2.1),
                                                      'max_high_value' : lambda item_lvl: round(item_lvl * 3)}
                                },
                    },
    'weapon_right' : {'barrel lid'   : {'armor' : {'stat_type' : 'single_value_int',
                                       'min_value' : lambda item_lvl: round(item_lvl * 1),
                                       'max_value' : lambda item_lvl: round(item_lvl * 2)}
                                },
                    'wooden shield' : {'armor' : {'stat_type' : 'single_value_int',
                                       'min_value' : lambda item_lvl: round(item_lvl * 1.1),
                                       'max_value' : lambda item_lvl: round(item_lvl * 2.1)}
                                },
                    'nordic shield' : {'armor' : {'stat_type' : 'single_value_int',
                                       'min_value' : lambda item_lvl: round(item_lvl * 1.2),
                                       'max_value' : lambda item_lvl: round(item_lvl * 2.2)}
                                },
                    'bronze shield' : {'armor' : {'stat_type' : 'single_value_int',
                                       'min_value' : lambda item_lvl: round(item_lvl * 1.3),
                                       'max_value' : lambda item_lvl: round(item_lvl * 2.3)}
                                },
                    },
    'body_armor' : {'leather shirt'   : {'armor' : {'stat_type' : 'single_value_int',
                                                    'min_value' : lambda item_lvl: round(item_lvl * 2),
                                                    'max_value' : lambda item_lvl: round(item_lvl * 3)}
                                },
                    'rusty chainmail' : {'armor' : {'stat_type' : 'single_value_int',
                                                    'min_value' : lambda item_lvl: round(item_lvl * 2.2),
                                                    'max_value' : lambda item_lvl: round(item_lvl * 3.5)}
                                },
                    'leather vest' : {'armor' : {'stat_type' : 'single_value_int',
                                                'min_value' : lambda item_lvl: round(item_lvl * 2.5),
                                                'max_value' : lambda item_lvl: round(item_lvl * 3.4)}
                                },
                    'rusted armor' : {'armor' : {'stat_type' : 'single_value_int',
                                                'min_value' : lambda item_lvl: round(item_lvl * 2.4),
                                                'max_value' : lambda item_lvl: round(item_lvl * 4)}
                                },
                    },
    'gloves' : {'leather gloves'   : {'armor' : {'stat_type' : 'single_value_int',
                                                'min_value' : lambda item_lvl: round(item_lvl * 0.6),
                                                'max_value' : lambda item_lvl: round(item_lvl * 0.9)}
                            },
                'decorated leather gloves' : {'armor' : {'stat_type' : 'single_value_int',
                                            'min_value' : lambda item_lvl: round(item_lvl * 0.8),
                                            'max_value' : lambda item_lvl: round(item_lvl * 1.1)}
                            },
                'fingerless battle gloves' : {'armor' : {'stat_type' : 'single_value_int',
                                                        'min_value' : lambda item_lvl: round(item_lvl * 1.0),
                                                        'max_value' : lambda item_lvl: round(item_lvl * 1.4)}
                            },
                'battle gloves' : {'armor' : {'stat_type' : 'single_value_int',
                                                    'min_value' : lambda item_lvl: round(item_lvl * 1.1),
                                                    'max_value' : lambda item_lvl: round(item_lvl * 1.6)}
                            },
                },
    'boots' : {'reinforced slippers'   : {'armor' : {'stat_type' : 'single_value_int',
                                                    'min_value' : lambda item_lvl: round(item_lvl * 1),
                                                    'max_value' : lambda item_lvl: round(item_lvl * 1.1)}
                            },
                'iron clogs' : {'armor' : {'stat_type' : 'single_value_int',
                                            'min_value' : lambda item_lvl: round(item_lvl * 1.0),
                                            'max_value' : lambda item_lvl: round(item_lvl * 1.5)}
                            },
                'leather decorated shoes' : {'armor' : {'stat_type' : 'single_value_int',
                                                        'min_value' : lambda item_lvl: round(item_lvl * 1.1),
                                                        'max_value' : lambda item_lvl: round(item_lvl * 1.4)}
                            },
                'steel clad boots' : {'armor' : {'stat_type' : 'single_value_int',
                                                    'min_value' : lambda item_lvl: round(item_lvl * 1.2),
                                                    'max_value' : lambda item_lvl: round(item_lvl * 1.8)}
                            },
                },
    'helmet' : {'leather hat'   : {'armor' : {'stat_type' : 'single_value_int',
                                                'min_value' : lambda item_lvl: round(item_lvl * 1),
                                                'max_value' : lambda item_lvl: round(item_lvl * 1.2)}
                            },
                'iron helmet' : {'armor' : {'stat_type' : 'single_value_int',
                                            'min_value' : lambda item_lvl: round(item_lvl * 1.1),
                                            'max_value' : lambda item_lvl: round(item_lvl * 1.4)}
                            },
                'cloth coif' : {'armor' : {'stat_type' : 'single_value_int',
                                            'min_value' : lambda item_lvl: round(item_lvl * 0.8),
                                            'max_value' : lambda item_lvl: round(item_lvl * 1.0)}
                            },
                'decorated steel helmet' : {'armor' : {'stat_type' : 'single_value_int',
                                                        'min_value' : lambda item_lvl: round(item_lvl * 1.0),
                                                        'max_value' : lambda item_lvl: round(item_lvl * 1.8)}
                            },
                },
    'belt' : {'simple leather belt' : {'armor' : {'stat_type' : 'single_value_int',
                                                  'min_value' : lambda item_lvl: round(item_lvl * 0.5),
                                                  'max_value' : lambda item_lvl: round(item_lvl * 1.0)}
                                },
                "thug's belt" : {'strength' : {'stat_type' : 'single_value_int',
                                                'min_value' : lambda item_lvl: round(item_lvl * 1.0),
                                                'max_value' : lambda item_lvl: round(item_lvl * 2.0)}
                                },
                "necromancer's belt" : {'intelligence' : {'stat_type' : 'single_value_int',
                                                        'min_value' : lambda item_lvl: round(item_lvl * 1.0),
                                                        'max_value' : lambda item_lvl: round(item_lvl * 2.0)}
                            },
                'scale belt' : {'all_attributes' : {'stat_type' : 'single_value_int',
                                                        'min_value' : lambda item_lvl: round(item_lvl * 1),
                                                        'max_value' : lambda item_lvl: round(item_lvl * 1.5)}
                            },
                },
    'amulet' : {'nature amulet' : {'speed' : {'stat_type' : 'single_value_float',
                                                'min_value' : lambda item_lvl: item_lvl * 0.05,
                                                'max_value' : lambda item_lvl: item_lvl * 0.12}
                                },
                'frozen amulet' : {'armor_percent' : {'stat_type' : 'single_value_float',
                                                      'min_value' : lambda item_lvl: 0.01,
                                                      'max_value' : lambda item_lvl: 0.10}
                                },
                'celestial amulet' : {'physical_damage_percent' : {'stat_type' : 'single_value_float',
                                                                    'min_value' : lambda item_lvl: 0.01,
                                                                    'max_value' : lambda item_lvl: 0.12}
                                },
                'eternal amulet' : {'health_percent' : {'stat_type' : 'single_value_float',
                                                        'min_value' : lambda item_lvl: 0.01,
                                                        'max_value' : lambda item_lvl: 0.2}
                                },
                },
    'ring' : {'strength ring' : {'strength' : {'stat_type' : 'single_value_int',
                                                'min_value' : lambda item_lvl: round(item_lvl * 1.4),
                                                'max_value' : lambda item_lvl: round(item_lvl * 4)}
                                },
                'agility ring' : {'agility' : {'stat_type' : 'single_value_int',
                                                'min_value' : lambda item_lvl: round(item_lvl * 1.4),
                                                'max_value' : lambda item_lvl: round(item_lvl * 4)}
                            },
                'intelligence ring' : {'intelligence' : {'stat_type' : 'single_value_int',
                                                        'min_value' : lambda item_lvl: round(item_lvl * 1.4),
                                                        'max_value' : lambda item_lvl: round(item_lvl * 4)}
                            },
                'elemental ring' : {'all_attributes' : {'stat_type' : 'single_value_int',
                                                        'min_value' : lambda item_lvl: round(item_lvl * 1),
                                                        'max_value' : lambda item_lvl: round(item_lvl * 2)}
                            },
                }
}

ITEMS_POSSIBLE_VARIANTS = {
    'weapon_left'  :{'dagger'       : {'image_path' : 'Images/Items/WeaponLeft/Dagger.png'},
                     'jagged sword' : {'image_path' : 'Images/Items/WeaponLeft/JaggedSword.png'},
                     'rusty sword'  : {'image_path' : 'Images/Items/WeaponLeft/RustySword.png'},
                     'silver sword' : {'image_path' : 'Images/Items/WeaponLeft/SilverSword.png'}
                    },
    'weapon_right' :{'barrel lid'    : {'image_path' : 'Images/Items/WeaponRight/BarrelLid.png'},
                     'wooden shield' : {'image_path' : 'Images/Items/WeaponRight/WoodenShield.png'},
                     'nordic shield' : {'image_path' : 'Images/Items/WeaponRight/NordicShield.png'},
                     'bronze shield' : {'image_path' : 'Images/Items/WeaponRight/BronzeShield.png'}
                    },
    'body_armor' :{'leather shirt'   : {'image_path' : 'Images/Items/BodyArmor/LeatherShirt.png'},
                   'rusty chainmail' : {'image_path' : 'Images/Items/BodyArmor/RustyChainmail.png'},
                   'leather vest'    : {'image_path' : 'Images/Items/BodyArmor/LeatherVest.png'},
                   'rusted armor'    : {'image_path' : 'Images/Items/BodyArmor/RustedArmor.png'}
                },
    'gloves' :{'leather gloves'           : {'image_path' : 'Images/Items/Gloves/LeatherGloves.png'},
               'decorated leather gloves' : {'image_path' : 'Images/Items/Gloves/DecoratedLeatherGloves.png'},
               'fingerless battle gloves' : {'image_path' : 'Images/Items/Gloves/FingerlessBattleGloves.png'},
               'battle gloves'            : {'image_path' : 'Images/Items/Gloves/BattleGloves.png'}
                },
    'boots' :{'reinforced slippers'     : {'image_path' : 'Images/Items/Boots/ReinforcedSlippers.png'},
              'iron clogs'              : {'image_path' : 'Images/Items/Boots/IronClogs.png'},
              'leather decorated shoes' : {'image_path' : 'Images/Items/Boots/LeatherDecoratedShoes.png'},
              'steel clad boots'        : {'image_path' : 'Images/Items/Boots/SteelCladBoots.png'}
                },
    'helmet' :{'leather hat'            : {'image_path' : 'Images/Items/Helmet/LeatherHat.png'},
               'iron helmet'            : {'image_path' : 'Images/Items/Helmet/IronHelmet.png'},
               'cloth coif'             : {'image_path' : 'Images/Items/Helmet/ClothCoif.png'},
               'decorated steel helmet' : {'image_path' : 'Images/Items/Helmet/DecoratedSteelHelmet.png'}
                  },
    'belt' : {'simple leather belt' : {'image_path' : 'Images/Items/Belt/SimpleLeatherBelt.png'},
              "thug's belt"         : {'image_path' : "Images/Items/Belt/Thug'sBelt.png"},
              "necromancer's belt"  : {'image_path' : "Images/Items/Belt/Necromancer's Belt.png"},
              "scale belt"          : {'image_path' : 'Images/Items/Belt/ScaleBelt.png'},
               },
    'amulet' : {'nature amulet'    : {'image_path' : 'Images/Items/Amulet/NatureAmulet.png'},
                'frozen amulet'    : {'image_path' : 'Images/Items/Amulet/FrozenAmulet.png'},
                'celestial amulet' : {'image_path' : 'Images/Items/Amulet/CelestialAmulet.png'},
                'eternal amulet'   : {'image_path' : 'Images/Items/Amulet/EternalAmulet.png'},
               },
    'ring' :{'strength ring'     : {'image_path' : 'Images/Items/Ring/RingOfStrength.png'},
             'agility ring'      : {'image_path' : 'Images/Items/Ring/RingOfAgility.png'},
             'intelligence ring' : {'image_path' : 'Images/Items/Ring/RingOfIntelligence.png'},
             'elemental ring'    : {'image_path' : 'Images/Items/Ring/ElementalRing.png'}
            }
}

ALL_ITEMS_VARIANTS_DROP_CHANCES = {
                                   'weapon_left'  : {'dagger'       : {'level_required' : 1, 'max_chance' : 1000, 'peak_lvl_point' : 1, 'standard_deviation' : 6},
                                                     'jagged sword' : {'level_required' : 1, 'max_chance' : 1000, 'peak_lvl_point' : 4, 'standard_deviation' : 6},
                                                     'rusty sword'  : {'level_required' : 4, 'max_chance' : 1000, 'peak_lvl_point' : 6, 'standard_deviation' : 6},
                                                     'silver sword' : {'level_required' : 6, 'max_chance' : 1000, 'peak_lvl_point' : 9, 'standard_deviation' : 6},
                                                    },
                                   'weapon_right' : {'barrel lid'    : {'level_required' : 1, 'max_chance' : 1000, 'peak_lvl_point' : 1, 'standard_deviation' : 5},
                                                     'wooden shield' : {'level_required' : 1, 'max_chance' : 1000, 'peak_lvl_point' : 3, 'standard_deviation' : 5},
                                                     'nordic shield' : {'level_required' : 3, 'max_chance' : 1000, 'peak_lvl_point' : 6, 'standard_deviation' : 5},
                                                     'bronze shield' : {'level_required' : 5, 'max_chance' : 1000, 'peak_lvl_point' : 9, 'standard_deviation' : 5},
                                                     }, 
                                   'body_armor'   : {'leather shirt'   : {'level_required' : 1, 'max_chance' : 1000, 'peak_lvl_point' : 1, 'standard_deviation' : 6},
                                                     'rusty chainmail' : {'level_required' : 1, 'max_chance' : 1000, 'peak_lvl_point' : 4, 'standard_deviation' : 7},
                                                     'leather vest'    : {'level_required' : 5, 'max_chance' : 1000, 'peak_lvl_point' : 7, 'standard_deviation' : 6},
                                                     'rusted armor'    : {'level_required' : 7, 'max_chance' : 1000, 'peak_lvl_point' : 12, 'standard_deviation' : 10},
                                                    },
                                   'gloves'       :{'leather gloves'            : {'level_required' : 1, 'max_chance' : 1000, 'peak_lvl_point' : 2, 'standard_deviation' : 6},
                                                    'decorated leather gloves'  : {'level_required' : 4, 'max_chance' : 1000, 'peak_lvl_point' : 4, 'standard_deviation' : 6},
                                                    'fingerless battle gloves'  : {'level_required' : 6, 'max_chance' : 800, 'peak_lvl_point'  : 7, 'standard_deviation' : 16},
                                                    'battle gloves'             : {'level_required' : 9, 'max_chance' : 800, 'peak_lvl_point'  : 12, 'standard_deviation' : 25},
                                                  },
                                   'boots'       :{'reinforced slippers'     : {'level_required' : 1, 'max_chance' : 1000, 'peak_lvl_point' : 2, 'standard_deviation' : 5},
                                                   'iron clogs'              : {'level_required' : 3, 'max_chance' : 1000, 'peak_lvl_point' : 5, 'standard_deviation' : 7},
                                                   'leather decorated shoes' : {'level_required' : 6, 'max_chance' : 1000, 'peak_lvl_point' : 7, 'standard_deviation' : 10},
                                                   'steel clad boots'        : {'level_required' : 9, 'max_chance' : 900, 'peak_lvl_point' : 10, 'standard_deviation' : 15},
                                                  },
                                   'helmet'       :{'leather hat'            : {'level_required' : 2, 'max_chance' : 1000, 'peak_lvl_point' : 2, 'standard_deviation' : 5},
                                                    'iron helmet'            : {'level_required' : 4, 'max_chance' : 1000, 'peak_lvl_point' : 5, 'standard_deviation' : 6},
                                                    'cloth coif'             : {'level_required' : 7, 'max_chance' : 1000, 'peak_lvl_point' : 8, 'standard_deviation' : 8},
                                                    'decorated steel helmet' : {'level_required' : 9, 'max_chance' : 900, 'peak_lvl_point' : 14, 'standard_deviation' : 15},
                                                  },
                                   'belt'      :{'simple leather belt' : {'level_required' : 3, 'max_chance' : 1000, 'peak_lvl_point' : 5, 'standard_deviation' : 8},
                                                  "thug's belt"         : {'level_required' : 6, 'max_chance' : 1000, 'peak_lvl_point' : 10, 'standard_deviation' : 25},
                                                  "necromancer's belt"  : {'level_required' : 6, 'max_chance' : 1000, 'peak_lvl_point' : 10, 'standard_deviation' : 25},
                                                  "scale belt"          : {'level_required' : 9, 'max_chance' : 900, 'peak_lvl_point' : 15, 'standard_deviation' : 35},
                                                  },
                                   'amulet'       : {'nature amulet'    : {'level_required' : 4, 'max_chance' : 1000, 'peak_lvl_point' : 10, 'standard_deviation' : 50},
                                                     'frozen amulet'    : {'level_required' : 5, 'max_chance' : 1000, 'peak_lvl_point' : 15, 'standard_deviation' : 50},
                                                     'celestial amulet' : {'level_required' : 7, 'max_chance' : 1000, 'peak_lvl_point' : 20, 'standard_deviation' : 50},
                                                     'eternal amulet'   : {'level_required' : 10, 'max_chance' : 1000, 'peak_lvl_point' : 25, 'standard_deviation' : 50},
                                                    },
                                   'ring'         : {'strength ring'     : {'level_required' : 2, 'max_chance' : 1000, 'peak_lvl_point' : 5, 'standard_deviation' : 50},
                                                     'agility ring'      : {'level_required' : 4, 'max_chance' : 1000, 'peak_lvl_point' : 10, 'standard_deviation' : 50},
                                                     'intelligence ring' : {'level_required' : 7, 'max_chance' : 1000, 'peak_lvl_point' : 15, 'standard_deviation' : 50},
                                                     'elemental ring'    : {'level_required' : 10, 'max_chance' : 800, 'peak_lvl_point' : 20, 'standard_deviation' : 50},
                                                    },
                                }