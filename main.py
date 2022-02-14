import pygame
from pygame.locals import *

clock = pygame.time.Clock()

pygame.init();

win = pygame.display.set_mode((250,250));
pygame.display.set_caption("Definitely Not Pokémon");

moveUp = pygame.image.load("Character/BoxUp.png");
moveDown = pygame.image.load("Character/BoxDown.png");
moveLeft = pygame.image.load("Character/BoxLeft.png");
moveRight = pygame.image.load("Character/BoxRight.png");

image = moveUp;

x = 100;
y = 100;

running = True;

while running:
  
  for event in pygame.event.get():
    if event.type == QUIT:
      running = False;
      pygame.quit();
      quit();
  
  keys = pygame.key.get_pressed()

  if keys[pygame.K_UP]:
    y += -5;
    image = moveUp;
  elif keys[pygame.K_DOWN]:
    y += 5;
    image = moveDown;
  elif keys[pygame.K_LEFT]:
    x += -5;
    image = moveLeft;
  elif keys[pygame.K_RIGHT]:
    x += 5;
    image = moveRight;

  win.fill('green');
  win.blit(image, (x, y));

  pygame.display.update();
  clock.tick(60);