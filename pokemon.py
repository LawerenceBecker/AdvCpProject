import pygame
import random
import math
from moveDatabase import moves
from pokemonData import pokemon, cpMult, expTotal, expYield

class PygameData(pygame.sprite.Sprite):
    def __init__(self, name, level):
        super().__init__()
        self.inventorySprite = pygame.Surface((64,64))
        self.battleSprite = pygame.Surface((64,64))

        self.data = EntityData(name, level)
        self.positionIndex = 0

    def stats(self, whichStat):
        if whichStat == 'Health':
            return self.data.health
        elif whichStat == 'MaxHealth':
            return self.data.maxHealth
        elif whichStat == 'Type':
            return self.data.type
        elif whichStat == 'Attack':
            return self.data.attack
        elif whichStat == 'Defense':
            return self.data.defense
        elif whichStat == 'CP':
            return self.data.cp

    def heal(self, amount):
        self.data.health += amount
        if self.data.health >= self.data.maxHealth:
            self.data.health = self.data.maxHealth
        print(f'You healed {self.data.nickName} for {amount} points')
        print(f'{self.data.nickName}\'s HP: {self.data.health} / {self.data.maxHealth}')

class EntityData():
    def __init__(self, name, level):
        self.name = name
        self.nickName = name

        self.hpIV = random.randint(1,16)
        self.attackIV = random.randint(1,16)
        self.defenseIV = random.randint(1,16)

        self.level = level
        self.exp = expTotal[level]

        self.pokemonType = pokemon[name]['baseStats']['type']

        self.FireQuick = Move('Fire', "Quick", 'Ember')
        self.GrassQuick = Move('Grass', 'Quick', 'Vine Whip')
        self.NormalQuick = Move('Normal', 'Quick', 'Tackle')
        self.WaterQuick = Move('Water', 'Quick', 'Water Gun')

        self.FireSpecial = Special('Fire', 'Special', 'Fire Punch')
        self.GrassSpecial = Special('Grass', 'Special', 'Solar Beam')
        self.NormalSpecial =  Special('Normal', 'Special', 'Return')
        self.WaterSpecial = Special('Water', 'Special', 'Surf')
      
        self.maxHealth = self.statCalc(self.hpIV, 'hp')
        self.health = self.maxHealth
        
        self.attack = self.statCalc(self.attackIV, 'attack')
        self.defense = self.statCalc(self.defenseIV, 'defense')

        self.cp = self.cpCalc()

    def expNeeded(self):
        return expTotal[self.level+1], expTotal[self.level+1] - self.exp

    def gainExperience(self, pokemon2, a=1):
        return math.floor((a * expYield[pokemon2.data.name] * pokemon2.data.level) / 7)

    def checkLevelUp(self):
        if self.exp >= expTotal[self.level+1]:
            print(f'{self.nickName} gained a level')
            self.level += 1
            self.attack = self.statCalc(self.attackIV, 'attack')
            self.defence = self.statCalc(self.defenseIV, 'defense')
            self.maxHealth = self.statCalc(self.hpIV, 'hp')
            self.cp = self.cpCalc()
            
    def cpCalc(self):
        return math.ceil((math.sqrt(self.maxHealth) * self.attack * math.sqrt(self.defense))/10)
        
    def statCalc(self, iv, stat):
        return math.floor((pokemon[self.name]['baseStats'][stat] + iv) * cpMult[self.level])

class Move():
    def __init__(self, type, typeMove, name):
        self.moveName = name
        self.moveType = type
        self.power = moves[typeMove][type][name]['Power']
        self.cooldown = moves[typeMove][type][name]['Cooldown']
        self.fillMeter = moves[typeMove][type][name]['FillMeter']

class Special():
    def __init__(self, type, typeMove, name):
        self.moveName = name
        self.moveType = type
        self.power = moves[typeMove][type][name]['Power']
        self.meterSize = moves[typeMove][type][name]['MeterSize']
        self.bars = moves[typeMove][type][name]['Bars']