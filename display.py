import pygame
import time
from pygame.locals import *

def display(board):   
    pygame.init()
    surface=pygame.display.set_mode((1000,1000))
    surface.fill((0,0,0))
    pygame.display.flip()


    a1=pygame.image.load("a1.jpg").convert()
    a5=pygame.image.load("a5.jpg").convert()
    ax=-100
    ay=-100
    for row in board:
        ax=-100
        ay+=100
        for instant in row:
            ax+=100
            if instant == "1":
                surface.blit(a1,(ax,ay))
            elif instant == "5":
                surface.blit(a5,(ax,ay))
    pygame.display.flip()
    
