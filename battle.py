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
    self.cpuChargeMeter = 0
    self.playerChargeMeter = 0
    
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

        poke1quick = eval(f'self.pokemon1.data.{self.pokemon1.data.pokemonType}Quick')
        poke2quick = eval(f'self.pokemon2.data.{self.pokemon2.data.pokemonType}Quick')

        poke1special = eval(f'self.pokemon1.data.{self.pokemon1.data.pokemonType}Special')
        poke2special = eval(f'self.pokemon2.data.{self.pokemon2.data.pokemonType}Special')



      
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z and pygame.time.get_ticks() - self.playerTicks >= poke1quick.cooldown:
              
                self.playerTicks = pygame.time.get_ticks()
              
                print('you did damage')

              
                
                damage = self.damage(poke1quick, self.pokemon1, self.pokemon2)
                self.pokemon2.data.health -= damage

                if self.playerChargeMeter + poke1quick.fillMeter > poke1special.meterSize:
                  self.playerChargeMeter = poke1special.meterSize
                else: 
                  self.playerChargeMeter += poke1quick.fillMeter

                print(f"Meter charge: {self.playerChargeMeter}")

              
                if self.pokemon2.data.health <= 0:
                  self.pokemon2.data.health = 0
                  print('You won')
                  battle = False


                  
              
            # should open menu here
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_x:
              choice = input("\n\nWhat would you like to do? \n1. Pokemon \n2. Bag \n3. Run \n4. Go Back \n> ")
              if choice == '2':
                  choice = input('\n1. Items \n2. Pokeballs \n> ')
                  if choice == '1':
                    pass
                  elif choice == '2':
                    bagLen = len(self.player.pokemonBag)
                    capture(self.player, self.pokemon2)
                    if len(self.player.pokemonBag) > bagLen:
                        return

        if pygame.time.get_ticks() - self.cpuTicks >= poke2quick.cooldown:
          
          self.cpuTicks = pygame.time.get_ticks()

          print('cpu did damage')
              
          damage = self.damage(poke2quick, self.pokemon2, self.pokemon1)

          self.pokemon1.data.health -= damage

          if self.cpuChargeMeter + poke2quick.fillMeter > poke2special.meterSize:
            self.cpuChargeMeter = poke2special.meterSize
          else: 
            self.cpuChargeMeter += poke2quick.fillMeter

          
          if self.pokemon1.data.health <= 0:
            self.pokemon1.data.health = 0
            print('You lose')
          
          print(f"Cpu charge: {self.cpuChargeMeter}")

          print(self.pokemon2.data.name)
          
          # self.pokemon1.data.health -= damage
          # print(f'\nEnemy\'s Health: {self.pokemon2.data.health} / {self.pokemon2.data.maxHealth}')
          # print(f'Your Health: {self.pokemon1.data.health} / {self.pokemon1.data.maxHealth}')



# To-do: 

# usable special attack
# basic UI for health and special meter
# differentiate wild encounters and trainer battles
# random pokemon each wild encounter
# being able to switch out pokemon mid battle