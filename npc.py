import pygame

class NPC(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, job, shopInv):

        super().__init__(groups)

        self.image = pygame.Surface((64,64))
        self.image.fill('blue')

        self.rect = self.image.get_rect(topleft = (x*64,y*64))
        self.hitbox = self.rect.inflate(6,6)
        self.placement = 1

        self.job = job
        self.tileType = ''

        self.shopInv = shopInv

    def shop(self):
        print('What do you want to buy?')

        for index,item in enumerate(self.shopInv):
            print(f'{index+1}. {item[0]} ${item[1]}')

        choice = int(input('> '))

        for index,item in enumerate(self.shopInv):
            if index+1 == choice:
                print(f'You bought {item[0]} for {item[1]}')