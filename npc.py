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

    def shop(self, player):
        while True:
            print('\nWhat do you want to buy?')
            print(f'Player Money: {player.money}\n')
    
            for index,item in enumerate(self.shopInv):
                print(f'{index+1}. {item[0].name} ${item[1]}')
    
            choice = int(input('> '))
    
            for index,item in enumerate(self.shopInv):
                if index+1 == choice:
                    item[0].name
                    choice = int(input('How many > '))
                    if player.money >= (item[1] * choice):
                        player.money -= item[1]
                        player.add_item(item[0], choice)
                        print(f'You bought {item[0].name} for {item[1]*choice}')
                        return
                    else:
                        print('You can\'t afford that')
                    