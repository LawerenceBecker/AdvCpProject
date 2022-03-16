import pygame
import sys

from player import Player
from pokemon import PygameData
from pickupItem import PickupItem
from npc import NPC
from item import Item
from tile import Tile
from csv import reader
from route import Route

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280,720))
        pygame.display.set_caption('Adv CP Pokemon Clone')
        pygame.init()
        self.clock = pygame.time.Clock()

        self.uiTick = pygame.time.get_ticks()

        self.sprites = CameraGroup()
        self.uiSprites = pygame.sprite.Group()
        self.objectSprites = pygame.sprite.Group()
        self.routeAreas = pygame.sprite.Group()

        self.CreateMap('Map/PokemonCloneTestMap.csv')

    def main(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:

                        if pygame.time.get_ticks() - self.uiTick >= 100:
                            for elem in self.uiSprites:
                                if elem.rect.collidepoint(pygame.mouse.get_pos()):
                                    if hasattr(elem, 'on_click'):
                                        if elem.active == True:
                                            elem.on_click()
                                            self.uiTick = pygame.time.get_ticks()
                                            break
                                        
                                        
                                        
                                        
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    sys.exit()

            self.screen.fill('#9edb64')

            self.sprites.custom_draw(self.player)
            self.uiSprites.draw(self.screen)
            self.uiSprites.update()
            self.player.update()

            pygame.display.update()
            self.clock.tick(60)

    def CreateMap(self, mapCSV):
        self.player = Player([self.sprites], 6, 6, self.objectSprites, self.routeAreas, self.uiSprites)
        
        choice = input('Load previous data?(y/n) \n> ')
        if choice.lower() == 'y':
            self.player.load_char()
        else:
            self.player.add_pokemon(PygameData('Charmander', 5), 'Test')
            self.player.add_pokemon(PygameData('Bulbasaur', 5), 'Test2')
            self.player.add_pokemon(PygameData('Squirtle', 5), 'Test3')
            self.player.add_pokemon(PygameData('Pidgey', 5), 'Test4')
            self.player.add_item(Item('Potion', 'Medicine'), 3)
            self.player.add_item(Item('Poké Ball', 'Pokeballs'), 10)
        
        PickupItem([self.sprites, self.objectSprites], 1, 1, Item('Potion', "Medicine"))
        NPC([self.sprites, self.objectSprites], 1, 7, 'shop', [[Item('Potion','Medicine'), 100], [Item('Poké Ball', 'Pokeballs'), 100], [Item('Great Ball', 'Pokeballs'), 200], [Item('Ultra Ball', 'Pokeballs'), 300], [Item('Master Ball', 'Pokeballs'), 100]])
        NPC([self.sprites, self.objectSprites], 1, 9, 'pokecenter')
        NPC([self.sprites, self.objectSprites], 9, 1, 'trainer', 'left', ['Test Trainer', PygameData('Bulbasaur', 4), PygameData('Pidgey', 3)])

        NPC([self.sprites, self.objectSprites], 4, 6, 'person', ['This is a test', 'Wow dialog', 'The guy by the grass is a special npc'])
        NPC([self.sprites, self.objectSprites], 4, 10, 'person', None, NPC.testSpecial)

        Route('Test', self.routeAreas)
        
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
