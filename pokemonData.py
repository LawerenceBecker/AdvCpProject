from moveDatabase import moves

cpMult = {
    1: 0.094,
    2: 0.16639787,
    3: 0.21573247,
    4: 0.25572005,
    5: 0.29024988,
    6: 0.3210876,
    7: 0.34921268,
    8: 0.3752356,
    9: 0.39956728,
    10: 0.4225,
    11: 0.44310755,
    12: 0.4627984,
    13: 0.48168495,
    14: 0.49985844,
    15: 0.51739395
}

pokemon = {
  'Charmander': {
    'baseStats': {
        'hp': 236,
        'attack': 116,
        'defense': 93,
        'type': 'Fire'
    }
  },
  
  'Bulbasaur': {
    'baseStats': {
        'hp': 256,
        'attack': 118,
        'defense': 111,
        'type': 'Grass'
    }
  },
  
  'Squirtle': {
    'baseStats': {
        'hp': 254,
        'attack': 94,
        'defense': 121,
        'type': 'Water'
    }
  },
  
  'Pidgey': {
    'baseStats': {
        'hp': 240,
        'attack': 85,
        'defense': 73,
        'type': 'Normal'
    }
  }
}

# -----------------------------------

# pokemon = {
# hp  'Charmander': {
#         'StartStats': {
#             'pokemonType': 'Fire',
#             'maxHealth': 39,
#             'attack': 52,
#             'defense': 43,
#             'spAttack': 60,
#             'spDefense': 50,
#             'speed': 65
#         },
# hp     'MoveList': {
#             1: 'Scratch',
#             2: 'Growl',
#             3: None,
#             4: 'Ember',
#             5: None,
#             6: None,
#             7: None,
#             8: 'Smokescreen',
#             9: None,
#             10: None,
#             11: None,
#             12: 'Dragon Breath',
#             13: None,
#             14: None,
#             15: None,
#         }
#     }
# }