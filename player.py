import pygame
import pickle

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, objectSprites):
        super().__init__(groups)

        self.moveUp = pygame.image.load("Character/BoxUp.png").convert_alpha()
        self.moveDown = pygame.image.load("Character/BoxDown.png").convert_alpha()
        self.moveLeft = pygame.image.load("Character/BoxLeft.png").convert_alpha()
        self.moveRight = pygame.image.load("Character/BoxRight.png").convert_alpha()

        self.image = self.moveUp
        self.rect = self.image.get_rect(topleft = (0,0))

        self.prevTick = pygame.time.get_ticks()
        self.moveTimer = 250

        self.direction = pygame.math.Vector2()

        self.objectSprites = objectSprites

    def update(self):
        self.input()

        self.rect.x += self.direction.x * 64
        self.collision("horizontal")

        self.rect.y += self.direction.y * 64
        self.collision("vertical")


    def find_placement(self):
        return self.rect.centery

    def collision(self, direction):                        

        if direction == "horizontal":
            for sprite in self.objectSprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                        
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right
                        

        if direction == "vertical":
            for sprite in self.objectSprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                        
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
    
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LSHIFT]:
            self.moveTimer = 100
        else: 
            self.moveTimer = 250 

        self.direction = pygame.math.Vector2()

        if pygame.time.get_ticks() - self.prevTick >= self.moveTimer:
            if keys[pygame.K_BACKSPACE]:
                print('\nSaving... \n...')
                self.save_char()
                print('Done Saving')
                self.prevTick = pygame.time.get_ticks()

            elif keys[pygame.K_RETURN]:
                print('Reset(Debug)')
                self.rect.topleft = (0,0)
                self.save_char()
                self.prevTick = pygame.time.get_ticks()

            elif keys[pygame.K_DELETE]:
                print('\nLoading... \n...')
                self.load_char()
                print('Done Loading')
                self.prevTick = pygame.time.get_ticks()

            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self.direction.y = -1
                self.image = self.moveUp
                self.prevTick = pygame.time.get_ticks()

            elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.image = self.moveDown
                self.prevTick = pygame.time.get_ticks()
                
            elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.image = self.moveLeft
                self.prevTick = pygame.time.get_ticks()

            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.image = self.moveRight
                self.prevTick = pygame.time.get_ticks()

    def get_data(self):
        return self.rect.x, self.rect.y

    def save_char(self):
        with open("Data/CharData.plk", "wb") as charData:
            pickle.dump(self.get_data(), charData, -1)

    def load_char(self):
        with open('Data/CharData.plk', 'rb') as charData:
            self.rect.x, self.rect.y = pickle.load(charData)
