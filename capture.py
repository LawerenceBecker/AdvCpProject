import pygame
import random

def ball_shake(catchRate, ballPick, f):
    if ballPick == 'Poké Ball': ball = 255
    if ballPick == 'Great Ball': ball = 200
    if ballPick == 'Ultra Ball': ball = 150
    
    d = (catchRate * 255) / ball

    x = (d * f) / 255

    if x < 30:
        print('shake.')
    elif x < 70:
        print('shake.')
        print('shake..')
    else:
        print('shake.')
        print('shake..')
        print('shake...')
        

def capture(player, pokemon):
    print(f'\nWild {pokemon.data.name} is avilable to capture')
    while True:
        if len(player.bag['Pokeballs']) == 0:
            ('You ran out of balls')
            return
        print('\nThrow a Ball?')
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
                    break
                elif item[0].name == 'Great Ball':
                    ball = 8
                    break
                elif item[0].name == 'Ultra Ball':
                    ball = 4
                    break
                elif item[0].name == 'Master Ball':
                    print('shake.')
                    print('shake..')
                    print('shake...')
                    print('You Caught it')

                    nickName = input("Give it a name \n> ")
        
                    if nickName == None:
                        nickName = pokemon.data.name
        
                    print(f'{nickName} joins your party')
                    
                    player.add_pokemon(pokemon, nickName)
                    return
                

        player.remove_item(item[0])
        m = random.randint(0, 255)
    
        f = (pokemon.data.maxHealth * 255 * 4) / (pokemon.data.health * ball)
        
        if f >= m:
            print('shake.')
            print('shake..')
            print('shake...')
            print('You Caught it')

            nickName = input("Give it a name \n> ")

            if nickName == None:
                nickName = pokemon.data.name

            print(f'{nickName} joins your party')
            
            player.add_pokemon(pokemon, nickName)
            return
        else:
            ball_shake(m, player.bag['Pokeballs'][index][0].name, f)
            print('It broke free')
