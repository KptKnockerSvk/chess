COLS = ["a", "b", "c", "d","e", "f", "g", "h"]
PAWNS = [["a3"], ["b2"], ["c2"], ["d2"], ["e2"], ["f2"], ["g2"], ["h2"]]
TOWERS = [["d5"], ["h1"]]
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
    tower_str = 0 # int(input(f"int-Which one tower?: \n{TOWERS} \n--> ")) -1 #
    tower_str = str(TOWERS[tower_str])[2] + str(TOWERS[tower_str])[3]
    tower_list = [[]]
    tower_list[0] = tower_str

    #Possible boxes for move
    next_pos = []
    attackable = []
    index_of_tow = board_out.index(tower_list)    
    index_of_tows = TOWERS.index(tower_list)
    l1 = [8,-8]
    dic = {1:8, 2:-8, 3:1, 4:-1}
    x,y  = 1, 1
    f_num = (8 - int(tower_str[1])) * 8
    while x < 5:
        z = index_of_tow + dic[x] * y 
        y += 1       
        zz = dic[x]
        if zz in l1 and board_out[z] == ["__"]:
            next_pos.append(z)        
        elif zz not in l1:
            if z == (f_num-1) or z == (f_num+8):
                x += 1    
                y = 1  
            else:
                next_pos.append(z)                        
        else:            
            x += 1
            y = 1
            #if attack is possible
            if 0 < z < 63:
                attackable.append(z)

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
            zz = 8 - i -1
            if z > 0:
                tower_str = COLS[z] + str(zz)
                
                x = 1
                break
            else:
                pass
    #Setting TOWERS, boardout, making postition from number (35 to d4)
    pos_list[0] = tower_str
    TOWERS[index_of_tows] = pos_list
    board_out[next_pos] = pos_list   
    print(pos_list)
    return pos_list
        
def horse_movement():
    pass


#Initialisation
if __name__ == "__main__":
    board_out = creation_of_field()
    while True:      
        fig =  (input("str-Which figure do you want to move: P-awn, T-ower, H-orse " + "\n")) # "t" # 
        fig = fig.lower()    

        if fig == "p":                         
            pos_list = pawn_movement()   
        elif fig == "t":
            pos_list = tower_movement()
        elif fig == "h":
            pos_list = horse_movement()
        else:
            print("Either wrong input or Q")
            break
        figure_movement(fig, pos_list)         
        (current_board(board_out))

