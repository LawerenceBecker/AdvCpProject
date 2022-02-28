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
            return self.data.combatPower
        elif whichStat == 'Attack':
            return self.data.attack
        elif whichStat == 'Defense':
            return self.data.defense

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
        self.maxHealth = pokemon[name]['baseStats']['maxHealth']
        self.health = self.maxHealth
        self.level = 4
        self.exp = 0
        self.totalExp = 0

        self.pokemonType = pokemon[name]['baseStats']['type']

        self.normalMove = Move('Fire', "Quick", 'Ember')
        
        self.attack = pokemon[name]['baseStats']['attack']
        self.defense = pokemon[name]['baseStats']['defense']

class Move():
    def __init__(self, type, typeMove, name):
        self.moveName = name
        self.moveType = type
        self.power = moves[typeMove][type][name]['Power']
