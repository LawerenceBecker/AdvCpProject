from moveDatabase import moves

pokemon = {
  'Charmander': {
    'StartStats': {
        'maxHealth': 39,
        'attack': 52,
        'defense': 43,
        'spAttack': 60,
        'spDefense': 50,
        'speed': 65
    },
    'CP': 250,
    'Type': 'Fire'
  },
  
  'Bulbasaur': {
    'StartStats': {
        'maxHealth': 45,
        'attack': 49,
        'defense': 49,
        'spAttack': 65,
        'spDefense': 65,
        'speed': 45
    },
    'CP': 250,
    'Type': 'Grass'
  },
  
  'Squirtle': {
    'StartStats': {
        'maxHealth': 44,
        'attack': 48,
        'defense': 65,
        'spAttack': 50,
        'spDefense': 64,
        'speed': 43
    },
    'CP': 250,
    'Type': 'Water'
  },
  
  'Pidgey': {
    'StartStats': {
        'maxHealth': 40,
        'attack': 45,
        'defense': 40,
        'spAttack': 35,
        'spDefense': 35,
        'speed': 56
    },
    'CP': 250,
    'Type': 'Normal'
  }
}

# -----------------------------------

# pokemon = {
#     'Charmander': {
#         'StartStats': {
#             'pokemonType': 'Fire',
#             'maxHealth': 39,
#             'attack': 52,
#             'defense': 43,
#             'spAttack': 60,
#             'spDefense': 50,
#             'speed': 65
#         },
#         'MoveList': {
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