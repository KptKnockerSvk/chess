COLS = ["a", "b", "c", "d","e", "f", "g", "h"]
PAWNS = [["a2"], ["b2"], ["c2"], ["d2"], ["e2"], ["f2"], ["g2"], ["h2"]]
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
        new_num = str_1 + str(int(str_2) + 1)            
        ret_list[0] = new_num
        figure_transformation(board_out, ret_list)
        pass

def pawn_movement():
    pass



#Initialisation
if __name__ == "__main__":
    board_out = creation_of_field()
    while True:        
        #(current_board(board_out))

        fig = "p" #(input("str-Which figure do you want to move: P - awn " + "\n")) # 
        fig = fig.lower()
        if fig == "p":
            print("Your pawns are:\n", PAWNS,"\n")
            pos = "h2" # input("str-Which one: ") #
            pos_list = [[]]
            while True:
                if int(pos[1]) == 2:
                    double_step = 1 #int(input("1 or 2 ")) - 1 #
                else:
                    double_step = 0
                pos_list[0] = pos
                pos_index = PAWNS.index(pos_list)
                board_out[8 * (8 - int(pos[1])) + pos_index] = ["__"]
                PAWNS[pos_index] = pos[0] + str(int(pos[1]) + 1 + double_step)
                pos_list[0] = pos[0] + str(int(pos[1]) + double_step)
                break
            
            
        
        figure_movement(fig, pos_list)         
        (current_board(board_out))
        break
