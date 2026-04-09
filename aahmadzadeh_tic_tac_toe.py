#Author: Arman Ahmadzadeh
#Date: 2/20/2025
#Description: complete two or one player Tic-Tac-Toe game that runs in the terminal. 
#Uses lists, loops, conditionals, functions, and input validation 

import random

def board_size():
    '''
    Ask the user for the size of the board (3, 4, or 5).
    Validates if the input is 3, 4, or 5; re-prompts on invalid input without crashing.
    Args:
        none
    Returns:
        size (int): size of the board
    '''
    while True: #Loop until valid input is given
        try:    #Try except block to make sure input is integer
            size = int(input("Enter the size of the board (3, 4, or 5): ")) #aks user for board size and convert to integer
            if size in [3, 4, 5]:                                           #If the input is 3, 4 or 5 return the size
                return size
            else:                                                           #If not 3,4,5 ask again
                print("Invalid input. Please enter 3, 4, or 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def create_board(size):
    '''
    Create an board with empty cells based on given size
    Args:
        n (int): size of the board
    Returns:
        board (list of lists): cells of the game board

    '''
    board = []              #board begins as empty list
    for i in range(size):   #Loop through the given size
        row = [" "] * size  #Creates a row (list within list) of empty cells for the given size and adds it to board
        board.append(row)
    return board            #return list of lists representing the board


def find_winning_move(board, player):
    '''
    Find if winning move for X or O exists, returns the index if it does
    Args:
        board (list of lists): cells of the game board
        player (variable): x or o
    Returns:
        row, column(tuple): index of winning move or None
    '''
    n = len(board)                 #Get size of board
    for i in range(n):             #loop through rows
        for j in range(n):         #loop through columns
            if board[i][j] == " ": #if a cell is empty it is set to player (could be a win)
                board[i][j] = player
                if check_winner(board) == player: #check if this move wins
                    board[i][j] = " "             #reset the cell and return as tuple
                    return (i, j)                
                board[i][j] = " "
    return None                    #If there is no winning move return none

def ai_move(board, player):
    '''
    Implement a simple computer player that makes valid moves.
    computer makes a move by following this priority:
    1. Win immediately if possible
    2. Block opponent's immediate win
    3. Take the center if available
    4. Take a random available corner
    5. Take a random available cell
    Args:
        board (list of lists): cells of the game board
        player (variable): x or o
    Returns:
        board(list of lists): updated cells of the game board
    '''
    n = len(board)    #Get size of board

    if player == "X": #Figures out opponent
        opponent = "O"
    else:
        opponent = "X"

    # 1. win immediately if possible
    win_move = find_winning_move(board, player)
    if win_move: #if is found, make wining move and return board
        board[win_move[0]][win_move[1]] = player
        return board

    # 2. block opponent's immediate win
    block_move = find_winning_move(board, opponent)
    if block_move: #if opponent winning move found, take it and return board
        board[block_move[0]][block_move[1]] = player
        return board

    # 3. take the center
    if board[n//2][n//2] == " ": #Center is found by dividing size of rows and columns by 2
        board[n//2][n//2] = player #Take center and return board
        return board

    # 4. take random corner
    corners = [(0, 0), (0, n-1), (n-1, 0), (n-1, n-1)]  # List of corner cells as tuples (row, column)
    empty_corners = []

    for row, col in corners:                                     #Loops though corners                            
        if board[row][col] == " ":                               #If corner is empty
            empty_corners.append((row, col))                     #Add to list of empty corners

    if empty_corners:                                            #If empty corners found
        row, col = random.choice(empty_corners)                  #Choose a random empty corner by assigning index and take it, then return board
        board[row][col] = player
        return board

    # 5. random move
    empties = [] #empty list for empties
    for i in range(n): #Loop through rows and columns to find empty cells
        for j in range(n):
            if board[i][j] == " ":
                empties.append((i, j)) #Add empty cell index as tuple to list
    if empties: #If there are empty cells
        r,c = random.choice(empties) #Index of row and column equal to a random choice from list
        board[r][c] = player #Take the cell and return board
    return board

def format_ansi(cell):
    '''
    Format cell for ANSI color output
    Args:
        cell (str): "X", "O", or " "
    Returns:
        formatted_cell (str): ANSI formatted cell
    '''
    if cell == "X":
        return "\033[91mX\033[0m"  # Red X5
    elif cell == "O":
        return "\033[94mO\033[0m"  # Blue O
    else:
        return " "  # Empty cell

def board_display(board):
    '''
    Print the board in a user-friendly format.
    Board prints correctly after each move with row/column labels; formatting is clean and readable.
    Args:
        board (list of lists): cells of the game board
    Returns:
        none
    '''    

    #list_of_lists[row_index][column_index]

    n = len(board) #Get board size

    if n == 3: #If board is 3x3 print with this format
            print('\n')
            print("    1   2   3")
            print(f" 1  {format_ansi(board[0][0])} | {format_ansi(board[0][1])} | {format_ansi(board[0][2])}")
            print("   -----------")
            print(f" 2  {format_ansi(board[1][0])} | {format_ansi(board[1][1])} | {format_ansi(board[1][2])}")
            print("   -----------")
            print(f" 3  {format_ansi(board[2][0])} | {format_ansi(board[2][1])} | {format_ansi(board[2][2])}")
            print('\n')

    elif n == 4: #If board is 4x4 print with this format
            print('\n')
            print("    1   2   3   4")
            print(f" 1  {format_ansi(board[0][0])} | {format_ansi(board[0][1])} | {format_ansi(board[0][2])} | {format_ansi(board[0][3])}")
            print("   ---------------")
            print(f" 2  {format_ansi(board[1][0])} | {format_ansi(board[1][1])} | {format_ansi(board[1][2])} | {format_ansi(board[1][3])}")
            print("   ---------------")
            print(f" 3  {format_ansi(board[2][0])} | {format_ansi(board[2][1])} | {format_ansi(board[2][2])} | {format_ansi(board[2][3])}")
            print("   ---------------")
            print(f" 4  {format_ansi(board[3][0])} | {format_ansi(board[3][1])} | {format_ansi(board[3][2])} | {format_ansi(board[3][3])}")
            print('\n')

    else: #If board is 5x5 print with this format
            print('\n')
            print("    1   2   3   4   5")
            print(f" 1  {format_ansi(board[0][0])} | {format_ansi(board[0][1])} | {format_ansi(board[0][2])} | {format_ansi(board[0][3])} | {format_ansi(board[0][4])}")
            print("   -------------------")
            print(f" 2  {format_ansi(board[1][0])} | {format_ansi(board[1][1])} | {format_ansi(board[1][2])} | {format_ansi(board[1][3])} | {format_ansi(board[1][4])}")
            print("   -------------------")
            print(f" 3  {format_ansi(board[2][0])} | {format_ansi(board[2][1])} | {format_ansi(board[2][2])} | {format_ansi(board[2][3])} | {format_ansi(board[2][4])}")
            print("   -------------------")
            print(f" 4  {format_ansi(board[3][0])} | {format_ansi(board[3][1])} | {format_ansi(board[3][2])} | {format_ansi(board[3][3])} | {format_ansi(board[3][4])}")
            print("   -------------------")
            print(f" 5  {format_ansi(board[4][0])} | {format_ansi(board[4][1])} | {format_ansi(board[4][2])} | {format_ansi(board[4][3])} | {format_ansi(board[4][4])}")
            print('\n')



def player_move(board, player):
    '''
    Prompts correct player (X/O); validates input is in range
    and cell is empty; re-prompts on invalid input without
    crashing. Makes player move.
    Args:
        board (list of lists): cells of the game board
        player (variable): x or o
    Returns:
        board(list of lists): updated cells of the game board

    '''    

    n = len(board) #Get size of board

    while True: #Loop until valid input is given

        move = input(f"player {player}: enter row and column: ")
        try:
            row, column = move.split(",") #input is split into row and column

            row = int(row)        #Make sure they are integers
            column = int(column)    

        except ValueError:  
            print("Invalid input, please enter row and column separated by a comma")
            continue

        if row < 1 or row > n or column < 1 or column > n:           #checks range of row and column is withing board limits
            print(f"Invalid input, Row and/or column is out of range use 1 to {n}")
            continue

        row_index = row -1 #Remove 1 to get the correct index
        column_index = column -1  

        if board[row_index][column_index] != " ": #Checks id cell is empty
            print ("Invalid input, cell is full")
            continue

        break #If valid input given break out of loop

    board[row_index][column_index] = player #Take the cell and return board
    return board

def check_winner(board):
    '''
    Return X, O or none
    Correctly detects all winning combinations (rows, columns, diagonals);
    Announces the winning player.
    Args:
        board (list of lists): cells of the game board
    Returns:
        X, O, None (variable): Current Winner

    '''    
    n = len(board)  # Get size of board
   
    # Rows check
    for i in range(n):                         #Loop though each row
        if board[i][0] != " ":                 #If first cell in row isn't empty
            win = True                         #Assume its a win until disproved
            for j in range(1, n):              #Loop though the other cells after the first
                if board[i][j] != board[i][0]: #If any of these cells dose not match the first
                    win = False                #win disproved so break out of loop
                    break
            if win:
                return board[i][0]  # Return the winner
   
    # Columns check
    #Same checks as rows but with i and j switch to loop through columns instead of rows
    for i in range(n):
        if board[0][i] != " ":  
            win = True
            for j in range(1, n):
                if board[j][i] != board[0][i]:
                    win = False
                    break
            if win:
                return board[0][i]  
   
    # Diagonal 1 check (top-left to bottom-right)
    if board[0][0] != " ":                  #If top left cell isn't empty
        win = True                          #Assume its a diagonal win until disproved
        for i in range(1, n):               #Loop through the diagonal cells after the first
            if board[i][i] != board[0][0]:  #If any dont match the first
                win = False                 #Disprove win and break
                break
        if win:
            return board[0][0]  #Return the winner
   
    # Diagonal 2 check (top-right to bottom-left)
    #Same checks as diagonal 1 but with different index
    if board[0][n-1] != " ":      #n - 1 is the index of top right cell
        win = True
        for i in range(1, n):
            if board[i][n-1-i] != board[0][n-1]: #n - 1 - i is the index of the diagonals after teh first
                win = False
                break
        if win:
            return board[0][n-1]  # Return the winner
   
    return None  #If all checks fail, no winner found so return none


def is_draw(board):
    '''
    Return true if the board is full with no winner
    Correctly identifies a draw when all cells are filled with
    no winner.
    Args:
        board (list of lists): cells of the game board
    Returns:
        sorted_dict (dict):
    '''    
    n = len(board) #Get size of board
    if check_winner(board) == None:       #If theres no winner
        for i in range(n):                #Loop though rows and columns
            for j in range(n):
                if board[i][j] == " ":    #If there is an empty cell return false because its not a draw
                    return False
        return True                       #If there are no empty cells and no winner, it is a draw
   
def play_game():
    '''
    Run one complete game of Tic-Tac-Toe.
    determines who goes first 
    Ask for 1 or 2 player mode
    implement the game loop
    Use a while True loop for the main game loop; break out of it when someone wins or the
    game is a draw.
    Game alternates turns properly; ends on win or draw;
    offers replay option.
    '''    

    size = board_size() #Gets the board size

    #asks user for game mode and if single player (AI), asks for X or O for computer, and if none given defaults to O
    mode = input("Enter 1 for single player, 2 for two player: ").strip()
    machine_player = None          
    if mode == "1":  
        machine_player = input("Enter X or O for machine player: ").strip().upper()
        if machine_player not in ["X", "O"]:
            print("Invalid input, defaulting to O")
            machine_player = "O"
       
    board = create_board(size) #Creates the board based on the given size
    players = ["X", "O"]
    current_player = 0
    X_score = 0
    O_score = 0

    while True:                      #Game loop that breaks when player quits
        board_display(board)         #Displays the empty board at the game start
        while True:                  #Loop for each player turn that breaks when game ends
            if machine_player == players[current_player]:                     #If its machine's turn
                print(f"Machine player {machine_player} is making a move...")
                board = ai_move(board, machine_player)                        #Make move for machine
            else:
                board = player_move(board, players[current_player])           #Otherwise as player for move
            board_display(board)                                              #After move is made show board
            if check_winner(board) == players[current_player]:                #If there is a winner set variable and exit loop
                winner = players[current_player]
                break
            elif is_draw(board):                                              #if there is a draw set winner to non and exit loop
                winner = None
                break

            current_player = 1 - current_player                               #Switch player

        if winner != None: #If there is a winner, print winner and update score
            print(f"Winner is {winner}")
            if winner == "X":
                X_score += 1
            else:
                O_score += 1
        else:
            print("winner is none, DRAW")
            print("A perfect game will always draw")

        print(f"SCORE X: {X_score} O: {O_score}")

        #Ask if player wants to go again, if not break loop, otherwise reset board and start new game
        again = input("Press enter to play again or type 'q' to quit: ").strip().lower()
        if again == "q":
            break

        board = create_board(size) #Reset board for new game
        current_player = 0 #Reset player to X for new game (in tic tac toe X always goes first)

play_game()





