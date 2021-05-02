# 265158_PyProject

# Project Information

* In this project we are making a Tic-Tac Toe game which can be played by two person.

* There is no change in the rules of the game. No new rule is added or removed.

* The person who make 3 (same symbol) either " X " or " O " wins.

* we have presented the initial state of the game which shows the numbers and these 
    numbers are actual positions in the game (1 to 9) and only these numbers should 
    be entered by the user. Inputs other than 1 to 9  is considered invalid input and 
    person is asked to input again.
                        
                                |     |     |     |
                                |  1  |  2  |  3  |
                                |_____|_____|_____|
                                |     |     |     |
                                |  4  |  5  |  6  |         <<===== State Showing the position and value which is to be used 
                                |_____|_____|_____|                 while playing this game.
                                |     |     |     |
                                |  7  |  8  |  9  |
                                |     |     |     |


                                |     |     |     |
                                |  .  |  .  |  .  |
                                |_____|_____|_____|
                                |     |     |     |
                                |  .  |  .  |  .  |         <<===== Initial State. Where " . " is showing empty positions 
                                |_____|_____|_____|                 ( Here all positions are empty now )
                                |     |     |     |
                                |  .  |  .  |  .  |
                                |     |     |     |
                                
                                
                                |     |     |     |
                                |  .  |  X  |  O  |
                                |_____|_____|_____|
                                |     |     |     |
                                |  X  |  .  |  .  |         <<===== State Showing the when game is being played. 
                                |_____|_____|_____|                 " X " is for player 1 and " O " is for player 2 and " . " shows places to be filled.
                                |     |     |     |
                                |  O  |  O  |  X  |
                                |     |     |     |
                                
                                
* Once a person has placed the symbol in certain location then other same location can
    not be entered again If entered then it is also considered invalid input.

* After each entry the state of table is displayed.

* At last either of the two opponents wins or the match is tied.
