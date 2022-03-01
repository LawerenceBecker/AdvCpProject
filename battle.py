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

from pokemon import PygameData
from capture import *

class Battle:
  def __init__(self, player, pokemon1, pokemon2):
    self.pokemon1 = pokemon1
    self.pokemon2 = pokemon2
    self.player = player
    self.playerTicks = pygame.time.get_ticks()
    self.cpuTicks = pygame.time.get_ticks()

    self.go()

  def damage(self, move, dealingPokemon, takingPokemon, trainer=1):

      if move.moveType == dealingPokemon.data.pokemonType: stab = 1.2
      else: stab = 1

      modifier = effective(dealingPokemon.data.pokemonType, takingPokemon.data.pokemonType)[1] * stab * trainer

      damage = math.floor((0.5 * move.power * (dealingPokemon.stats('Attack') / takingPokemon.stats('Defense'))) * modifier + 1 )

      print(damage)

      return damage
    
  def go(self):
      
    battle = True
    print("BATTLE (z to attack)")
    
    while battle:
          
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z and pygame.time.get_ticks() - self.playerTicks >= self.pokemon1.data.normalMove.cooldown:
              
                self.playerTicks = pygame.time.get_ticks()
              
                print('you did damage')
                  
              
                damage = self.damage(self.pokemon1.data.normalMove, self.pokemon1, self.pokemon2)
                self.pokemon2.data.health -= damage

            
            # should open menu here
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_x:
              run = input("Would you like to run away? >> ")
              if run == 'y' or run == 'yes':
                print("You ran away successfully")
                battle = False
              else:
                print("You didn't run away")
                break

        

      
        if self.pokemon2.data.health <= 0:
            self.pokemon2.data.health = 0
            print('You won')
            capture(self.player, self.pokemon2)
            battle = False
        elif self.pokemon1.data.health <= 0:
          self.pokemon1.data.health = 0
          print('You lose')

        if pygame.time.get_ticks() - self.cpuTicks >= self.pokemon2.data.normalMove.cooldown:
          self.cpuTicks = pygame.time.get_ticks()
              
          print('cpu did damage')
                  
              
          damage = self.damage(self.pokemon2.data.normalMove, self.pokemon2, self.pokemon1)
          
          self.pokemon1.data.health -= damage
          print(f'\nEnemy\'s Health: {self.pokemon2.data.health} / {self.pokemon2.data.maxHealth}')
          print(f'Your Health: {self.pokemon1.data.health} / {self.pokemon1.data.maxHealth}')
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