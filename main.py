COLS = ["a", "b", "c", "d","e", "f", "g", "h"]
PAWNS = [["a3"], ["b2"], ["c2"], ["d2"], ["e2"], ["f2"], ["g2"], ["h2"]]
TOWERS = [["a1"], ["h1"]]
HORSES = [["b1"], ["g1"]]
BISHOPS = [["c1"], ["f1"]]
ROYALS = [["d1"], ["e1"]]
        
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
                    # A0  B1  C2  D3  E4  F5  G6  H7    
                    # 97  98  99  100  101 102 103 104
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

def figure_transformation(board_in, given_list, set=None):
    figs = given_list[:]
    x = set
    if x == 1:
        for i in figs:
            #print(i)
            for y in i:
                fig_to_be_added = str(y)
                coors = COLS.index(fig_to_be_added[2]) + ((8 - int(fig_to_be_added[3]))*8)
                board_in[coors] = y

                
    else:
        h_list = [[]]
        for i in figs:
            z = 0
            if i[0] == '"':
               z = 0
            if i[0] in "abcdefgh": 
               z = 2
            fig_to_be_added = str(i)            
            coors = COLS.index(fig_to_be_added[2-z]) + ((8 - int(fig_to_be_added[3-z]))*8)
            if z == 2:
                h_list[0] = i
                board_in[coors] = h_list
            else:
                board_in[coors] = i

def figure_movement(choice, num):
    fig, num = choice, num
    num_string = str(num)
    str_1 = num_string[2][0][0]
    str_2 = num_string[3][0][0]
    ret_list = [[]]
    if fig == "p":
        new_num = str_1 + str_2         
        ret_list[0] = new_num
        figure_transformation(board_out, ret_list)
        pass

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
    #if friendly in way
    #if attack is possible
    return pos_list


#Initialisation
if __name__ == "__main__":
    board_out = creation_of_field()
    while True:      
        fig =  (input("str-Which figure do you want to move: P - awn " + "\n")) # "p" #
        fig = fig.lower()    

        if fig == "p":                         
            pos_list = pawn_movement()   
        elif fig == "t":
            pos_list = tower_movement()
        elif fig == "q":
            break
        figure_movement(fig, pos_list)         
        (current_board(board_out))

