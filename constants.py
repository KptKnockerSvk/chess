import pygame

#CONSTANTS
BLACK = (90,89,84)
WHITE = (255,255,255)
YELLOW = (243,155,6)
GREEN = (62,200,0)

WIDTH = 600
HEIGHT = 600
CURRENT_ROUND = 0

COLS = ["a", "b", "c", "d","e", "f", "g", "h"]
PAWNS = [["a2"], ["b2"], ["c2"], ["d2"], ["e2"], ["f2"], ["g2"], ["h2"]]
TOWERS = [["a1"], ["h1"]]
HORSES = [["b1"], ["g1"]]
BISHOPS = [["c1"], ["f1"]]
ROYALS = [["d1"], ["e1"]]  
##
PAWNS2 = [["a7"], ["b7"], ["c7"], ["d7"], ["e7"], ["f7"], ["g7"], ["h7"]]
TOWERS2 = [["a8"], ["h8"]]
HORSES2 = [["b8"], ["g8"]]
BISHOPS2 = [["c8"], ["f8"]]
ROYALS2 = [["e8"], ["d8"]] 


all_figs_in = [PAWNS, TOWERS, HORSES, BISHOPS, ROYALS]
sec_team_all_figs = [PAWNS2, TOWERS2, HORSES2, BISHOPS2, ROYALS2]
#IMAGES
pawn = pygame.image.load("images\pawn.png")
bishop = pygame.image.load("images\ig_bishop.png")
horse = pygame.image.load("images\horse.png")
king = pygame.image.load("images\king.png")
queen = pygame.image.load("images\queen.png")
tower = pygame.image.load("images\ower.png")