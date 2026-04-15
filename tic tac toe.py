# Create an empty board with positions 1-9
board = [" " for _ in range(9)]

# Function to display the board
def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

# Function to check if someone has won
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check for draw
def check_draw():
    return " " not in board  # no empty spaces left

# Main game function
def play_game():
    current_player = "X"
    
    while True:
        display_board()
        
        # Take input from player
        try:
            move = int(input(f"Player {current_player}, choose position (1-9): ")) - 1
            
            # Validate input range
            if move < 0 or move > 8:
                print("Invalid position. Choose between 1 and 9.")
                continue
            
            # Check if position is already taken
            if board[move] != " ":
                print("Position already taken. Try again.")
                continue
            
            # Place the move
            board[move] = current_player
            
            # Check if current player wins
            if check_winner(current_player):
                display_board()
                print(f"Player {current_player} wins!")
                break
            
            # Check for draw
            if check_draw():
                display_board()
                print("It's a draw!")
                break
            
            # Switch player
            current_player = "O" if current_player == "X" else "X"
        
        except ValueError:
            print("Please enter a number between 1 and 9.")

# Start the game
play_game()