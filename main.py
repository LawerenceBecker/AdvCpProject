import pygame
import sys

from player import Player
from tile import Tile

def main():

  screen = pygame.display.set_mode((1280,720))
  pygame.display.set_caption('Adv CP Pokemon Clone')
  clock = pygame.time.Clock()
    
  sprites = CameraGroup()
  objectSprites = pygame.sprite.Group()

  player = Player(sprites, objectSprites)
  player.load_char()
  player.add_pokemon('Charmander')
  Tile([sprites, objectSprites])
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.QUIT
        sys.exit()

    screen.fill('#9edb64')

    sprites.custom_draw(player)
    player.update()

    pygame.display.update()
    clock.tick(60)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

if __name__ == '__main__':
  main()
