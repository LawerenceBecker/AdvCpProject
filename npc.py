import pygame
import sys, time

def delayPrint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.025)


class NPC(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, job, specialInfo=None, specialInteraction=None):

        super().__init__(groups)

        self.image = pygame.Surface((64,64))
        if job == 'shop': self.image.fill('blue')
        elif job == 'pokecenter': self.image.fill('red')
        elif job == 'person': self.image.fill('grey')
        elif job == 'trainer': self.image.fill('white')
            

        self.rect = self.image.get_rect(topleft = (x*64,y*64))
        self.hitbox = self.rect.inflate(2,2)
        self.placement = 1
        
        self.job = job
        self.tileType = ''

        self.shopInv = specialInfo
        self.dialogArray = specialInfo
        self.facing = specialInfo
        self.npcPokeBag = specialInteraction
        self.active = True
        
        self.specialInteraction = specialInteraction

    def person(self, player):
        if self.specialInteraction:
            self.specialInteraction(self, player)
            return
        for text in self.dialogArray:
            delayPrint(f'\n{text}')
            input('')

    def testSpecial(self, player):
        print('\n'*3)

        print('\nI have the abilty to do unique stuff like,')
        player.rect.x += 64
        delayPrint('\nmoving you')
    
    def pokeCenter(self, player):
        while True:
            print('\nWelcome to the Pokemon Center')
            choice = input('Would you like to have us heal your pokemon? \n1. Yes \n2. No \n> ')
            if choice == '1':
                print('Just one moment')

                if len(player.pokemonBag) == 1: print('-------\n| o . |\n| . . |\n| . . |\n-------')
                elif len(player.pokemonBag) == 2: print('-------\n| o o |\n|     |\n|     |\n-------')
                elif len(player.pokemonBag) == 3: print('-------\n| o o |\n| o   |\n|     |\n-------')
                elif len(player.pokemonBag) == 4: print('-------\n| o o |\n| o o |\n|     |\n-------')
                elif len(player.pokemonBag) == 5: print('-------\n| o o |\n| o o |\n| o   |\n-------')
                elif len(player.pokemonBag) == 6: print('-------\n| o o |\n| o o |\n| o o |\n-------')

                delayPrint('\nding.')
                delayPrint('\nding..')
                delayPrint('\nding!')

                for pokemon in player.pokemonBag:
                    pokemon.data.health = pokemon.stats('MaxHealth')

                delayPrint('\n\nYour pokemon are fully healed')
                delayPrint('\nPlease come back again')

                return
                
            elif choice == '2':
                print('Please come back again')
                return
            
    
    def shop(self, player):
        while True:
            if player.money == 0:
                print('You have no money')
                return
                
            print('\nWhat do you want to buy?')
            print(f'Player Money: {player.money}\n')
    
            for index,item in enumerate(self.shopInv):
                print(f'{index+1}. {item[0].name} ${item[1]}')
            print(f'{index+2}. End')
    
            choice = int(input('> '))

            if choice == index+2:
                return
            
            for index,item in enumerate(self.shopInv):
                if index+1 == int(choice):
                    item[0].name
                    choice = int(input('How many > '))
                    if choice == 0:
                        return
                    elif player.money >= (item[1] * choice):
                        player.money -= item[1] * choice
                        player.add_item(item[0], choice)
                        print(f'You bought {item[0].name} for {item[1]*int(choice)}')
                        return
                    else:
                        print('You can\'t afford that')
                    