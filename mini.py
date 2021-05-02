"""*******************************************************************
    THIS IS TIC TAC TOE GAME PROGRAME WHICH IS PLAYED BY 2 USER
    THIS PROGRAM INITIALLY DISPLAYS THE BOARD POSITION WITH NUMBERS
    WHICH SHOWS THE POSITION NUMBER AND THOSE SHOWN NUMBERS ARE THE
    ONLY VALID POSITION TO BE ENTERED BY THE USER. 
    THIS GAME FOLLOWS ALL THE RULES OF REAL TIC TAC TOE GAME. NO RULES
    ARE EXEMPTED OR NO NEW RULES IS INTRODUCED.

    ------------------------- BEST OF LUCK ------------------------- 
 ********************************************************************"""

square = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']


"""/*********************************************

THIS FUNCTION RETURNS THE STATUS OF THE GAME 
------  1 WHEN SOMEONE HAS WON
------ -1 WHEN GAME IS STILL IN PROGRESS
------  O WHEN THE GAME IS OVER WITHOUT ANY RESULT
 **********************************************/"""

def wincheck():
    count=0
    if(square[1]=='O' or square[1]=='X'):
        #print(square[1])
        if (square[1] == square[2] and square[2] == square[3]):
            #print(square[1])
            return 1
        elif (square[1] == square[4] and square[4] == square[7]):
          #  print(square[1])
            return 1
        elif (square[1] == square[5] and square[5] == square[9]):
            print(square[1])
            return 1

    if(square[2]=='O' or square[2]=='X'):
        if (square[2] == square[5] and square[5] == square[8]):
            return 1

    if(square[3]=='O' or square[3]=='X'):
        if (square[3] == square[6] and square[6] == square[9]):
            return 1
     
        elif (square[3] == square[5] and square[5] == square[7]):
            return 1

    if(square[4]=='O' or square[4]=='X'):
        if (square[4] == square[5] and square[5] == square[6]):
            return 1
    

    if(square[7]=='O' or square[7]=='X'):  
        if (square[7] == square[8] and square[8] == square[9]):
            return 1
    
   
    for i in range(1, 10):
        if(square[i]=='.'):
            break;
        count+=1
    if(count == 9):
        return 0
    else:
        return  -1

"""/*******************************************************************
    THIS FUNCTION WILL DROW THE BOARD POSITION AFTER EACH SUCCESSFUL
    ENTRY BY THE USER
 ********************************************************************/"""

def board():
    print("\n\n\tTic Tac Toe\n\n");

    print("Player 1 (X)  -  Player 2 (O)\n\n\n");


    print("     |     |     \n");
    print(" ",square[1]," | ",  square[2]," | ", square[3]," \n");

    print("_____|_____|_____\n");
    print("     |     |     \n");

    print(" ",square[4]," | ",  square[5]," | ", square[6]," \n");

    print("_____|_____|_____\n");
    print("     |     |     \n");

    print(" ",square[7]," | ",  square[8]," | ", square[9]," \n");

    print("     |     |     \n\n");




"""/*******************************************************************
    THIS FUNCTION WILL DROW THE INITIAL BOARD POSITION AND SHOWS THE
    BOARD NUMBER WHICH IS ACTUAL VALID POSITION NUMBER WHICH WILL BE
    ENTERED BY THE PLAYER
 ********************************************************************/"""

def initial_board_position():
    print("\n\n\tTic Tac Toe\n\n");

    print("Player 1 (X)  -  Player 2 (O)\n\n\n");


    print("     |     |     \n");
    print("  1  |  2  |  3 \n");

    print("_____|_____|_____\n");
    print("     |     |     \n");

    print("  4  |  5  |  6 \n");

    print("_____|_____|_____\n");
    print("     |     |     \n");

    print("  7  |  8  |  9 \n");
    print("     |     |     \n\n");





player = 1
win_chance=-1
choice = 0;
initial_board_position()

while(win_chance == -1):
    board();
    player = 1 if(player % 2) else 2;
    print("Player ",player," enter position number:  ", end="")
    choice = int(input())

    mark = 'X' if(player == 1) else 'O';
        
    if(choice<10 and choice>0 and square[choice]=='.'):
        square[choice] = mark

    else:
        print("Invalid move ")
        player-=1

    win_chance = wincheck()
    player+=1
    
board();
    
if (win_chance == 1):
    player-=1
    print("==>\aPlayer " , player , " win ");
else:
    print("==>\aGame draw");

