# pokemon go damage mechanics  
# https://gamepress.gg/pokemongo/damage-mechanics

# Current damage calculation
# https://bulbapedia.bulbagarden.net/wiki/Damage

# pokemon go CP mechanics 
# https://gamepress.gg/pokemongo/pokemon-stats-advanced#ivs

# CP multiplier
# https://gamepress.gg/pokemongo/cp-multiplier

import pygame
import math
from moveDatabase import moves
from moveEffectiveness import effective

class Battle:
  def __init__(self, pokemon1, pokemon2):
    self.pokemon1 = pokemon1
    self.pokemon2 = pokemon2

    self.go()

  def damage(self, move, dealingPokemon, takingPokemon, trainer=1):

      if move.moveType == dealingPokemon.data.pokemonType: stab = 1.2
      else: stab = 1

      modifier = effective(dealingPokemon.data.pokemonType, takingPokemon.data.pokemonType)[1] * stab * trainer

      damage = math.floor((0.5 * move.power * (dealingPokemon.stats('Attack') / takingPokemon.stats('Defense'))) * modifier + 1 )

      print(damage)

      return damage
    
  def go(self):

    while True:

        if self.pokemon2.data.health <= 0:
            print('You won')
            break
        print(f'\nEnemy\'s Health: {self.pokemon2.data.health} / {self.pokemon2.data.maxHealth}')
        print(f'Your Health: {self.pokemon1.data.health} / {self.pokemon1.data.maxHealth}')
            
        attack = input('\nATTACK > ')
    
        if attack == '':
          print('you did damage')
          damage = self.damage(self.pokemon1.data.normalMove, self.pokemon1, self.pokemon2)
          self.pokemon2.data.health -= damage
        else:
          print('no damage for you :)')


# Things we need:

# Pokemon Stats:
# - CP (Combat Power)
# - Type
# - Moves (normal and special)
# -- Damage 
# -- Type
 
# Battle system:
# - Continous attacking
# - Move delay  (based on damage)
# - Special meter charging  (based on speed/move delay)
# - Type advantages 
# - Bag accessible at anytime 
# - Differentiate wild encounters and trainer battles