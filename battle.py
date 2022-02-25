import pygame
from moveDatabase import moves

class Battle:
  def __init__(self, pokemon1, pokemon2):
    self.pokemon1 = pokemon1.data;
    self.pokemon2 = pokemon2.data;

  
  def go(self):
    attack = input('ATTACK > ')
      
    p1health = self.pokemon1.health;
    p1cp = self.pokemon1.cp; # add cp to pokemondata
    p1type = self.pokemon1.type;
    p1spCharge = 0
    
    p2health = self.pokemon2.health;
    p2cp = self.pokemon2.cp;
    p2type = self.pokemon2.type;
    p2spCharge = 0

    if attack == '':
      print('you did damage')
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