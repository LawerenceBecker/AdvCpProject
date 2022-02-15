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

class EntityData():
    def __init__(self, name):
        self.name = name
        self.pokemonType = pokemon[name]['StartStats']['pokemonType']
        self.maxHealth = pokemon[name]['StartStats']['maxHealth']
        self.health = self.maxHealth
        self.level = 14
        self.exp = 0
        self.totalExp = 0
        self.moves = []

        for lv in range(1, self.level+1):
            if pokemon[name]['MoveList'][lv]:
                if len(self.moves) == 4:
                    self.moves.pop(0)
                self.moves.append(Move(pokemon[name]['MoveList'][lv]))

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