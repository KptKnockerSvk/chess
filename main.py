COLS = ["a", "b", "c", "d","e", "f", "g", "h"]


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

    pawns = [["a2"], ["b2"], ["c2"], ["d2"], ["e2"], ["f2"], ["g2"], ["h2"]]
    towers = [["a1"], ["h1"]]
    horses = [["b1"], ["g1"]]
    bishops = [["c1"], ["f1"]]
    royals = [["d1"], ["e1"]]
    all_figs = [pawns, towers, horses, bishops, royals]
    figure_transformation(board_in, all_figs, 1)
    return board_in, all_figs



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



#Initialisation
if __name__ == "__main__":
    board_out, all_figs_in = creation_of_field()  
    all_figs = all_figs_in[:]  

    while True:        
        #(current_board(board_out))

        fig = "p" #(input("strWhich figure do you want to move: P - awn " + "\n"))
        fig = fig.lower()
        if fig == "p":
            pos = "d2" #input("strWhich one: " + str(all_figs[0]) + "\n")
            pos_list = [[]]
            pos_list[0] = pos
            pos_index = all_figs[0].index(pos_list)
            all_figs[0][3] = "__"
            print(all_figs)

        figure_movement(fig, pos_list) 
        (current_board(board_out))
        break
