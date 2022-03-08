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
        
class RouteLabel(pygame.sprite.Sprite):
    def __init__(self, group, text):
        super().__init__(group)
        
        self.font = pygame.font.Font('asset/DisposableDroidBB.ttf', 36)
        self.text = self.font.render(text, True, (0,0,0))

        self.image = pygame.Surface((self.text.get_width()+20, self.text.get_height()+10))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = ((pygame.display.get_surface().get_size()[0]/2)-(self.text.get_width()/2), 0))

        self.image.blit(self.text, [10, 5])

        self.prevTick = pygame.time.get_ticks()
        self.startFading = False
        self.timer = 400

    def update(self):
        if self.rect.y <= -self.rect.h:
            self.kill()
        if self.startFading == True:
            if pygame.time.get_ticks() - self.prevTick >= 20:
                self.rect.y -= 2
                self.prevTick = pygame.time.get_ticks()
            
        if pygame.time.get_ticks() - self.prevTick >= self.timer:
            self.startFading = True
            self.prevTick = pygame.time.get_ticks()
