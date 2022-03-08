import pygame
from routeData import *

class Route(pygame.sprite.Sprite):
    def __init__(self, id, group):
        super().__init__(group)

        self.image = pygame.Surface(routes[id]['AreaSize'])
        self.rect = self.image.get_rect(topleft = (routes[id]['Position']))
        self.image.set_alpha(0)

        self.entered = False

        self.name = routes[id]['Name']
        self.pokemonTable = routes[id]['PokemonTable']
