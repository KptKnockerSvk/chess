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
        
   
    
    return board_in



def current_board(board_in):
    current_row = []
    for i in range(8):
        for y in range(8):
            current_row.append(board_in[y+i*8])
        print(str(current_row))
        current_row = []
    return "This is current board"

def pawn_setup(board_in):
    pawns = [["a2"], ["b2"], ["c2"], ["d2"], ["e2"], ["f2"], ["g2"], ["h2"]]
    for i in pawns:
        pawn_to_be_added = str(i)
        coors = COLS.index(pawn_to_be_added[2]) + (48)
        board_in[coors] = i


board_out = creation_of_field()
pawn_setup(board_out)
print(current_board(board_out))