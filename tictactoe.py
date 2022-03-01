import random

#print the board
#get input
#check result
#switch the player
#checkresult

board = [ 
         "-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"
         ]
current_player = "X"
winner = None
game_running = True


def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print ("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print ("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    
def player_input(board):
    pos = int(input("Choose a position 1 to 9: "))
    if pos >= 1 and pos <=9 and board[pos-1] == "-":
        board[pos-1] = current_player
    else:
        print("position already taken, choose another position ")
        
def check_horizontal(board):
    global winner 
    if board[0] == board[1] == board[2] and board[1] != "-" :
        winner = board[0]
        return True
    
    elif board[3] == board[4] == board[5] and board[4] != "-" : 
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "-" :
        winner = board[6]
        return True
    
def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-" :
        winner = board[0]
        return True
    
    elif board[1] == board[4] == board[7] and board[1] != "-" : 
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-" :
        winner = board[2]
        return True
    
def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-" :
        winner = board[0]
        return True
    
    elif board[2] == board[4] == board[6] and board[2] != "-" : 
        winner = board[2]
        return True
    
def check_tie(board):
    global game_running
    if "-" not in board:
        print_board(board)
        print("It's a tie")
        game_running = False

def check_winner(board):
    global game_running
    if check_horizontal(board) or check_vertical(board) or check_diagonal(board):
        print(f"Winner is {winner}")
        game_running = False
def next_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else: 
        current_player = "X"
        
def smart_guy(board):
    while current_player == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            next_player()
            
while game_running:
    print_board(board)
    player_input(board)
    check_winner(board)
    check_tie(board)
    next_player()
    smart_guy(board)
    check_winner(board)
    check_tie(board)