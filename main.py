COLS = ["a", "b", "c", "d","e", "f", "g", "h"]
PAWNS = [["a2"], ["b2"], ["c2"], ["d2"], ["e2"], ["f2"], ["g2"], ["h2"]]
TOWERS = [["a3"], ["h1"]]
HORSES = [["b1"], ["g1"]]
BISHOPS = [["c1"], ["f1"]]
ROYALS = [["d3"], ["e1"]]
        
all_figs_in = [PAWNS, TOWERS, HORSES, BISHOPS, ROYALS]


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
    figure_transformation(board_in, all_figs_in, 1)
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

    if fig == "p":    
        PAWNS[fig_index] = num  
    elif fig == "t":
        TOWERS[fig_index] = num
    elif fig == "h":
        HORSES[fig_index] = num
    elif fig == "b":
        BISHOPS[fig_index] = num          
    elif fig == "q":
        ROYALS[0] = num
    elif fig == "k":
        ROYALS[1] = num          
    else: 
        print("Failll")

def pawn_movement():      
    print("Your pawns are:\n", PAWNS,"\n")
    pos =   int(input("int-Which one: ")) - 1 # 1 #
    pos = str(PAWNS[pos])
    pos = pos[2] + pos[3]
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
    for i in next_pos:  
        help_i = [[]]
        help_i[0] = i
        if help_i in board_out:
            print("Possible attack move! ")
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


    
    if len(next_pos) > 0:
        choose = int(input(f"int-Choose whitch one: \n{next_pos} \n--> ")) #1 # 
        next_pos = next_pos[choose-1]
        print(f"You have chosen {next_pos}")
    else:
        print("Not good")    
       
    
    pos_list = [[]]
    moving_pawn = [[]]
    while True:
        
        pos_list[0] = pos
        pos_index = PAWNS.index(pos_list)
        board_out[8 * (8 - int(pos[1])) + pos_index] = ["__"]
        moving_pawn[0] = pos[0] + str(int(pos[1]) + 1)
        PAWNS[pos_index] = moving_pawn
        pos_list[0] = next_pos
        return pos_list

def tower_movement():
    #choose which tower
    tower_str = 0 # int(input(f"int-Which one tower?: \n{TOWERS} \n--> ")) -1 #
    tower_str = str(TOWERS[tower_str])[2] + str(TOWERS[tower_str])[3]
    tower_list = [[]]
    tower_list[0] = tower_str    
    index_of_tows = TOWERS.index(tower_list)
    index_of_tow = board_out.index(tower_list)
    print(index_of_tows)

    attackable, next_pos = straight_movement(tower_str, tower_list)

    #Choose which one  
    choice = (input(f"A-ttack {attackable} \nor M-ove {next_pos} \n"))    
    if choice == "a" and len(attackable) != 0:
        choice = int(input(f"Which one:\n{attackable} ")) - 1
        next_pos = attackable[choice]
        
    else:
        choice = int(input(f"Which one:\n{next_pos} \n")) - 1
        next_pos = next_pos[choice]
    
    #Transformation    
    board_out[index_of_tow] = ["__"]
    x = 0
    pos_list = [[]]
    while True:
        if x == 1:
            break
        for i in range(7):
            z = next_pos - (56 - (i*8))
            zz = 8 - i + 1
            if z >= 0:
                tower_str = COLS[z] + str(zz)
                
                x = 1
                break
            else:
                pass
    #Setting TOWERS, boardout, making postition from number (35 to d4)
    pos_list[0] = tower_str
    TOWERS[index_of_tows] = pos_list
    board_out[next_pos] = pos_list   
    return pos_list
        
def horse_movement():
    horse_pos = 0 # int(input(f"Which one:\n{HORSES}")) - 1 #0
    horse_str = str(HORSES[horse_pos]) 
    horse_str = horse_str[2] + horse_str[3]
    
    #Possible movement
    x = chr(ord(horse_str[0]) - 2)
    y = int(horse_str[1]) + 1
    
    pos_list = []
    for i in range(2):
        if i == 1:
            y = int(y[1])
        st1 = x + str(y - i*2) #b6
        st2 = chr(ord(x) + 1) + str((y + 1) - (4*i)) #c7
        st3 = chr(ord(x) + 3) + str((y + 1) - 4*i) #e7
        st4 = chr(ord(x) + 4) + str(y - 2*i)     #f6
        st_list = [st1, st2, st3, st4]
        for y in st_list:
            if y[0] in "abcdefgh" and 0 < int(y[1]) < 9 and len(y) == 2:
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
    timed_string = int(str(pos_list)[3])
    choice = 0 # int(input(f"int-Choose which one {pos_list}")) - 1 #
    pos_list = pos_list[choice]
    board_out[COLS.index(pos_list[0]) + ((8 - timed_string) *8)] = ["__"]        
    pos_list2 = [[]]
    pos_list2[0] = pos_list
    HORSES[horse_pos] = pos_list2
    return pos_list2

    # return

def bishop_movement():
    choice = 0# int(input(f"Which one bishop?\n{BISHOPS}") - 1) #
    bish_to_move = str(BISHOPS[choice])[2:4]
    bish_index_in_board = board_out.index(BISHOPS[choice])
    #Check for valid move  
    pos_list = diagonal_movement(bish_to_move)
    
    #Choose next pos
    choose =  int(input(f"Choose next position {pos_list}\n")) - 1 # 0 #
    pos_list = [pos_list[choose]]
    board_out[bish_index_in_board] = ["__"]
    BISHOPS[choice] = pos_list
    return pos_list

def queen_movement():
    queen_as_str = str(ROYALS[0])[2:4]
    q_index_as_board = board_out.index(ROYALS[0])
    index_in_queens = 0

    first_list, fourth_list = diagonal_movement(queen_as_str)
    second_list, third_list = straight_movement(queen_as_str)   

    third_list = fourth_list[:] + third_list[:]
    first_list = first_list[:] + second_list[:] 
    #Choose which one
    choice = choose_a_choice(first_list, third_list)

    
    #Transformation    
    pos_list = [choice]
    return pos_list, q_index_as_board, index_in_queens 

def king_movement():
    king_as_str = str(ROYALS[1])[2:4]

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
    
    
    #return 
    

def straight_movement(fig):
    fig_str = fig
    #Possible boxes for move
    next_pos = []
    attackable = []       
    for i in range(4):        
        x = 1
        if i == 0: #Values for heading
            y, z = 0, 1
        elif i == 1:
            y, z = 1, 0
        elif i == 2:
            y, z = 0,-1
        else:
            y, z = -1,0
        while True:
            next_string = chr(ord(fig_str[0]) + y*x) + str(int(fig_str[1]) + z*x)  
            x += 1
            if 96 < ord(next_string[0]) < 105 and 0 < int(next_string[1]) < 9:
                ind_of_str = COLS.index(next_string[0]) + ((8 - int(next_string[1])) * 8)
                if [next_string] in board_out:
                    break
                if len(board_out[ind_of_str]) == "3aa":
                    attackable.append(next) 
                    break
                elif board_out[ind_of_str] == ["__"]:
                    next_pos.append(next_string)
                else:
                    break
            else:
                break
    return next_pos, attackable

def choose_a_choice(move, attack):
    movee = move[:]
    attackk = attack[:]
    while True:
        if len(movee) == 0:
            type_of_move = "a" 
            print("You can only attack")   
        elif len(attack) == 0:
            type_of_move = "m"
            print("You can only move") 
        else:
            type_of_move = input(f"str-Attack: {attackk}\n or Move{movee} ").lower()
        if type_of_move == "m":
            choosen_list = movee[:]
        elif type_of_move == "a":
            choosen_list = attackk[:]
        choice = choosen_list[int(input(f"int-Choose where to go\n{choosen_list}\n--> ")) - 1]
        break
    print(f"You have choosen --> {choice} <--")
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
                if [next_string] in board_out:
                    break
                if len(board_out[ind_of_str]) == "3aa":
                    attackable.append(next) 
                    break
                elif board_out[ind_of_str] == ["__"]:
                    next_pos.append(next_string)
                else:
                    break
            else:
                break
    return next_pos, attackable

#Initialisation
if __name__ == "__main__":
    board_out = creation_of_field()
    while True:      
        fig =  (input("str-Which figure do you want to move: P-awn, T-ower, H-orse, B-ishop, Q-ueen, K-ing" + "\n")) # "t" # 
        fig = fig.lower()    

        if fig == "p":                         
            pos_list = pawn_movement()   
            figure_movement(fig, pos_list) 
        elif fig == "t":
            pos_list = tower_movement()
        elif fig == "h":
            pos_list = horse_movement()
        elif fig == "b":
            pos_list = bishop_movement()
        elif fig == "q":
            pos_list, old_index, fig_index = queen_movement()
        elif fig == "k":
            pos_list = king_movement()
        else:
            print("Either wrong input or E")
            break

        figure_movement(fig, pos_list, old_index, fig_index)        
        (current_board(board_out))

