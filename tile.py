import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.image = pygame.Surface((64,64))
        self.rect = self.image.get_rect(topleft = (128, 64))

    def find_placement(self):
        return self.rect.centery