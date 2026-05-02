#Author: Arman Ahmadzadeh
#Date: 5/4/2026
#Description: 
# Complete classic single player Battleship game where you go 
# against the computer. The player and computer hide a fleet of ships on
# a grid, and take turns attacking coordinates in order to
# sink the enemies's fleet first.
#https://www.w3schools.com/python/ref_module_time.asp
#https://www.geeksforgeeks.org/python/clear-screen-python/
#https://www.geeksforgeeks.org/python/string-alignment-in-python-f-string/

import random   #Used for random ship placement and random shots
import os       #Used to clear the terminal screen for cleaner game feel
import time     # used for short pauses in the game after each hit to display messages

#Global emoji variables for printing the board, not necessary but helpful for not having to copy/paste all these emojis 
WATER     = "🟦"   # ocean cell not yet hit
SHIP      = "🟩"   # safe ship cell
HIT       = "💥"   # attacked but not sunk ship cell
MISS      = "🔵"   # missed hit cell
SUNK      = "💀"   # sunken ship cell
LAST_HIT  = "🔥"   # Most recent hit cell
LAST_MISS = "🌊"   # Most recent miss cell

def clear_screen():
    """
    At the start of each turn this function clears the terminal using os.system function 
    If on Windows (nt) will use "cls" command to clear otherwise for MacOS or Linux will use "clear"
    """
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    """
    Prints the big title banner at the top of the screen during each turn to make it feel more like a game
    """
    print("=============================================")
    print("    🚢  ⚓  B A T T L E S H I P  ⚓  🚢")
    print("  🌊  THE  CLASSIC  NAVAL  COMBAT  GAME 🌊  ")
    print("=============================================")


def pause(message):
    """
    Using input pauses the game until player presses enter
    Used after each turn to ensure player controls game pace
    """
    print("\n")
    input(f"{message}")


def board_size():
    """
    Asks the player how big they want the battlefield.
    validates input using while true and try/except 
    Returns:
        size (int): battlefield size
    """
    while True:
        try:
            size = int(input("\n⚓ Enter BATTLEFIELD SIZE (minimum 6): ")) #asks for size as int
            if size >= 6:     #If input is greater than or equal to 6 return
                return size
            print("🚫 The theatre of war must be at least 6 wide.") #Else display error message
        except ValueError:     
            #If value error (not a number) display error message
            print("🚫 Invalid input. Please enter a number.")

def create_board(size):
    """
    Builds the board based on size
    Water emojis used as empty space
    Board is a list of rows, where each row is a list of cells
    Args:
        size (int): board size
    Returns:
        board (list of lists): board 
    """
    board = []              #board begins as empty list
    for i in range(size):   #Loop through the given size
        row = [f"{WATER}"] * size  #Creates a row (list within list) of empty cells for the given size and adds it to board
        board.append(row)
    return board            #return list of lists representing the board

def print_single_board(board, title, last_shot=None, fleet=None):
    """
    Prints one board in the terminal with a title above it
    This function works for the boards in the board list
    We will use it for the players hidden board and the machines visible board 
    Args:
        board (list of lists): game board grid
        title (str): the heading above board
        last_shot (tuple): row, col of the most recent shot on the board will be highlighted with 🔥 or 💧
        fleet (list): list of ships coordinates for status bar of 🚢 (alive) vs 💀 (sunk)
    """
    n = len(board) #Get the board size 
    #Fleet status bar only is printed if fleet list passed in, so when the player is positioning ships there will be no status bar
    if fleet is not None: #If fleet passed in 
        status = "".join("💀" if ship["sunk"] else "🚢" for ship in fleet) #status string is 💀 for sunken or 🚢 for working ship joined together without space
        print(f"\n⚔️  {title}   FLEET: {status}")  #Print status bar with title (player or machine) and fleet status from above
    else:
        print(f"\n⚔️  {title}") #If we are using during ship positioning just print title
    #Print statement for the column header/label
    #First print 5 spaces to line up with board
    #Join everything from the f string without spaces
    #Inside the f string loop through the length of the board
    #for each int in the length add 1 to acount for index, then left align and set width to 3 chars including that index
    print("     " + "".join(f"{j+1:<3}" for j in range(n)))
    #Code below is for the board grid
    for i in range(n): #for rows in the board size 
        row_cells = [] #create list for rows
        for j in range(n): #for columns in the board size
            cell = board[i][j] #define the cell
            #Check if there is a last shot (not = none), and then have the coordinate set equal to this last shot
            if last_shot is not None and (i, j) == last_shot:
                if cell == HIT or cell == SUNK: #Now for the last shot check if the cell is a hit or sunken cell and set it equal to 🔥
                    cell = LAST_HIT
                elif cell == MISS:              #If the cell is a miss have it equal to 💧
                    cell = LAST_MISS
            row_cells.append(cell + " ") #Have the cell added to the list of row cells but with a extra space
        #Print the row label (+1 for index) right aligned with all of the looped through cells joined with no space afterwards
        print(f" {i+1:>2}  " + "".join(row_cells))


def print_boards(boards, stats, fleet_player, fleet_machine,
                 last_player_shot, last_computer_shot):
    """
    This function prints both boards together with the stats line
    It uses the above function for the actual printing
    It is used before every turn to refresh player with the current boards
    Args:
        boards (list): list of game boards 
        stats (dict): dictionary of game stats
        fleet_player (list): list of ships dictionaries
        fleet_machine (list): list of ships dictionaries
        last_player_shot (tuple): row, col of the most recent player shot 
        last_computer_shot (tuple): row, col of the most recent computer shot
    """
    #Take out values from dict for easier referencing 
    turn   = stats["turn"]
    p_shot = stats["player_shots"]
    p_hit  = stats["player_hits"]
    c_shot = stats["computer_shots"]
    c_hit  = stats["computer_hits"]

    #Calculate accuracy by dividing hits by shots, if shots are greater than 0 then have calculation be 0 to avoid division error 
    p_acc = (p_hit * 100 // p_shot) if p_shot > 0 else 0
    c_acc = (c_hit * 100 // c_shot) if c_shot > 0 else 0

    #F string for displaying stats
    print(f"\n⚔️  TURN {turn}   │   YOUR ACCURACY: {p_acc}% ({p_hit}/{p_shot})"
          f"   │   ENEMY ACCURACY: {c_acc}% ({c_hit}/{c_shot})")

    # pass boards[0] (players real board), title, last computer shot, and player fleet into print single board function
    # pass boards[2] (computers "fake" board), title, last player shot, and computer fleet into print single board function
    print_single_board(boards[0], "YOUR WATERS",          last_computer_shot, fleet_player)
    print_single_board(boards[2], "ENEMY WATERS (RADAR)", last_player_shot,   fleet_machine)
    print()


def place_ship_player(board, ship_name, ship_size, n):
    """
    Handles the player manually placing a single ship.
    Returns a list of (row, col) coordinates the ship occupies,
    or None if the player typed 'R' to auto-place the rest.
    Args:
        board (list of lists): players real board grid
        ship_name (str): description
        ship_size (int): size of ship
        n (int): length of board
    Returns:
        coords (list): tuples representing the cells ocupyed by the given ship
    """
    #while true loop to validate players input
    while True:        
        coord = input(f"📍 Deploy {ship_name} [{ship_size} cells] — coordinate (row,column) "
                      f"or 'R' to auto-deploy the rest of the fleet: ").strip().lower()
        #Ask the user to deploy ship to starting cell telling them its size

        #If user selects r, return none, the next function will handle this 
        if coord == "r":
            return None

        # Parse coord into tuple of row, column as ints, also subtract 1 to acount for index within try except block
        try:
            row, col = coord.split(",")
            row = int(row) - 1
            col = int(col) - 1
        except ValueError:
            print("🚫 Invalid coordinate. Format: row,column (e.g. 3,5)")
            continue #continue if invalid 

        #Ask for ship direction
        orientation = input("🧭 HORIZONTAL or VERTICAL (h/v): ").strip().lower()
        if orientation not in ("h", "v"): #quick check using tuple to validate input and continue if invalid
            print("🚫 Invalid bearing. Use 'h' or 'v'.")
            continue

        # Build the list of cells that the ship will take 
        coords = []
        #loop through the ship size
        for i in range(ship_size):
            if orientation == "h":             #if horizontal
                coords.append((row, col + i))  #append to coords list by adding i to the col index
            else:                              #else vertical 
                coords.append((row + i, col))  #append to coords list by adding i to the row index

        #Validate coords list, begin with setting valid as true until disproved 
        valid = True
        for (r, c) in coords:                      #For each row and column in the proposed ship spots
            if r < 0 or r >= n or c < 0 or c >= n: #If the row is less than 0, row is greater than or equal to the board size--- 
                valid = False                      #column is less than 0, or column is greater than or equal to the board size
                break                              #Out of board range so break with valid proved false 
            if board[r][c] == SHIP:                #If a ship coord overlaps with another ship (in a ship spot)
                valid = False                      #Valid disproved and break 
                break

        if not valid: #If valid has been disproved print message and restart loop
            print("🚫 Cannot deploy there (out of range or overlapping another vessel).")
            continue

        #If none of these checks find anything invalid, loop through the tuples in the coords list and turn each into a safe ship and return list 
        for (r, c) in coords:
            board[r][c] = SHIP
        return coords


def place_ship_random(board, ship_size, n):
    """
    Randomly places a ship on the board (used for the computer's
    fleet, and for auto-placing the player's fleet if they choose 'R').
    Keeps trying new random spots until it finds one that fits.
    Args:
        board (list of lists): the battlefield grid for machine or player 
        ship_size (int): the size as an int of the given ship
        n (board size): the board size 
    Returns:
        coords (list): list of tuples that the ship will occupy 
    """
    #While true loop for validation 
    while True:
        orientation = random.choice(["h", "v"]) #Randomly select horizontal or vertical 
        if orientation == "h":                  #if horizontal 
            row = random.randint(0, n - 1)      #Row is random choice from index 0 to n (subtract 1 to adjust)
            col = random.randint(0, n - ship_size) #Col is random choice from index 0 to n (subtract ships' size to adjust)
        else:                                   #if vertical 
            row = random.randint(0, n - ship_size) #Row is random choice from index 0 to n (subtract ship's size to adjust)
            col = random.randint(0, n - 1)      #Row is random choice from index 0 to n (subtract 1 to adjust)

        coords = []                             #Create coords list
        for i in range(ship_size):              #Loop through the ship size 
            if orientation == "h":              #If the ship is going horizontal
                coords.append((row, col + i))   #take the random row and col and add to the list, add i to column to build the ship "down"
            else:                               #If the ship is going vertical
                coords.append((row + i, col))   #take the random row and col and add to the list, add i to row to build the ship "right" facing

        valid = True                            #Assumes the coords are valid
        for (r, c) in coords:                   #Loop through each
            if board[r][c] == SHIP:             #If any is already ship
                valid = False                   #Overlap so valid is false and break
                break
        if not valid:                           #If invalid start again to try a new random position 
            continue   

        for (r, c) in coords:            #If everything is good, loop through r, c and have each index r, c set equal to a ship spot
            board[r][c] = SHIP
        return coords                    #Return the ship coords list


def choose_ships(boards):
    """
    Guides the player through deploying ships and then
    automatically deploys the computer's fleet.
    Returns the boards and with each side's fleets coordinates
    Args:
        boards (list): list of all 4 boards
    Returns:
        boards (list): list of all 4 boards
        fleet_player (list): list of ship dictionaries 
        fleet_machine (list): list of ship dictionaries 
    """
    n = len(boards[0])           #take the board size
    player_board   = boards[0]   #set real player board 
    computer_board = boards[1]   #set real computer board 

    #List of tuples with ship name and size from classic battleship game 
    all_ships = [
        ("AIRCRAFT CARRIER", 5),
        ("BATTLESHIP",       4),
        ("CRUISER",          3),
        ("SUBMARINE",        3),
        ("DESTROYER",        2),
    ]

    #No more than 1/3 of the board can have a ship to keep game playable

    max_cells = (n * n) // 3                  #The max cells allowed for ships is the board size (n x n) divided by 3
    allowed_ships = []                        #Empty list
    total = 0                                 #Current total ship cells starts at 0 
    for name, size in all_ships:              #loop through the name & size of each ship type 
        if total + size <= max_cells:         #If the total cells + the size of the current ship is less than the max allowed (should be)
            allowed_ships.append((name, size))#add this allowed ship into the list
            total += size                     #add the current ships size to the total

    print(f"\n🌊 Battlefield: {n}×{n}. Fleet authorized: {len(allowed_ships)} vessels.") #display message with the length of the allowed ships list 
    print("⚓ Commander, deploy your FLEET!  (type 'R' at any prompt to auto-deploy)\n")
    print_single_board(player_board, "YOUR WATERS")                #prints a single board with a title (player's real board)

    #These 2 lists will have dicts for every ship cell, key value pairs for the ship cell name, coordinate, and status 
    fleet_player  = []  
    fleet_machine = []    

    auto = False        #It will be true if player chooses r 
    index = 0           
    while index < len(allowed_ships):    #While the current index is less than the amount of ships allowed
        name, size = allowed_ships[index]#name and size are the index of an allowed ship
        if auto:                         #player choose auto
            coords = place_ship_random(player_board, size, n) #have coords = to the random place function called with the player board, size, and n 
            print(f"🎲 {name} auto-deployed.")                #print which ship has just deployed 
        else:                                                  #if manual 
            coords = place_ship_player(player_board, name, size, n) #call manual ship placement function with board, name, size and n, and have result = to coords
            if coords is None:                                      #If  coords is none
                print("🎲 Auto-deploying the remaining fleet...")   #Player chose R so switch mode by setting auto to true and continue while loop
                auto = True
                continue
        #With the current ship add it to the list of dicts with all relevant info
        fleet_player.append({"name": name, "coords": coords, "sunk": False})
        #Show the player where it is by printing single board of player 
        print_single_board(player_board, "YOUR WATERS")
        #Add 1 to the index for the next ship to go through this process 
        index += 1

    #loop through the name and size in the allowed ship list
    for name, size in allowed_ships:
        coords = place_ship_random(computer_board, size, n) #Place the ship randomly using other function with relevant info passed through 
        fleet_machine.append({"name": name, "coords": coords, "sunk": False}) #Add dict to the enemy fleet list containing relevant info

    print("\n✅ Fleet deployed. 📡 Enemy armada detected on the horizon.")
    pause("⏎  Press ENTER to commence hostilities...") #Pause until player confirms 

    return boards, fleet_player, fleet_machine #return the boards, and fleet info


def computer_move(boards, stats):
    """
    Simple reasoning for the computer
    - If there are damaged ship cells, target neighboring cells 
    - Otherwise, fire randomly at any open cell
    Args:
        boards (list): list of 4 boards
        stats (dict): current computer game stats
    Returns:
        boards (list): list of 4 current boards
        r,c (tuple): coord of most recent shot
    """
    hidden_player = boards[0]   #players real hidden board
    our_player    = boards[3]   #A mirrored board which is what the computer can see
    n = len(our_player)         #Get board size

    hits = [] 

    for i in range(n):                  #loop through rows and col of board
        for j in range(n):
            if our_player[i][j] == HIT: #If a coord is already hit
                hits.append((i,j))      #Add the index to a list

    target = None
    if hits: #if there are already hit cells 
        candidates = [] 
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)] #list of all adjacent cells to any single cell
        for (r, c) in hits:                            #for the index of each hit
            for (i, j) in neighbors:                   #for the index of each tuple of neighbor coords
                row, col = r + i, c + j                #Have a row and col coord set equal to the neighboring coord index + the given hit cell
                if 0 <= row < n and 0 <= col < n and our_player[row][col] == WATER: #check if the candidate is within board limits and is open water
                    candidates.append((row, col))      #Add the verified candidate to the list
        if candidates:                                 #If candidates found choose a random one from the list to target
            target = random.choice(candidates)

    #If there is no current target (no discoverd ships not yet sunken)
    if target is None:
        spaces = []
        for i in range(n):                  #loop through rows and col of board
            for j in range(n):
                if our_player[i][j] == WATER: #If a coord is free ocean
                    spaces.append((i,j))      #Add the index to a list
        
        if spaces:                         #choose random coord from the list to be targeted
            target = random.choice(spaces)

    r, c = target                 #Get target index
    stats["computer_shots"] += 1  #Add 1 to computer shots counter

    #Verify with the real player board
    if hidden_player[r][c] == SHIP:  #If the target is a ship
        hidden_player[r][c] = HIT    #turn it into a hit cell
        our_player[r][c]    = HIT    #also turn the computer view cell into hit
        stats["computer_hits"] += 1  #Add 1 to computer hits stats counter
        print(f"💥 DIRECT HIT on your fleet at ({r+1},{c+1})! Brace for impact!") #Display message with 1 added to acount for index
    else:                           #If the target is a miss
        hidden_player[r][c] = MISS  #Have it set to the temporary miss in both boards
        our_player[r][c]    = MISS
        print(f"💦 Enemy shell splashes into the sea at ({r+1},{c+1}) — enemy MISSED!") #display message

    return boards, (r, c) #Return the boards list and target coords tuple


def player_move(boards, stats):
    """
    Takes the player input, fires and reports results
    Args:
        boards (list): description
        stats (dict): description
    Returns:
        boards (list): list of 4 current boards
        r,c (tuple): coord of most recent shot
    """
    hidden_computer = boards[1]   #the enemy's real board
    our_computer    = boards[2]   #players radar 
    n = len(our_computer)         #get size

    while True:  #while true loop until valid coord is given
        move = input("🎯 Commander, lock in target (row,column) and FIRE: ") #ask player for target
        try:                               #try except block to catch value errors and restart loop
            row, column = move.split(",")  #use .split to get row and col individually and turn into ints
            row    = int(row)
            column = int(column)
        except ValueError:
            print("🚫 Invalid coordinates. Format: row,column")
            continue

        if row < 1 or row > n or column < 1 or column > n:   #If input outside board limits restart loop
            print(f"🚫 Target out of range! Use 1 to {n}.")
            continue

        r = row - 1       #Convert r and c to 0 based index
        c = column - 1

        #If the chosen cell is not free water then restart loop
        if our_computer[r][c] != WATER:
            print("🚫 This sector has already been engaged. Choose another.")
            continue
        break

    stats["player_shots"] += 1 #Add 1 to play shots in stats dictionary 

    #If the coord is a ship than change to hits on both boards and add 1 to player hits value
    if hidden_computer[r][c] == SHIP:
        hidden_computer[r][c] = HIT
        our_computer[r][c]    = HIT
        stats["player_hits"] += 1 
        print("💥 DIRECT HIT! Enemy vessel taking damage!")
    else:   #if the coord is not a hit then change to miss on both boards
        hidden_computer[r][c] = MISS
        our_computer[r][c]    = MISS
        print("💦 SPLASH! Shot missed, Commander.")

    return boards, (r, c) #return the boards and coord


def check_ships(boards, fleet_player, fleet_machine):
    """
    After each shot checks if any ships have been fully sunk
    If so, update their cells to SUNK and update that ships status 
    in the fleet list to sunk, displays message alerting player of sunken ship
    Args:
        boards (list): list of all 4 boards
        fleet_player (list): list of ship dictionaries 
        fleet_machine (list): list of ship dictionaries 
    Returns:
        none
    """
    #Set all the board types
    hidden_player   = boards[0]
    hidden_computer = boards[1]
    our_computer    = boards[2]
    our_player      = boards[3]

    #Check for the status of each player ship
    for ship in fleet_player: #for each dictionary (a ship)
        if ship["sunk"]:      #If the ship is already checked as sunk then skip
            continue
        #For the other ships assume they are sunk
        is_sunk = True      
        for r, c in ship["coords"]: #Loop through all the ships cells (coords value in dict)
            if hidden_player[r][c] != HIT: #if a cell is not hit 
                is_sunk = False            #Its disproven so end the loop, the ship is still floating
                break       
        if is_sunk:                 #If sunk not proved wrong
            for r, c in ship["coords"]:  #Loop through all the ship cells and set them to sunk in both boards
                hidden_player[r][c] = SUNK
                our_player[r][c] = SUNK
            ship["sunk"] = True      #Update status in dictionary
            print(f"⚠️  EMERGENCY! Your {ship['name']} has been SUNK by the ENEMY! ⚠️")

    # Same check for each computer ship
    for ship in fleet_machine:
        if ship["sunk"]:
            continue
        is_sunk = True 
        for r, c in ship["coords"]:
            if hidden_computer[r][c] != HIT:
                is_sunk = False
                break 
        if is_sunk:
            for r, c in ship["coords"]:
                hidden_computer[r][c] = SUNK
                our_computer[r][c] = SUNK
            ship["sunk"] = True
            print(f"🎖️  ENEMY {ship['name']} DESTROYED! Congratulations, Commander!")


def check_win(fleet_player, fleet_machine):
    """
    Quickly figures out who is the winner, 
    by checking if all ships in a feet are sunk
    Else, returns none and the game goes on 
    Args:
        fleet_player (list): list of ship dictionaries 
        fleet_machine (list): list of ship dictionaries 
    Returns:
        none
    """
    #Use all to check if every item, a given ship, has a sunk bool that is true in the fleet list
    if all(ship["sunk"] for ship in fleet_machine):
        return "player"
    if all(ship["sunk"] for ship in fleet_player):
        return "computer"
    return None


def play_game():
    '''
    This is the main game loop it starts a battle, keeps track of the score,
    and offers a rematch unless the player quits.
    '''        
    clear_screen() #Refresh the screen to erase anything that may be there
    banner()       #print the banner 

    # Ask for the board size only once (reused across rematches)
    size = board_size()

    #We have list of player and computer, so we can refer to index 0 = player and index 1 = computer
    #Starting commander is set to 0 (player)
    #Also set up scores for both
    players        = ["player", "computer"]
    current_player = 0
    player_score   = 0
    computer_score = 0

    #Outer while true loop for one full match which ends when someone loses (battle loop)
    while True:
        clear_screen() #Again clean terminal and print banner at the battle start
        banner()

        # Four boards system for each battle, there are all in boards list
        #   0 = player real ships board
        #   1 = computers's real ships board (hidden from player)
        #   2 = players radar view of the enemy 
        #   3 = computer's view of player (what shots it has taken)
        # Each board is the same size 
        boards = [create_board(size), create_board(size),
                  create_board(size), create_board(size)]

        #We have our boards equal what the choose ship function returns, also the two fleet lists of dictionaries are returned 
        boards, fleet_player, fleet_machine = choose_ships(boards)

        #Create dictionary of game stats 
        #create variables for the most recent shots to later mark them in board
        #create winner and set to none
        stats = {"turn": 0,
                 "player_shots": 0, "player_hits": 0,
                 "computer_shots": 0, "computer_hits": 0}
        last_player_shot   = None
        last_computer_shot = None
        winner = None

        # Inner loop (outer is for battle inner just for each turn)
        # Instead of while true its while there is no winner
        while winner == None:

            #Add 1 to the turn counter of who ever's turn it is
            if players[current_player] == "player":
                stats["turn"] += 1

            # Refresh the screen and print both boards with stats header
            clear_screen()
            banner()
            print_boards(boards, stats, fleet_player, fleet_machine,
                         last_player_shot, last_computer_shot)

            #If the player is the computer add a short pause and have the computer take its move
            if players[current_player] == "computer":
                print("📡 ENEMY COMMANDER is calculating firing solution...")
                time.sleep(1.2)   
                boards, last_computer_shot = computer_move(boards, stats)
            #Else have the player take their move
            else:
                boards, last_player_shot = player_move(boards, stats)

            #Check if the last shot sank a ship to display message if so
            check_ships(boards, fleet_player, fleet_machine)
            #Check if there is a winner
            winner = check_win(fleet_player, fleet_machine)

            #If winner does not equal none, (if theres a winner) break out of loop
            if winner is not None:
                break

            #Call pause function so player decides when to continue game
            pause("⏎  Press ENTER to continue...")
            #Swap the player (will always be 0 or 1)
            current_player = 1 - current_player

        #If loop is broken the match is over so clear screen and print the final boards
        clear_screen()
        banner()
        print_boards(boards, stats, fleet_player, fleet_machine,
                     last_player_shot, last_computer_shot)

        #Depending on who won add to their schore
        if winner == "player":
            print("\n🏆🎖️  VICTORY! You have destroyed the enemy armada, Commander!  🎖️🏆")
            player_score += 1
        else:
            print("\n⚓🔥  DEFEAT! Your fleet has sunk the bottom of the sea...  🔥⚓")
            computer_score += 1

        #Print total scores across matches
        print(f"\n⚓ YOUR SCORE: {player_score}   │   ⚓ ENEMY SCORE: {computer_score}\n")

        #Ask player if they want to play again, if not break out of final loop to end game
        again = input("Press ENTER to rejoin the battle, or 'Q' to surrender: ").strip().lower()
        if again == "q":
            print("\n🌊 Farewell, Commander. Thank you for playing 'B A T T L E S H I P · THE CLASSIC NAVAL COMBAT GAME' 🌊\n")
            break
        #If they want to play again reset player to 0 (player)
        current_player = 0

#Run entire game
play_game()

