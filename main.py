import pygame
import sys

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Adv CP Pokemon Clone')
clock = pygame.time.Clock()

moveUp = pygame.image.load("Character/BoxUp.png");
moveDown = pygame.image.load("Character/BoxDown.png");
moveLeft = pygame.image.load("Character/BoxLeft.png");
moveRight = pygame.image.load("Character/BoxRight.png");

image = moveUp;

x = 100;
y = 100;

def main():
  global image, x, y

  prevTick = pygame.time.get_ticks()

  moveTimer = 250
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.QUIT
        sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LSHIFT]:
      moveTimer = 100
    else: 
      moveTimer = 250

    if pygame.time.get_ticks() - prevTick >= moveTimer:
        if keys[pygame.K_UP]:
            y += -64;
            image = moveUp;
            prevTick = pygame.time.get_ticks()
        elif keys[pygame.K_DOWN]:
            y += 64;
            image = moveDown;
            prevTick = pygame.time.get_ticks()
        elif keys[pygame.K_LEFT]:
            x += -64;
            image = moveLeft;
            prevTick = pygame.time.get_ticks()
        elif keys[pygame.K_RIGHT]:
            x += 64;
            image = moveRight;
            prevTick = pygame.time.get_ticks()

    screen.fill('#9edb64')
    screen.blit(image, (x, y));

    pygame.display.update()
    clock.tick(60)

if __name__ == '__main__':
  main()
