import pygame
import sys

from player import Player
<<<<<<< HEAD
from npc import NPC
=======
>>>>>>> 97ab58a80c8b27a5d6ef4b25c9769835ef21ea85
from item import Item
from tile import Tile
from csv import reader

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280,720))
        pygame.display.set_caption('Adv CP Pokemon Clone')
        self.clock = pygame.time.Clock()

        self.sprites = CameraGroup()
        self.objectSprites = pygame.sprite.Group()

        self.CreateMap('Map/PokemonCloneTestMap.csv')

    def main(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    sys.exit()

            self.screen.fill('#9edb64')

            self.sprites.custom_draw(self.player)
            self.player.update()

            pygame.display.update()
            self.clock.tick(60)

    def CreateMap(self, mapCSV):
        self.player = Player([self.sprites], 6, 6, self.objectSprites)
        self.player.load_char()
        self.player.add_item(Item('Potion', 'Medicine'), 3)
        self.player.add_item(Item('Poké Ball', 'Pokeballs'), 10)
        self.player.add_pokemon('Charmander')
        self.player.add_pokemon('Charmander')
        self.player.add_pokemon('Charmander')
<<<<<<< HEAD

        NPC([self.sprites, self.objectSprites], 2, 7, 'shop', [['Potion', '100'], ['Poké Ball', '100']])
=======
>>>>>>> 97ab58a80c8b27a5d6ef4b25c9769835ef21ea85

        terrainLayout = []
        with open(mapCSV) as levelMap:
            layout = reader(levelMap, delimiter = ',')
            for row in layout:
                terrainLayout.append(list(row))

        for rowIndex, row in enumerate(terrainLayout):
            for colIndex, col in enumerate(row):
                x = colIndex
                y = rowIndex
                if col == '0':
                    Tile([self.sprites, self.objectSprites], x, y)
                elif col == '1':
                    Tile([self.sprites, self.objectSprites], x, y, 'grass')




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

        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.placement):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

if __name__ == '__main__':
 game = Game()
 game.main()
