import pygame
import pickle
import sys
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
        self.money = 30000000

        self.active = True

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

            if keys[pygame.K_TAB]:
                self.prevTick = pygame.time.get_ticks()
                for elem in self.uiSprites:
                    if isinstance(elem, Menu) and elem.job == 'Inv':
                        elem.kill()
                        for elem in self.uiSprites:
                            if isinstance(elem, Options)and elem.job == 'InvOpt':
                                elem.kill()
                        self.active = True
                        return
                Menu(self.uiSprites, self, 'Inv')
                self.active = False

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
                        elif self.interactableSprite.job == 'trainer' and self.interactableSprite.active == True:
                            Battle(self, self.interactableSprite.npcPokeBag[1:], self.interactableSprite.npcPokeBag[0])
                            self.interactableSprite.active = False
                    if hasattr(self.interactableSprite, 'item'):
                        print(f'\nYou found a {self.interactableSprite.item.name}')
                        self.add_item(self.interactableSprite.item, 1)
                        self.interactableSprite.kill()
                        
                    self.prevTick = pygame.time.get_ticks()
            
            if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.active == True:
                self.direction.y = -1
                self.image = self.moveUp
                self.prevTick = pygame.time.get_ticks()
                self.facing = 'UP'
                self.interactingAB = True

            elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.active == True:
                self.direction.y = 1
                self.image = self.moveDown
                self.prevTick = pygame.time.get_ticks()
                self.facing = 'DOWN'
                self.interactingAB = True
                
            elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.active == True:
                self.direction.x = -1
                self.image = self.moveLeft
                self.prevTick = pygame.time.get_ticks()
                self.facing = 'LEFT'
                self.interactingRL = True

            elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.active == True:
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

class Menu(pygame.sprite.Sprite):
    def __init__(self, group, player, job):
        super().__init__(group)

        self.player = player
        self.job = job

        self.font = pygame.font.Font("Data/DisposableDroidBB.ttf", 24)

        if job == 'Inv':
            self.image = pygame.Surface((200, 260))
            self.image.fill('light grey')
            self.rect = self.image.get_rect(topleft= (pygame.display.get_surface().get_width()-200,150))
            Options(group, 'Pokemon', self.rect.x+20, self.rect.y+20, self.player, 'InvOpt')
            Options(group, 'Bag', self.rect.x+20, self.rect.y+80, self.player, 'InvOpt')
            Options(group, 'Save', self.rect.x+20, self.rect.y+140, self.player, 'InvOpt')
            Options(group, 'End', self.rect.x+20, self.rect.y+200, self.player, 'InvOpt')
            
        elif job == 'ExitComf':
            self.image = pygame.Surface((200, 100))
            self.image.fill('light grey')
            self.rect = self.image.get_rect(topleft= ((pygame.display.get_surface().get_width()/2)-100,(pygame.display.get_surface().get_height()/2)-100))

            text = self.font.render('Are you sure?', True, (0,0,0))
            self.image.blit(text, [100-(text.get_width()/2), 10])

            Options(group, 'Yes', self.rect.x+32, self.rect.y+45, self.player, 'ExitOpt')
            Options(group, 'No', self.rect.x+107, self.rect.y+45, self.player, 'ExitOpt')
            
        elif job == 'PokeInfo':
            self.image = pygame.Surface((200, 180))
            self.image.fill('dark grey')
            self.rect = self.image.get_rect(topleft= (pygame.display.get_surface().get_width()-200,pygame.display.get_surface().get_height()-200))
            
            Options(group, 'Summary', self.rect.x+20, self.rect.y+20, self.player, 'InfoOpt')
            Options(group, 'Swap', self.rect.x+20, self.rect.y+70, self.player, 'InfoOpt')
            Options(group, 'Cancel', self.rect.x+20, self.rect.y+120, self.player, 'InfoOpt')
            

class Options(pygame.sprite.Sprite):
    def __init__(self, group, text,x, y, player, job):
        super().__init__(group)

        self.player = player
        self.group = group
        self.job = job
        self.active = True

        self.text = text
        self.font = pygame.font.Font("Data/DisposableDroidBB.ttf", 24)
    
        if job == 'InvOpt':
            self.image = pygame.Surface((160, 40))
            self.rect = self.image.get_rect(topleft = (x, y))
            
            self.text_surface = self.font.render(self.text, True, (155,155,155))
            self.image.blit(self.text_surface, [10,10])
        elif job == 'ExitOpt':
            self.image = pygame.Surface((60, 40))
            self.rect = self.image.get_rect(topleft = (x, y))
            
            self.text_surface = self.font.render(self.text, True, (155,155,155))
            self.image.blit(self.text_surface, [0,0])
        elif job == 'InfoOpt':
            self.image = pygame.Surface((160, 40))
            self.rect = self.image.get_rect(topleft = (x, y))
            
            self.text_surface = self.font.render(self.text, True, (155,155,155))
            self.image.blit(self.text_surface, [10,10])

    def update(self):

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image.fill('grey')
            color = (255,255,255)
        else:
            self.image.fill('black')
            color = (155,155,155)
        
        self.text_surface = self.font.render(self.text, True, color)
        self.image.blit(self.text_surface, [10,10])
        

    def on_click(self):
        if self.job == 'InvOpt':
            if self.text == 'Pokemon':
                for elem in self.group:
                    if hasattr(elem, 'job') and elem.job == 'InvOpt':
                        elem.active = False
                PokemonIndetifier(self.group, self.player)
                
            elif self.text == 'Bag':
                for index, pocket in enumerate(self.player.bag):
                    print(f'{index+1}. {pocket}')
                print(f'{index+2}. End')
                choice = int(input('> '))
                
                if choice == index+2:
                    return
                for index, pocket in enumerate(self.player.bag):
                    if choice == index+1:
                        des = pocket  
                
                if len(self.player.bag[des]) != 0 and des != None:
                    print(f'\n{des}:')
                    for index, item in enumerate(self.player.bag[des]):
                        print(f'{index+1}. {item[0].name} x{item[1]}')
                    print(f'{index+2}. End')
                    
                    choice = int(input('> '))
    
                    if choice == index+2:
                        return
                    
                    for index, item in enumerate(self.player.bag[des]):
                        if index+1 == choice:
                            item[0].find_use(self)
                            return
                else:
                    print('You have no items in that pocket')
                
            elif self.text == 'Save':
                print('\nSaving... \n...')
                self.player.save_char()
                print('Done Saving')
    
            elif self.text == 'End':
                Menu(self.group, self.job, 'ExitComf')

        elif self.job == 'ExitOpt':
            if self.text == 'Yes':
                pygame.QUIT
                sys.exit()
            elif self.text == 'No':
                for elem in self.group:
                    if isinstance(elem, Menu) and elem.job == 'ExitComf':
                        elem.kill()
                    if isinstance(elem, Options) and elem.job == 'ExitOpt':
                        elem.kill()

        elif self.job == 'InfoOpt':
            if self.text == 'Cancel':
                for elem in self.group:
                    if hasattr(elem, 'switchie'):
                        elem.switchie = False
                for elem in self.group:
                    if hasattr(elem, 'inUse'): 
                        elem.inUse = False
                        elem.active = True
    
                    elif isinstance(elem, Menu) and elem.job == 'PokeInfo': elem.kill()
                    elif isinstance(elem, Options) and elem.job == 'InfoOpt': elem.kill()

            elif self.text == 'Summary':
                for elem in self.group:
                    if hasattr(elem, 'switchie'):
                        elem.switchie = False
                for elem in self.group:
                    if hasattr(elem, 'inUse'): 
                        elem.inUse = False
                        elem.active = True
    
                    elif isinstance(elem, Menu) and elem.job == 'PokeInfo': elem.kill()
                    elif isinstance(elem, Options) and elem.job == 'InfoOpt': elem.kill()

                print(f'Health: {self.player.stats("Health")} / {self.player.stats("MaxHealth")} \nLevel: {self.player.data.level} \nCP: {self.player.stats("CP")} \nEXP: {self.player.data.exp} / {self.player.data.expNeeded()[0]}: {self.player.data.expNeeded()[1]} needed')

            elif self.text == 'Swap':
                for elem in self.group:
                    if hasattr(elem, 'switchie'):
                        elem.switchie = False
                for elem in self.group:
                    if hasattr(elem, 'inUse') and elem.inUse == True:
                        elem.switchie = True
                        elem.inUse = False
                    if isinstance(elem, PokemonOptions):
                        elem.active = True

class PokemonIndetifier(pygame.sprite.Sprite):
    def __init__(self, group, player):
        super().__init__(group)

        self.image = pygame.Surface(pygame.display.get_window_size())
        self.image.fill('light grey')
        self.rect = self.image.get_rect(topleft = (0,0))

        self.player =player

        self.font = pygame.font.Font("Data/DisposableDroidBB.ttf", 96)
        self.text_surface = self.font.render('Pokemon', True, (255,255,255))
        self.image.blit(self.text_surface, [30,10])

        for index, poke in enumerate(self.player.pokemonBag):
            PokemonOptions(group, self, poke, index, self.player)

        CloseButton(group, self)


class PokemonOptions(pygame.sprite.Sprite):
    def __init__(self, group, parent, pokemon, posIndex, player):
        super().__init__(group)

        self.image = pygame.Surface((1200,96))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft= (40, 120+(120*posIndex)))
        self.posIndex = posIndex
        self.parent = parent
        self.group = group
        self.inUse = False
        self.active = True
        self.switchie = False
        self.player = player
        
        self.pokemon = pokemon
        self.font = pygame.font.Font("Data/DisposableDroidBB.ttf", 64)
        self.smallFont = pygame.font.Font("Data/DisposableDroidBB.ttf", 48)

        self.pokemonImage = pokemon.inventorySprite
        self.pokemonName = self.font.render(self.pokemon.data.nickName, True, (0,0,0))
        self.pokemonLevel = self.smallFont.render('lv. ' + str(self.pokemon.data.level), True, (0,0,0))
        self.pokemonCP = self.smallFont.render(('CP '+str(self.pokemon.data.cp)), True, (0,0,0))
        
        LevelBar(group, self.pokemon, self.rect.x+132+self.pokemonName.get_width(), self.rect.y+72)

        self.fillPokeData()
    
    def fillPokeData(self):

        self.image.blit(self.pokemonImage, [16,16])
        self.image.blit(self.pokemonName, [104,16])
        self.image.blit(self.pokemonLevel, [132+self.pokemonName.get_width() ,16])
        self.image.blit(self.pokemonCP, [1180-self.pokemonCP.get_width() ,24])
        

    def update(self):
        for elem in self.group:
            if hasattr(elem, 'inUse') and elem.inUse == True:
                return
        if self.switchie == True:
            self.image.fill('light blue')
        elif self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image.fill('dark grey')
        elif self.inUse == True:
            self.image.fill('dark grey')
        else:
            self.image.fill('grey')

        self.fillPokeData()

    def on_click(self): 
        for elem in self.group:
            if hasattr(elem, 'switchie'):
                if elem.switchie == True:
                    elem1index = elem.posIndex
                    elem2index = self.posIndex

                    self.player.pokemonBag.pop(elem1index)
                    self.player.pokemonBag.insert(elem1index, self.pokemon)
                    
                    self.player.pokemonBag.pop(elem2index)
                    self.player.pokemonBag.insert(elem2index, elem.pokemon)

                    elem.switchie = False

                    for elem in self.group:
                        if isinstance(elem, Menu) and elem.job == 'PokeInfo':
                            elem.kill()
                        elif isinstance(elem, Options) and elem.job == 'InfoOpt':
                            elem.kill()
                        elif isinstance(elem, PokemonOptions):
                            elem.kill()

                    optionsParent = self.parent
                    
                    for index, poke in enumerate(self.player.pokemonBag):
                        PokemonOptions(self.group, optionsParent, poke, index, self.player)
                    
                    return
        self.inUse = True
        for elem in self.group:
            if isinstance(elem, PokemonOptions):
                elem.active = False
            
        Menu(self.group, self.pokemon, 'PokeInfo')
        
class LevelBar(pygame.sprite.Sprite):
    def __init__(self, group, pokemon, x, y):
        super().__init__(group)

        self.image = pygame.Surface((96,8))
        self.rect = self.image.get_rect(topleft = (x,y))

        amount = (pokemon.data.exp - pokemon.data.expNeeded()[2]) / (pokemon.data.expNeeded()[0] - pokemon.data.expNeeded()[2])
        
        self.fillBar = pygame.Surface((64*amount, 8))
        self.fillBar.fill('light blue')

        self.image.blit(self.fillBar, [0,0])
        
class CloseButton(pygame.sprite.Sprite):
    def __init__(self,group, parent):
        super().__init__(group)

        self.image = pygame.Surface((64,64))
        self.rect = self.image.get_rect(topleft = (1206,10))
        self.group = group
        self.active = True
        
        self.parent = parent

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image.fill('dark grey')
        else:
            self.image.fill('black')
            
    
    def on_click(self):
        for elem in self.group:
            if hasattr(elem, 'parent') and elem.parent == self.parent:
                elem.kill()
            elif isinstance(elem, LevelBar):
                elem.kill()
            elif isinstance(elem, Menu) and elem.job == 'PokeInfo':
                elem.kill()
            elif isinstance(elem, Options) and elem.job == 'InfoOpt':
                elem.kill()
            elif hasattr(elem, 'switchie'):
                elem.switchie = False
        if isinstance(self.parent, PokemonIndetifier):
            for elem in self.group:
                if hasattr(elem, 'job') and elem.job == 'InvOpt':
                    elem.active = True
                    
        self.parent.kill()
        self.kill()
        