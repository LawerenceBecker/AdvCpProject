# This website provides information for all available pokemon go moves:
# https://gamepress.gg/pokemongo/pokemon-move/ember

# (FillMeter is the Energy Delta stat)
# fill meter should equal 10 energy per second for most moves (EPS is not the same as Energy Delta)


# For how much each special move needs to be charged, it's based on it's Charge Energy column
# 3 means it needs 33 energy, 2 means it needs 50, 1 means 100
## the more energy it needs the more damage it does

## found here: https://pokemongohub.net/post/meta/multi-bar-vs-single-bar-charged-moves/

moves = {'Quick': {
          'Fire': {
            'Ember': { 
              'Power': 10,
              'Cooldown': 1000,
              'FillMeter': 10}
          },
          'Grass': {
            'Vine Whip': {
              'Power': 7,
              'Cooldown': 600,
              'FillMeter': 6}
          },
          'Water': {
            'Water Gun': {
              'Power': 5,
              'Cooldown': 500,
              'FillMeter': 5}
          },
          'Normal': {
            'Tackle': {
              'Power': 5,
              'Cooldown': 500,
              'FillMeter': 5}
          },
          'Dragon': {
            'Dragon Tail': {
              'Power': 13,
              'Cooldown': 1100,
              'FillMeter': 9}
          },
          'Psychic': {
            'Confusion': {
              'Power': 20,
              'Cooldown': 1600,
              'FillMeter': 15}
          },
          'Electric': {
            'Spark': {
              'Power': 6,
              'Cooldown': 700,
              'FillMeter': 9}
          }
},
         
        'Special': {
         'Fire': {
           'Fire Punch': {
             'Power': 55,
             'Bars': 3,
             'MeterSize': 33}
         },
         'Grass': {
           'Solar Beam': {
             'Power': 180,
             'Bars': 1,
             'MeterSize': 100}
         },
         'Water': {
           'Surf': {
             'Power': 65,
             'Bars': 2,
             'MeterSize': 50}
         },
         'Normal': {
           'Return': {
             'Power': 35,
             'Bars': 3,
             'MeterSize': 33}
         },
         'Dragon': {
           'Dragon Claw': {
             'Power': 50,
             'Bars': 3,
             'MeterSize': 33}
         },
         'Psychic': {
           'Psybeam': {
             'Power': 70,
             'Bars': 2,
             'MeterSize': 50}
         },
         'Electric': {
           'Discharge': {
             'Power': 65,
             'Bars': 3,
             'MeterSize': 33}
         }
        }
      }