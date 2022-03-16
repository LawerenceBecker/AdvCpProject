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
  def __init__(self, player, pokemon2, trainerInfo=None):
    for pokemon in player.pokemonBag:
      if pokemon.data.health >= 1:   
        self.pokemon1 = pokemon
        break
    if trainerInfo:
        self.trainerName = trainerInfo
        self.trainerPokemon = pokemon2
        self.pokemon2 = self.trainerPokemon[0]
    else:
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
    if hasattr(self, 'trainerName'):
        trainerBattle = True
        print(f"\n{self.trainerName} has challenged you!")

        print(f'They sent out {self.pokemon2.data.name}!')

        input()
    else: trainerBattle = False
    print(f'\nGo {self.pokemon1.data.nickName}!')
    input()

    print("BATTLE (z to attack)")

    
    
    while battle:
      
        event_list = pygame.event.get()
        for event in event_list:
            poke1quick = eval(f'self.pokemon1.data.{self.pokemon1.data.pokemonType}Quick')
            poke2quick = eval(f'self.pokemon2.data.{self.pokemon2.data.pokemonType}Quick')
    
            poke1special = eval(f'self.pokemon1.data.{self.pokemon1.data.pokemonType}Special')
            poke2special = eval(f'self.pokemon2.data.{self.pokemon2.data.pokemonType}Special')
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z and pygame.time.get_ticks() - self.playerTicks >= poke1quick.cooldown:
              
                self.playerTicks = pygame.time.get_ticks()
              
                print('you did damage')

              
                if trainerBattle:
                    damage = self.damage(poke1quick, self.pokemon1, self.pokemon2, 1.3)
                else:
                    damage = self.damage(poke1quick, self.pokemon1, self.pokemon2)
                self.pokemon2.data.health -= damage

                if self.playerChargeMeter + poke1quick.fillMeter > poke1special.meterSize:
                  self.playerChargeMeter = poke1special.meterSize
                else: 
                  self.playerChargeMeter += poke1quick.fillMeter

                print(f"Meter charge: {self.playerChargeMeter}")

              
                if self.pokemon2.data.health <= 0:
                  self.pokemon2.data.health = 0
                  if trainerBattle:
                      print(f'{self.pokemon1.data.nickName} gained {self.pokemon1.data.gainExperience(self.pokemon2, 1.5)} experience points')
                      self.pokemon1.data.exp += self.pokemon1.data.gainExperience(self.pokemon2)
                      self.pokemon1.data.checkLevelUp()
                      for pokemon in self.trainerPokemon:
                          if pokemon.data.health >= 1:
                              win = False
                              print(f'\n{self.pokemon2.data.name} fainted!')
                              print(f'\n{self.trainerName} sends out {pokemon.data.name}')
                              self.pokemon2 = pokemon
                              self.cpuTicks = pygame.time.get_ticks()
                              self.cpuChargeMeter = 0
                              input()
                          else:
                              win = True
                      if win:
                          print('You Won')
                          battle=False
                  else:
                    print(f'{self.pokemon1.data.nickName} gained {self.pokemon1.data.gainExperience(self.pokemon2)} experience points')
                    self.pokemon1.data.exp += self.pokemon1.data.gainExperience(self.pokemon2)
                    self.pokemon1.data.checkLevelUp()
                    
                    print('You won')
                    battle = False


                  
              
            # should open menu here
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_x:
              choice = input("\n\nWhat would you like to do? \n1. Pokemon \n2. Bag \n3. Run \n4. Go Back \n> ")

              if choice == '1':
                  print('\n')
                  for index, pokemon in enumerate(self.player.pokemonBag):
                    print(f'{index+1}. {pokemon.data.nickName} {pokemon.data.health} / {pokemon.data.maxHealth}')
                  print(f'{index+2}. Return')
                  choice = input('> ')
                  if choice == str(index+2):
                    pass
                  for index, pokemon in enumerate(self.player.pokemonBag):
                    if choice == str(index+1):
                      if pokemon.data.health >= 1:
                        print(f'\nCome back {self.pokemon1.data.nickName}!')

                        print(f'\nGo {pokemon.data.nickName}!')

                        self.pokemon1 = pokemon

                        input()
                        break
                      else:
                        print('You can\'t use that pokemon')

              elif choice == '2':
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

          if trainerBattle:
          
              damage = self.damage(poke2quick, self.pokemon2, self.pokemon1, 1.3)
          else:
              damage = self.damage(poke2quick, self.pokemon2, self.pokemon1)

          self.pokemon1.data.health -= damage

          if self.cpuChargeMeter + poke2quick.fillMeter > poke2special.meterSize:
            self.cpuChargeMeter = poke2special.meterSize
          else: 
            self.cpuChargeMeter += poke2quick.fillMeter

          
          if self.pokemon1.data.health <= 0:
            self.pokemon1.data.health = 0

            print(f'{self.pokemon1.data.name} fainted!')
            input()

            for pokemon in self.player.pokemonBag:
              if pokemon.data.health >= 1:
                lose = False

                print('\n')
                for index, pokemon in enumerate(self.player.pokemonBag):
                  print(f'{index+1}. {pokemon.data.nickName} {pokemon.data.health} / {pokemon.data.maxHealth}')
                choice = input('> ')
                for index, pokemon in enumerate(self.player.pokemonBag):
                  if choice == str(index+1):
                    if pokemon.data.health >= 1:
                      print(f'\nGo {pokemon.data.nickName}!')

                      self.pokemon1 = pokemon

                      input()
                      break
                    else:
                      print('You can\'t use that pokemon')
              else: lose = True
                  
            if lose == True:
              print('All your pokemon have fainted!')
              return

          
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