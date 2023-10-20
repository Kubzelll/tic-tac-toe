'''
$$\   $$\          $$\                           $$\ 
$$ | $$  |         $$ |                          $$ |
$$ |$$  /$$\   $$\ $$$$$$$\  $$$$$$$$\  $$$$$$\  $$ |
$$$$$  / $$ |  $$ |$$  __$$\ \____$$  |$$  __$$\ $$ |
$$  $$<  $$ |  $$ |$$ |  $$ |  $$$$ _/ $$$$$$$$ |$$ |
$$ |\$$\ $$ |  $$ |$$ |  $$ | $$  _/   $$   ____|$$ |
$$ | \$$\\$$$$$$  |$$$$$$$  |$$$$$$$$\ \$$$$$$$\ $$ |
\__|  \__|\______/ \_______/ \________| \_______|\__|
'''
def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_win(board):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return True
    for i in range(0, 3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return True
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True
    return False

def tic_tac_toe():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player = "X"
    while not check_win(board):
        print_board(board)
        print("Player " + player + "'s turn.")
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] == " ":
            board[move] = player
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("Invalid move. Please try again.")
    print_board(board)
    print("Player " + player + " wins!")


if __name__ == "__main__":
    tic_tac_toe()
