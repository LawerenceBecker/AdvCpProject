import pygame
import pickle
from random import *

from pokemon import PygameData
from capture import *
from battle import Battle
from route import RouteLabel

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, objectSprites, routeAreas, uiSprites):
        super().__init__(groups)

        self.moveUp = pygame.image.load("Character/BoxUp.png").convert_alpha()
        self.moveDown = pygame.image.load("Character/BoxDown.png").convert_alpha()
        self.moveLeft = pygame.image.load("Character/BoxLeft.png").convert_alpha()
        self.moveRight = pygame.image.load("Character/BoxRight.png").convert_alpha()

        self.facing = 'UP'

        self.image = self.moveUp
        self.rect = self.image.get_rect(topleft = (x*64,y*64))

        self.prevTick = pygame.time.get_ticks()
        self.moveTimer = 200

        self.direction = pygame.math.Vector2()
        self.placement = 1
        self.interactingRL = False
        self.interactingAB = False
        self.moveCounter = 0
        self.encounterTimer = randint(10, 25)

        self.objectSprites = objectSprites
        self.uiSprites = uiSprites
        self.routeAreas = routeAreas
        self.currentRoute = None
        self.interactableSprite = None

        self.pokemonBag = []
        self.bag = {'Medicine': [], 'Pokeballs': []}
        self.money = 300

    def update(self):
        self.input()

        for route in self.routeAreas:
            if self.rect.colliderect(route.rect):
                if route.entered == False:
                    self.currentRoute = route
                    route.entered = True
                    RouteLabel(self.uiSprites, route.name)
                    
            else:
                route.entered = False

        self.rect.x += self.direction.x * 64
        self.collision("horizontal")

        self.rect.y += self.direction.y * 64
        self.collision("vertical")

        self.interactableSprite = None
        for sprite in self.objectSprites:
            if hasattr(sprite, 'job'):
                if sprite.hitbox.colliderect(self.rect):
                    if sprite.rect.x - self.rect.x <= -1 and sprite.rect.y - self.rect.y <= -1: pass
                    elif sprite.rect.x - self.rect.x >= 1 and sprite.rect.y - self.rect.y >= 1: pass
                    elif sprite.rect.x - self.rect.x <= -1 and sprite.rect.y - self.rect.y >= 1: pass
                    elif sprite.rect.x - self.rect.x >= 1 and sprite.rect.y - self.rect.y <= -1: pass
                    elif sprite.rect.x - self.rect.x <= -1 and self.facing == "LEFT": self.interactableSprite = sprite
                    elif sprite.rect.x - self.rect.x >= 1 and self.facing == "RIGHT": self.interactableSprite = sprite
                    elif sprite.rect.y - self.rect.y <= -1 and self.facing == "UP": self.interactableSprite = sprite
                    elif sprite.rect.y - self.rect.y >= 1 and self.facing == "DOWN": self.interactableSprite = sprite
                if sprite.job == 'trainer':
                    if sprite.facing == 'left':
                        if sprite.rect.y == self.rect.y and self.rect.x >= sprite.rect.x - (5*64) and self.rect.x <= sprite.rect.x:
                            if sprite.active == True:
                                Battle(self, sprite.npcPokeBag[1:], sprite.npcPokeBag[0])
                                sprite.active = False
                    if sprite.facing == 'right':
                        if sprite.rect.y == self.rect.y and self.rect.x <= sprite.rect.x + (5*64) and self.rect.x >= sprite.rect.x:
                            if sprite.active == True:
                                Battle(self, sprite.npcPokeBag[1:], sprite.npcPokeBag[0])
                                sprite.active = False
                                
                    if sprite.facing == 'up':
                        if sprite.rect.x == self.rect.x and self.rect.y >= sprite.rect.y - (5*64) and self.rect.y <= sprite.rect.y:
                            if sprite.active == True:
                                Battle(self, sprite.npcPokeBag[1:], sprite.npcPokeBag[0])
                                sprite.active = False
                                
                    if sprite.facing == 'down':
                        if sprite.rect.x == self.rect.x and self.rect.y <= sprite.rect.y + (5*64) and self.rect.y >= sprite.rect.y:
                            if sprite.active == True:
                                Battle(self, sprite.npcPokeBag[1:], sprite.npcPokeBag[0])
                                sprite.active = False
                                
                        
            if hasattr(sprite, 'item'):
                if sprite.hitbox.colliderect(self.rect):
                    self.interactableSprite = sprite

    def remove_item(self, itemObj):
        for pocket in self.bag:
            if pocket == itemObj.pocket:
                for index, item in enumerate(self.bag[pocket]):
                    if item[0] == itemObj:
                        item[1] -= 1
                        if item[1] == 0:
                            self.bag[pocket].pop(index)
                            
    def add_item(self, itemObj, amount):
        for pocket in self.bag:
            if pocket == itemObj.pocket:
                for item in self.bag[pocket]:
                    if item[0].name == itemObj.name:
                        item[1] += amount
                        return
                self.bag[pocket].append([itemObj, amount])

    def add_pokemon(self, pokemon, nickName):
        if len(self.pokemonBag) < 6:
            pokemon.data.nickName = nickName
            self.pokemonBag.append(pokemon)
        else:
            print('\nYou have too many pokemon, so you let this one go')

    def collision(self, direction):                        

        
        
        if direction == "horizontal":
            for sprite in self.objectSprites:
                if sprite.rect.colliderect(self.rect):
                    if sprite.tileType == '':

                        
                        if self.direction.x > 0:
                            self.rect.right = sprite.rect.left
                            self.interactingRL = False
                            # print(f"wall to the right of me {self.interactingRL}")
                            
                        if self.direction.x < 0:
                            self.rect.left = sprite.rect.right
                            self.interactingRL = False
                            # print(f"wall to the left of me {self.interactingRL}")

                    elif sprite.tileType == 'grass':

                        if self.interactingRL == True:
                            self.interactingRL = False
                            self.moveCounter += 1

                            if self.moveCounter == self.encounterTimer:
                                self.encounterTimer = random.randint(10, 25)
                                self.moveCounter = 0
                                randomPoke = choice(self.currentRoute.pokemonTable)
                                Battle(self, PygameData(randomPoke[0], randomPoke[1]))
                        
                        

        if direction == "vertical":
            for sprite in self.objectSprites:
                if sprite.rect.colliderect(self.rect):
                    if sprite.tileType == '':

                        if self.direction.y > 0:
                            self.rect.bottom = sprite.rect.top
                            self.interactingAB = False
                            # print(f"wall below me {self.interactingAB}")
                            
                        if self.direction.y < 0:
                            self.rect.top = sprite.rect.bottom
                            self.interactingAB = False
                            # print(f"wall above me {self.interactingAB}")

                    elif sprite.tileType == 'grass':

                        if self.interactingAB == True:
                            self.interactingAB = False
                            self.moveCounter += 1

                            if self.moveCounter == self.encounterTimer:
                                self.encounterTimer = random.randint(10, 25)
                                self.moveCounter = 0
                                randomPoke = choice(self.currentRoute.pokemonTable)
                                Battle(self, PygameData(randomPoke[0], randomPoke[1]))
                        
            if hasattr(sprite, 'item'):
                if sprite.hitbox.colliderect(self.rect):
                    self.interactableSprite = sprite
    
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_x]:
            self.moveTimer = 100
        else: 
            self.moveTimer = 200

        self.direction = pygame.math.Vector2()

        if pygame.time.get_ticks() - self.prevTick >= self.moveTimer:
            if keys[pygame.K_BACKSPACE]:
                print('\nSaving... \n...')
                self.save_char()
                print('Done Saving')
                self.prevTick = pygame.time.get_ticks()

            elif keys[pygame.K_TAB]:
                while True:
                    print('\n1. Pokemon \n2. Bag \n3. End')
                    choice = int(input('> '))
                    if choice == 3:
                        return
                    elif choice == 1:
                        if self.pokemonBag != None:
                            for index, pokemon in enumerate(self.pokemonBag):
                                print(f'{index+1}. {pokemon.data.nickName}')
                            print(f'{index+2}. End')

                            choice = int(input('> '))
                            
                            for index, pokemon in enumerate(self.pokemonBag):
                                if choice == index+1:
                                    print(f'Health: {pokemon.stats("Health")} / {pokemon.stats("MaxHealth")} \nCP: {pokemon.stats("CP")}')
                                    break
                            
                            self.prevTick = pygame.time.get_ticks()
                            return
                        else:
                            print('You have no pokemon')
                    elif choice == 2:
                        for index, pocket in enumerate(self.bag):
                            print(f'{index+1}. {pocket}')
                        print(f'{index+2}. End')
                        choice = int(input('> '))
                        
                        if choice == index+2:
                            return
                        for index, pocket in enumerate(self.bag):
                            if choice == index+1:
                                des = pocket  
                        
                        if len(self.bag[des]) != 0 and des != None:
                            print(f'\n{des}:')
                            for index, item in enumerate(self.bag[des]):
                                print(f'{index+1}. {item[0].name} x{item[1]}')
                            print(f'{index+2}. End')
                            
                            choice = int(input('> '))

                            if choice == index+2:
                                return
                            
                            for index, item in enumerate(self.bag[des]):
                                if index+1 == choice:
                                    item[0].find_use(self)
                                    return
                        else:
                            print('You have no items in that pocket')

            elif keys[pygame.K_ESCAPE]:
                print('Reset(Debug)')
                self.rect.topleft = (6*64,6*64)
                self.save_char()
                self.pokemonBag = []
                self.prevTick = pygame.time.get_ticks()

            elif keys[pygame.K_DELETE]:
                print('\nLoading... \n...')
                self.load_char()
                print('Done Loading')
                self.prevTick = pygame.time.get_ticks()

            if keys[pygame.K_z]:
                if self.interactableSprite:
                    if hasattr(self.interactableSprite, 'job'):
                        if self.interactableSprite.job == 'shop':
                            self.interactableSprite.shop(self)
                        elif self.interactableSprite.job == 'pokecenter':
                            self.interactableSprite.pokeCenter(self)
                        elif self.interactableSprite.job == 'person':
                            self.interactableSprite.person(self)
                    if hasattr(self.interactableSprite, 'item'):
                        print(f'\nYou found a {self.interactableSprite.item.name}')
                        self.add_item(self.interactableSprite.item, 1)
                        self.interactableSprite.kill()
                        
                    self.prevTick = pygame.time.get_ticks()
            
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self.direction.y = -1
                self.image = self.moveUp
                self.prevTick = pygame.time.get_ticks()
                self.facing = 'UP'
                self.interactingAB = True

            elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.image = self.moveDown
                self.prevTick = pygame.time.get_ticks()
                self.facing = 'DOWN'
                self.interactingAB = True
                
            elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.image = self.moveLeft
                self.prevTick = pygame.time.get_ticks()
                self.facing = 'LEFT'
                self.interactingRL = True

            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.image = self.moveRight
                self.prevTick = pygame.time.get_ticks()
                self.facing = 'RIGHT'
                self.interactingRL = True

    def get_data(self):
        tempBag = []
        for pokemon in self.pokemonBag:
            tempBag.append(pokemon.data)
        return self.rect.x, self.rect.y, tempBag

    def save_char(self):
        with open("Data/CharData.plk", "wb") as charData:
            pickle.dump(self.get_data(), charData, -1)

    def load_char(self):
        tempBag = []
        with open('Data/CharData.plk', 'rb') as charData:
            self.rect.x, self.rect.y, tempBag = pickle.load(charData)
        
        for tempPoke in tempBag:
            tempPokeData = PygameData(tempPoke.name, tempPoke.level)
            tempPokeData.data = tempPoke
            self.pokemonBag.append(tempPokeData)
