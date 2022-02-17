import pygame
import random

def capture(player, pokemonName):
    print(f'\nWild {pokemonName} is avilable to capture')
    print('Throw Ball?')
    print('1. Pokeball')
    print('2. Greatball')
    print('3. Ultraball')

    ball = input('> ')

    if ball == '1':
        print('You throw a Pokeball')
        catchChance = 20
    elif ball == '2':
        print('You throw a Greatball')
        catchChance = 40
    elif ball == '3':
        print('You throw a Ultraball')
        catchChance = 60

    randChance = random.randint(0, 100)

    if randChance <= catchChance:
        print('You Caught it')
        player.add_pokemon(pokemonName)
    else:
        print('It ran it away')
