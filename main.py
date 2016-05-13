#-------------------------------------------------------------------------------
# Name:        boilerplate
# Purpose:      to start projects in pygame faster
#
# Author:      jholt
#
# Created:     11/05/2016
# Copyright:   (c) jholt 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame
import sys
from pygame.locals import *
from board import Board

pygame.init()

#settings to change
screen_size = (306,306)
framerate = 60
back_color = (255,207,107)

#some initialization
screen = pygame.display.set_mode(screen_size)
font = pygame.font.SysFont(None,36)
clock = pygame.time.Clock()
screen.fill(back_color)
game = Board()

#vars
lines = [((101,0),(101,305)), ((204,0),(204,305)), ((0,101),(305,101)), ((0,204),(305,204))]
plays = []
x_turn = True

#helper functions
def draw_text(string, font, surface, x, y):
    txt_display = font.render(string, 1, (0,0,0))
    surface.blit(txt_display, (x,y))

def get_xy(mouse_pos):
    x = -1
    y = -1
    if mouse_pos[0] <= 99:
        x = 0
    elif mouse_pos[0] <= 203:
        x = 1
    else:
        x = 2
    if mouse_pos[1] <= 99:
        y = 0
    elif mouse_pos[1] <= 203:
        y = 1
    else:
        y = 2
    return (x,y)

#x = pygame.image.load("imgs/X.png").convert_alpha()
#o = pygame.image.load("imgs/O.png").convert_alpha()

#game loop
while True:
    clock.tick(framerate)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            pos = get_xy(pygame.mouse.get_pos())
            if x_turn and game.setX(*pos):
                x_turn = False
                draw_pos = ((pos[0] * 100) + (pos[0] * 3), (pos[1] * 100) + (pos[1] * 3))
                x = pygame.image.load("imgs/X.png").convert_alpha()
                plays.append((x,draw_pos))
            elif not x_turn and game.setO(*pos):
                x_turn = True;
                draw_pos = ((pos[0] * 100) + (pos[0] * 3), (pos[1] * 100) + (pos[1] * 3))
                o = pygame.image.load("imgs/O.png").convert_alpha()
                plays.append((o,draw_pos))

    screen.fill(back_color)
    for line in lines:
        pygame.draw.line(screen,(0,0,0),line[0],line[1],3)

    for play in plays:
        screen.blit(play[0],play[1])

    pygame.display.update()
