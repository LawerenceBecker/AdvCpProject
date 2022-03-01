import pygame

class PickupItem(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, item):
        super().__init__(groups)

        self.image = pygame.Surface((32, 32))
        self.rect = self.image.get_rect(topleft = ((x*64)+16, (y*64)+16))
        self.rect.w = 48
        self.rect.h = 48
        self.hitbox = self.rect.inflate(1, 1)

        self.item = item
        self.tileType = ''
        
        self.placement = 1