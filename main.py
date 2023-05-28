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
        for i in figs:
            fig_to_be_added = str(i)
            coors = COLS.index(fig_to_be_added[2]) + ((8 - int(fig_to_be_added[3]))*8)
            board_in[coors] = i


def figure_movement(choice, num):
    fig, num = choice, num
    if fig == "p":
        print(ord("a"))

    


#pc init
#Initialisation
board_out, all_figs = creation_of_field()
print(current_board(board_out))
figure_movement("p", "a2")