# Chess - mordor edition
a. **Project title**  
b. **Project description**  
c. **Code structure explanation**  
d. **Known issues**

___
**A.**   
Basic chess :)  
**B.**   
After launch user gets to control upper part of board and can choose if he wants to play against basic AI, random. Or against another player. Structure of functions starts from clik-pos to pygame window. After that position is transformed into string of letter and number according to clicked position. Another step is choosing figure and new position for movement.  
**C.**   
### get_clicked_coords_(poss, m_p)  
*input*  
_poss_ - contains tuple of clicked coordinates.  
_m_p_ - list of current player figures  
code - transformation of poss into string type of letter-number with check of correct position. Transformation if written into _strng_ variable. _strng_ is made into list that is being iterated through double loop of m_p variable. Here is found indx var, that contains index of figure.
returns - indx(int), strng(list), cor_val(boolean)

### creation_of_field
*input* - None  
code - creates text version, where is written text version of playboard. This board is used for memorizing all figures.
returns *board_in*(list in list)

### current_board  
*input* - board_out  
code - Takes 1 row of lists and rewrites it into 8x8 grid.  
returns - nicely written version of board. Not in 1 row but in 8.  

### figure_transformation  
*input* - board_in, given_list  
code - during first run this initializes figures into board_out. Meaning all figures are written into empty board list.  

### figure_movement  
*input* - choice, numm, indx, fg_indx, cr  
code - *choice* var gives information about type of figure.(pawn,bishop..) Removing old position and writing a new one after movement. From *num*, which is new position, is made *new_index*, which is new position in board_out. *index* is index of old position, that is rewriten into empty ["__"]    
returns - Updated board_out

### ,,**name of figure**,,_movement
This function is made in same principle, where is given actual position of figure. From this var, it is found possible movement/attack.   
*input* - *cor* - list of current position
returns - choice (list of new position), old_index (old index, from which old position is removed)

### straight_movement
*input* - *fig*
code - universal function for tower, queen, chess checker, king where are found all possible movement, attack positions in straight line.  
returns - next_post (list of all possible move positions), attackable (list of all possible attack movements)  

### choose_a_choice  
*input* - move, attack, cur_pos
code - from given lists it asks user for wished position. Also posible choice of canceling chosen figure without change of round.  
returns - choice (list of new position)
 
### diagonal_movement   
same as straight_movement but with difference of diagonal type.  

### current_player   
input - round  
Main lists of fig positions *all_figs_in*, *sec_team_all_figs* are retransforming into lists of main_player, enemy_player. These lists are important in later part of code.   

### game_init   
input - figg, cor, c_r, pv_p_e   
code - From *figg* code decides which type of figure is choosen for movement. *cor* gives position of choosen figure. *c_r* gives current round from which it is decided which player is currently on move. *pv_p_e* gives information if player choosed pvp or pve. 
returns - if everything is given with good condition, figure_movement is called. If not pos_list is returned as number. In this case round is not changed and repeats.    

### paint_figures  
From given list and picture, picture is drawn into window.   
   
maincycle 
just magic :D 