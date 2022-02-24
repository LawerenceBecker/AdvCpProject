import pygame
import random

def capture(player, pokemon):
    print(f'\nWild {pokemon.data.name} is avilable to capture')
    while True:
        if len(player.bag['Pokeballs']) == 0:
            ('You ran out of balls')
            return
        print('Throw a Ball?')
        for index, item in enumerate(player.bag['Pokeballs']):
            print(f'{index+1}. {item[0].name} x{item[1]}')
        print(f'{index+2}. Give up')

        
        ball = int(input('> '))

        if ball == index+2:
            print(f'You let {pokemon.data.name} run away')
            return
        
        for index, item in enumerate(player.bag['Pokeballs']):
            if ball == index+1:
                print(f'You throw a {item[0].name}')
                if item[0].name == 'Poké Ball':
                    ball = 12
                elif item[0].name == 'Great Ball':
                    ball = 8
                elif item[0].name == 'Ultra Ball':
                    ball = 4
                player.remove_item(item[0])
    
        m = random.randint(0, 255)
    
        f = (pokemon.data.maxHealth * 255 * 4) / (pokemon.data.health * ball)
        
        if f >= m:
            print('You Caught it')

            nickName = input("Give it a name \n> ")

            if nickName == None:
                nickName = pokemon.data.name

            print(f'{nickName} joins your party')
            
            player.add_pokemon(pokemon, nickName)
            return
        else:
            print('It broke free')
