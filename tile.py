import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, tileType=''):
        super().__init__(groups)

        if tileType == 'grass':
            self.image = pygame.image.load('Tiles/Tall Grass.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (x*64, y*64))
            self.placement = 0

        else:
            self.image = pygame.image.load('Tiles/Temp Tree.png').convert_alpha()            
            self.rect = self.image.get_rect(topleft = (x*64, y*64))
            self.placement = 1
        
        self.tileType = tileType

