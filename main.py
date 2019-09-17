import pygame
import sys
from pygame.locals import*

pygame.init()

screen = pygame.display.set_mode([600,500])
pygame.display.set_caption('ASCIInvaders')

player_x = 260
#player_y = 250
player_v = 0.5

player = pygame.image.load('Trabalho/navinh.png')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == K_d:
            player_x += player_v
        if event.key == K_a:
            player_x -= player_v
    screen.blit(player,(player_x,450))
    pygame.display.flip()
    screen.fill((0,0,0))


