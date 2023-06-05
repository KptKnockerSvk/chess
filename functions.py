import pygame 
from constants import *


#SCREEN INIT
pygame.init()
win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chess Master Pro Ultimate Edition")
pygame.display.set_icon(pawn)

clock = pygame.time.Clock()

#Get "a2" of clicked position
def get_clicked_coords(poss):
    pos = poss
    
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
        indx = -1
        dic_for_fig = {
            0: PAWNS,
            1: TOWERS,
            2: HORSES,
            3: BISHOPS,
            4: ROYALS}
        
        z = [strng]
        end = 0
        for i in all_figs_in:            
            if end == 1:
                break
            indx += 1
            for y in i:
                if z == y:
                    index_of_cur_fig = i.index(z)
                    dic_val = dic_for_fig[indx] 
                    end = 1
                    if indx == 4 and z == ROYALS[1]:
                        indx = 5
                    break  
        return indx, z
    
def creation_of_field():
    board_in = [["__"], ["__"], ["__"], ["__"], ["__"], ["__"], ["__"], ["__"],    # 0
                ["__"], ["__"], ["__"], ["__"], ["__"], ["__"], ["__"], ["__"],    # 1
                ["__"], ["__"], ["__"], ["__"], ["__"], ["__"], ["__"], ["__"],    # 2
                ["__"], ["__"], ["__"], ["__"], ["__"], ["__"], ["__"], ["__"],    # 3
                ["__"], ["__"], ["__"], ["__"], ["__"], ["__"], ["__"], ["__"],    # 4
                ["__"], ["__"], ["__"], ["__"], ["__"], ["__"], ["__"], ["__"],    # 5
                ["__"], ["__"], ["__"], ["__"], ["__"], ["__"], ["__"], ["__"],    # 6 
                ["__"], ["__"], ["__"], ["__"], ["__"], ["__"], ["__"], ["__"]]    # 7
                # A0      B1      C2      D3      E4      F5      G6      H7    
                # 97      98      99      100     101     102     103     104
    figure_transformation(board_in, all_figs_in+sec_team_all_figs, 1)
    return board_in

def current_board(board_out):
    current_row = []
    board_in = board_out
    
    for i in range(8):
        for y in range(8):
            h = (i * 8) + y
            
            #print(board_in[h])
            current_row.append(board_in[h])
        print(str(current_row))
        current_row = []
    return "This is current board"

def figure_transformation(board_in, given_list, sett=None):
    figs = given_list[:]
    x = sett
    if x == 1:
        for i in figs:
            #print(i)
            for y in i:
                fig_to_be_added = str(y)
                coors = COLS.index(fig_to_be_added[2]) + ((8 - int(fig_to_be_added[3]))*8)
                board_in[coors] = y           
    else:
        print("No need for transf")     

def figure_movement(choice, numm, indx, fg_indx):
    fig, num, index, fig_index = choice, numm, indx, fg_indx
    num_string = str(num)
    str_1 = num_string[2][0][0]
    str_2 = num_string[3][0][0]    
    new_index = COLS.index(str_1) + ((8 - int(str_2)) * 8)
    board_out[new_index] = num
    board_out[index] = ["__"]
    
    if fig == 0:    
        PAWNS[fig_index] = num  
    elif fig == 1:
        TOWERS[fig_index] = num
    elif fig == 2:
        HORSES[fig_index] = num
    elif fig == 3:
        BISHOPS[fig_index] = num          
    elif fig == 4:
        ROYALS[0] = num
    elif fig == 5:
        ROYALS[1] = num          
    else: 
        print("Failll")

def pawn_movement(cor):        
    
    pos = str(cor)[2:4]
    p_index_as_board = board_out.index([pos])
    index_in_pawns = PAWNS.index([pos])
    #Check for enemy
    x = ord(pos[0]) - 1
    y = ord(pos[0]) + 1
    h_l_1 = chr(y) + str(int(pos[1]) + 1)
    h_l_2 = chr(x) + str(int(pos[1]) + 1)
    next_pos = []

    #Positions for attackable enemy figures
    if x == 96:
        next_pos.append(h_l_1)
    elif y == 105:
        next_pos.append(h_l_2)
    else:
        next_pos.append(h_l_1)
        next_pos.append(h_l_2)
    help_list = next_pos[:]
    attackable = []
    for i in next_pos:  
        help_i = [[]]
        help_i[0] = i + "x"
        if help_i in board_out:
            print("Possible attack move! ")
            attackable.append(help_i)
        else:
            help_list.remove(i)
    
    next_pos = help_list[:]
    
    #Check for possible move
    front = [[]]
    front[0] = pos[0] + str(int(pos[1])+1)
    if front in board_out:
        x = 1
        print("Position up is occupied")
    else:
        x = 2
        print("Position up is not occupied")
        front = str(front)
        front = front[2] + front[3]        
        next_pos.append(front)

    #Check for double    
    front = [[]] 
    if pos[1] == "2":
        front2 = pos[0] + str(int(pos[1]) + 2)
        front[0] = front2
        if front in board_out:
            print(f"{front2} is currenctly occupied")
        else:
            next_pos.append(front2)
    
    choice = choose_a_choice(next_pos, attackable, [pos])   

    return choice, p_index_as_board, index_in_pawns 

def tower_movement(cor):
    #choose which tower
    tower_str = str(cor)[2:4]      
    index_of_tows = TOWERS.index([tower_str])
    index_of_tow = board_out.index([tower_str])

    next_pos, attackable = straight_movement(tower_str)

    #Choose which one  
    choice = choose_a_choice(next_pos, attackable, [tower_str])
    return choice, index_of_tow, index_of_tows
        
def horse_movement(cor):
    
    horse_str = str(cor)[2:4]
    index_of_horse = board_out.index([horse_str])
    index_of_horses = HORSES.index([horse_str])
    
    #Possible movement
    x = chr(ord(horse_str[0]) - 2)
    y = int(horse_str[1]) + 1
    
    pos_list = []
    attackable = []
    for i in range(2):
        if i == 1:
            y = int(y[1])
        st1 = x + str(y - i*2) #b6
        st2 = chr(ord(x) + 1) + str((y + 1) - (4*i)) #c7
        st3 = chr(ord(x) + 3) + str((y + 1) - 4*i) #e7
        st4 = chr(ord(x) + 4) + str(y - 2*i)     #f6
        st_list = [st1, st2, st3, st4]
        st_list_copy = st_list[:]
        for y in st_list_copy:
            if len(y) > 2:
                st_list.remove(y)        
        for y in st_list:
            if y[0] in "abcdefgh" and 0 < int(y[1]) < 9 and len(y) == 2:
                board_indx_for_attack = COLS.index(y[0]) + ((8 - int(y[1])) * 8)
                if len(board_out[board_indx_for_attack]) == 3:
                    attackable.append(y)
                else:
                    pos_list.append(y)
    
    #check if valid
    help_list2 = pos_list[:]
    h_list = [[]]
    for i in help_list2:
        h_list[0] = i
        if h_list in board_out:
            print(f"Sorry pal, {h_list[0]} is occupied")
            pos_list.remove(h_list[0])
    #Choosing fig to move
    choice = choose_a_choice(pos_list, attackable, [horse_str])
    
    return choice, index_of_horse, index_of_horses

def bishop_movement(cor):
    bish_to_move = str(cor)[2:4]
    bish_index_in_board = board_out.index([bish_to_move])
    index_in_bishops = BISHOPS.index([bish_to_move])
    #Check for valid move  
    pos_list, attackable = diagonal_movement(bish_to_move)
    
    #Choose next pos
    choice = choose_a_choice(pos_list, attackable, [bish_to_move])

    return choice, bish_index_in_board, index_in_bishops

def queen_movement(cor):
    queen_as_str = str(cor)[2:4]
    q_index_as_board = board_out.index([queen_as_str])
    index_in_queens = 0

    first_list, fourth_list = diagonal_movement(queen_as_str)
    second_list, third_list = straight_movement(queen_as_str)   

    third_list = fourth_list[:] + third_list[:]
    first_list = first_list[:] + second_list[:] 
    #Choose which one
    choice = choose_a_choice(first_list, third_list, [queen_as_str])

    
    #Transformation    
    pos_list = choice
    return pos_list, q_index_as_board, index_in_queens 

def king_movement(cor):
    king_as_str = str(cor)[2:4]
    king_index_in_board = board_out.index([king_as_str])

    first_list, fourth_list = diagonal_movement(king_as_str)
    second_list, third_list = straight_movement(king_as_str)    

    third_list = fourth_list[:] + third_list[:]
    first_list = first_list[:] + second_list[:] + third_list[:]

    #Choose which one
    attackable = []
    moveable = []
    #kings ords, num    
    xx = ord(king_as_str[0])
    xy = int(king_as_str[1])
    for i in first_list:
        #check if in range of king
        x = ord(i[0])
        y = int(i[1])
        if xx - x == 1 or xx - x == -1 and  xy - 1 == y or xy + 1 == y:
            if i in third_list:
                attackable.append(i)
            else:
                moveable.append(i)
    choice = choose_a_choice(moveable, attackable, [king_as_str])
    
    return choice, king_index_in_board, 1

def check_if_chess(current_round):   
    round = current_round    
    list_of_spaces = [9,8,7,1,-1,-7,-8,-9]
    
    if round % 2 == 1:
        x = str(ROYALS[1])[2:4]   
        pawns_to_check = PAWNS2[:]
    else:
        x = str(ROYALS2[1])[2:4] 
        pawns_to_check = PAWNS[:]
    __, fourth_list = diagonal_movement(x)
    __, third_list = straight_movement(x)
    attackable = third_list[:] + fourth_list[:]
    chess_cond = []
    for i in attackable:
        space_betw = board_out.index([x]) - board_out.index([i])
        if space_betw in list_of_spaces:
            chess_cond.append(i)
            return chess_cond
        else:
            if [i] not in pawns_to_check:
                chess_cond.append(i)
                return chess_cond
    return None
    
def straight_movement(fig):
    fig_str = fig         
    #Possible boxes for move
    next_pos = []
    attackable = []       
    for i in range(4):        
        xx = 1
        if i == 0: #Values for heading
            y, z = 0, 1
        elif i == 1:
            y, z = 1, 0
        elif i == 2:
            y, z = 0,-1
        else:
            y, z = -1,0
        while True:
            next_string = chr(ord(fig_str[0]) + y*xx) + str(int(fig_str[1]) + z*xx) 
            xx += 1
            if 96 < ord(next_string[0]) < 105 and 0 < int(next_string[1]) < 9:
                ind_of_str = COLS.index(next_string[0]) + ((8 - int(next_string[1])) * 8)
                for ii in main_player:
                    for yy in ii:
                        if [next_string] in yy:
                            break  
                for iii in enemy_player:
                    for yyy in iii:
                        str_copy = [next_string]
                        if str_copy == yyy:
                            attackable.append(next_string) 
                            break
                if board_out[ind_of_str] == ["__"]:
                    next_pos.append(next_string)
                else:
                    break
            else:
                break
    return next_pos, attackable

def choose_a_choice(move, attack, cur_pos):
    movee = move[:] + cur_pos
    attackk = attack[:]
    xx = 0
    while True:
        if xx == 1:
            break
        if len(movee) == 0 and len(attackk) > 0:
            type_of_move = "a" 
            print(f"You can only attack, {attackk}")   
        elif len(attackk) == 0 and len(movee) > 0:
            type_of_move = "m"
            print(f"You can only move, {move}") 
        else:
            type_of_move = "ma"
        if type_of_move == "m":
            choosen_list = movee[:]
        elif type_of_move == "a":
            choosen_list = attackk[:]
        else:
            choosen_list = attackk[:] + movee[:]
            print(f"Attack: {attackk}, move: {movee}")
        xx = 0
        while True:
            if xx == 1:
                break
            for event in pygame.event.get():                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    __, choice = get_clicked_coords(pos)                    
                    timed_choice = str(choice)[2:4]
                    if timed_choice in choosen_list:
                        print(f"You have choosen --> {choice} <--")
                        xx = 1
                        break
                    else:
                        print("Unable to move")    
    
    for z in range(len(attackk)):
        print(z, choice)
        if choice == [attackk[z]]:
            print("point 1||||")
            for i in enemy_player:
                for y in i:
                    if choice == y:
                        print("point 2||||")
                        i.remove(choice)
                        print(PAWNS2)
                        xx = 1
    return choice

def diagonal_movement(fig_pos):
    f_pos = fig_pos
    next_pos = []
    attackable = []
    for i in range(4):  
        x = 1
        if i == 0: #Values for heading
            y, z = 1, 1
        elif i == 1:
            y, z = -1, 1
        elif i == 2:
            y, z = -1,-1
        else:
            y, z = 1,-1
        while True:
            next_string = chr(ord(f_pos[0]) + y*x) + str(int(f_pos[1]) + z*x)  
            x += 1
            if 96 < ord(next_string[0]) < 105 and 0 < int(next_string[1]) < 9:
                ind_of_str = COLS.index(next_string[0]) + ((8 - int(next_string[1])) * 8)
                for ii in main_player:
                    for yy in ii:
                        if [next_string] in yy:
                            break 
                for iii in enemy_player:
                    for yyy in iii:
                        str_copy = [next_string]
                        if str_copy == yyy:
                            attackable.append(next_string) 
                            break
                if board_out[ind_of_str] == ["__"]:
                    next_pos.append(next_string)
                else:
                    break
            else:
                break
    return next_pos, attackable

def current_player(round):    
    current_round = round
    main_player = all_figs_in[:]
    enemy_player = sec_team_all_figs[:]
    
    """ if current_round % 2 == 1:
        main_player = all_figs_in[:]
        enemy_player = sec_team_all_figs[:]
    else:
        main_player = sec_team_all_figs[:] 
        enemy_player = all_figs_in[:] """
    return main_player, enemy_player

board_out = creation_of_field() 

#Initialisation
def game_init(figg, cor):
    fig = figg       
    coor = cor 
    if fig == 0:                      
        pos_list, old_index, fig_index = pawn_movement(coor)   
    elif fig == 1:
        pos_list, old_index, fig_index = tower_movement(coor)
    elif fig == 2:
        pos_list, old_index, fig_index = horse_movement(coor)
    elif fig == 3:
        pos_list, old_index, fig_index = bishop_movement(coor)
    elif fig == 4:
        pos_list, old_index, fig_index = queen_movement(coor)
    elif fig == 5:
        pos_list, old_index, fig_index = king_movement(coor)
    else:
        print("Either wrong input or E")
    figure_movement(fig, pos_list, old_index, fig_index)  

def paint_figures(figures, pic):
        img = pic
        giv_list = figures
        
        for i in giv_list:
            i_str = str(i)
            position_x = COLS.index(i_str[2]) * 100
            position_y = ((8 - int(i_str[3])) * 100)
            
            win.blit(img, (position_x, position_y)) #1. do prava, 2. dole
            

cur_round_val = 0
if __name__ == "__main__":
    cur_round_val += 1
    
    running = True
    pos = None
    strng = None  
    (current_board(board_out))
    main_player, enemy_player = current_player(cur_round_val)
    check_if_chess(cur_round_val)
    while running:
        R_Q = ROYALS[0] + ROYALS2[0]
        R_K = ROYALS[1] + ROYALS2[1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                fig, coor = get_clicked_coords(pos)
                game_init(fig, coor)
                (current_board(board_out))
                pos = None
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
        
        
        for i in (all_figs_in + sec_team_all_figs):        
            if i == PAWNS or i == PAWNS2:
                pic = pawn
            elif i == TOWERS or i == TOWERS2:
                pic = tower 
            elif i == HORSES or i == HORSES2:
                pic = horse 
            elif i == BISHOPS or i == BISHOPS2:
                pic = bishop             
            else:
                for y in i:
                    pic = None
                    if y == [R_Q[0]] or y == [R_Q[1]]:
                        pic = queen
                    elif y == [R_K[0]] or y == [R_K[1]]:
                        pic = king
                    else:
                        pic = king

                    paint_figures([y], pic)
                    
            if i != ROYALS and i != ROYALS2:                           
                paint_figures(i, pic)

        if pos != None:
            strng = get_clicked_coords(pos)

        pygame.display.flip()
        clock.tick(60)

        pygame.quit


    
    
    
