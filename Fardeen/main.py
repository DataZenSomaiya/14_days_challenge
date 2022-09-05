import pygame
import os
import sys


screen_width = 1244
screen_height = 1016
SCREEN  = pygame.display.set_mode((screen_width, screen_height))

TRACK = pygame.image.load(os.path.join("assets", "track.png"))

def eval_genomes():
    run = True
    while run: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.blit(TRACK, (0,0))

eval_genomes()
        