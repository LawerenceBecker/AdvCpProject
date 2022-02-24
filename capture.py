import pygame
import random

def capture(player, pokemonName):
    print(f'\nWild {pokemonName} is avilable to capture')
    print('Throw Ball?')
    for index, item in enumerate(player.bag['Pokeballs']):
        print(f'{index+1}. {item[0].name} x{item[1]}')

    ball = int(input('> '))

    for index, item in enumerate(player.bag['Pokeballs']):
        if ball == index+1:
            print(f'You throw a {item[0].name}')
            if item[0].name == 'Poké Ball':
                catchChance = 20
            elif item[0].name == 'Great Ball':
                catchChance = 40
            elif item[0].name == 'Ultra Ball':
                catchChance = 60
            player.remove_item(item[0])

    randChance = random.randint(0, 100)

    if randChance <= catchChance:
        print('You Caught it')
        player.add_pokemon(pokemonName)
    else:
        print('It ran it away')
