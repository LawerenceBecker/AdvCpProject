## Experience info https://bulbapedia.bulbagarden.net/wiki/Experience

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

expYield = {
    'Simimander': 65,
    'Sewbasaur': 64,
    'Tirninja': 64,
    'Digvee': 92,
    'Drudpa': 170,
    'Kakuita': 59,
    'Manmite': 89,
    'Manrupt': 175
}

expTotal = {
    1: 6,
    2: 21,
    3: 51,
    4: 100,
    5: 172,
    6: 274,
    7: 409,
    8: 583,
    9: 800,
    10: 1064,
    11: 1382,
    12: 1757,
    13: 2195,
    14: 2700,
    15: 3276,
    16: 14790
}

pokemon = {
  'Simimander': { ## based on charmander
    'baseStats': {
        'hp': 236,
        'attack': 116,
        'defense': 93,
        'type': 'Fire'
    }
  },
  
  'Sewbasaur': { ## based on bulbasuar
    'baseStats': {
        'hp': 256,
        'attack': 118,
        'defense': 111,
        'type': 'Grass'
    }
  },
  
  'Tirninja': { ## based on Tirtouga
    'baseStats': {
        'hp': 144,
        'attack': 134,
        'defense': 146,
        'type': 'Water'
    }
  },
  
  'Belloraid': { ## based on bellsprout
    'baseStats': {
        'hp': 137,
        'attack': 139,
        'defense': 61,
        'type': 'Grass'
    }
  },

  'Digvee': { ## based on eevee
    'baseStats': {
        'hp': 146,
        'attack': 104,
        'defense': 114,
        'type': 'Normal'
    }
  },

  'Drudpa': { ## based on Druddigon
    'baseStats': {
        'hp': 184,
        'attack': 213,
        'defense': 170,
        'type': 'Dragon'
    }
  },

  'Kakuita': { ## based on Gothia
    'baseStats': {
        'hp': 128,
        'attack': 98,
        'defense': 112,
        'type': 'Psychic'
    }
  },

  'Manmite': { ## based on Magnemite
    'baseStats': {
        'hp': 93,
        'attack': 165,
        'defense': 121,
        'type': 'Electric'
    }
  },

  'Manrupt': { ## based on Camerupt
    'baseStats': {
        'hp': 172,
        'attack': 194,
        'defense': 136,
        'type': 'Fire'
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