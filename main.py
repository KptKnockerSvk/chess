import pygame
from functions import *

#CONSTANTS
BLACK = (90,89,84)
WHITE = (255,255,255)
WIDTH = 600
HEIGHT = 600

#IMAGES
pawn = pygame.image.load("images\pawn.png")

#SCREEN INIT
pygame.init()
win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chess Master Pro Ultimate Edition")
pygame.display.set_icon(pawn)

clock = pygame.time.Clock()

def get_clicked_coords(poss):
    pos = poss
    #Get "a2" of clicked position
    if pos != None:   
        if 0 < pos[0] < 800:   
            if 0 < pos[0] < 100:
                first = "a"
            elif pos[0] < 200:
                first = "b"
            elif pos[0] < 300:
                first = "c"
            elif pos[0] < 400:
                first = "d"
            elif pos[0] < 500:
                first = "e"
            elif pos[0] < 600:
                first = "f"
            elif pos[0] < 700:
                first = "g"
            elif pos[0] < 800:
                first = "h"

        if 0 < pos[1] < 800:
            if 0 < pos[1] < 100:
                sec = "8"
            elif pos[1] < 200:
                sec = "7"
            elif pos[1] < 300:
                sec = "6"
            elif pos[1] < 400:
                sec = "5"
            elif pos[1] < 500:
                sec = "4"
            elif pos[1] < 600:
                sec = "3"
            elif pos[1] < 700:
                sec = "2"
            elif pos[1] < 800:
                sec = "1"
        strng = first + sec
        pos = None
        return strng

def change_pos(text):
    strng = text
    #If string "a2" is given, find fig_type and change pos on click
    if strng != None:
        indx = -1
        dic_for_fig = {
            0: PAWNS,
            1: TOWERS,
            2: HORSES,
            3: BISHOPS,
            4: ROYALS}
        z = [strng]
        for i in all_figs_in:
            indx += 1
            for y in i:
                if z == y:
                    index_of_cur_fig = i.index(z)
                    dic_val = dic_for_fig[indx]     
                    strng = None  
                    while True:  
                        for event in pygame.event.get():                      
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pos = pygame.mouse.get_pos()
                                strng = [get_clicked_coords(pos)]
                        if strng != None:
                            break
                    dic_val[index_of_cur_fig] = strng
                    print(PAWNS)
        strng = None    


def game_is_on():
    running = True
    pos = None
    strng = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos() 
                print(pos) 
        #print rectangles of color
        help_var = 0
        for rows in range(8):
            help_var += 1
            for cols in range(8):
                help_var += 1
                if help_var % 2 == 0:
                    color = BLACK
                else:
                    color = WHITE
                pygame.draw.rect(win,color, (0+100*cols,0+100*rows,100,100))
        
        #Setting figures
        for i in range(8):
            win.blit(pawn, (0+100*i,600)) #1. do prava, 2. dole

        if pos != None:
            strng = get_clicked_coords(pos)

        if strng != None:
            change_pos(strng)

        pygame.display.flip()
        clock.tick(60)

        pygame.quit



game_is_on()  

    
    
    
