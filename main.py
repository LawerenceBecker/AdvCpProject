import pygame
import sys

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Adv CP Pokemon Clone')
clock = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                sys.exit()

        screen.fill('#9edb64')

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()