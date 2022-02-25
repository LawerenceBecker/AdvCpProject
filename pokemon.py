import pygame
from moveDatabase import moves
from pokemonData import pokemon

class PygameData(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.inventorySprite = pygame.Surface((64,64))
        self.battleSprite = pygame.Surface((64,64))

        self.data = EntityData(name)
        self.positionIndex = 0

    def stats(self, whichStat):
        if whichStat == 'Health':
            return self.data.health
        elif whichStat == 'MaxHealth':
            return self.data.maxHealth
        elif whichStat == 'Type':
            return self.data.type
        elif whichStat == 'CP':
            return self.data.cp
        elif whichStat == 'Level':
            return self.data.level
        elif whichStat == 'Attack':
            return self.data.attack
        elif whichStat == 'Defense':
            return self.data.defense
        elif whichStat == 'spAttak':
            return self.data.spAttack
        elif whichStat == 'spDefense':
            return self.data.spDefense
        elif whichStat == 'Speed':
            return self.data.speed

    def heal(self, amount):
        self.data.health += amount
        if self.data.health >= self.data.maxHealth:
            self.data.health = self.data.maxHealth
        print(f'You healed {self.data.name} for {amount} points')
        print(f'{self.data.name}\'s hp: {self.data.health}')

class EntityData():
    def __init__(self, name):
        self.name = name
        self.nickName = name
        self.maxHealth = pokemon[name]['StartStats']['maxHealth']
        self.health = self.maxHealth
        self.level = 4
        self.exp = 0
        self.totalExp = 0

        self.cp = pokemon[name]['CP']
        self.type = pokemon[name]['Type']
        
        self.attack = pokemon[name]['StartStats']['attack']
        self.defense = pokemon[name]['StartStats']['defense']
        self.spAttack = pokemon[name]['StartStats']['spAttack']
        self.spDefense = pokemon[name]['StartStats']['spDefense']
        self.speed = pokemon[name]['StartStats']['speed']

class Move():
    def __init__(self, name):
        self.moveName = name
        self.moveType = moves[name]['moveType']
        self.power = moves[name]['power']
        self.accuracy = moves[name]['accuracy']
        
        self.maxPP = moves[name]['maxPP']
        self.currentPP = self.maxPP