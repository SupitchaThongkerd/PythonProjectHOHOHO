import pygame, sys
import os
import time
import random


clock = pygame.time.Clock()

from pygame.locals import *
pygame.init() 

pygame.display.set_caption("HOHOHO GIVE MY SLEIGH BACK!")

window_size = (800, 600)

screen = pygame.display.set_mode(window_size, 0, 32)

santa = pygame.image.load("santa.png")

while True:
    santa = pygame.image.load("santa.png")

    screen.blit(santa, (50, 50))

    for event in pygame.event.get():
        if event.type == QUIT:
            
            pygame.quit()
            sys.exit()

    pygame.display.update
    #keep the game running at limited fps
    clock.tick(60)