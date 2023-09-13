def print_board(board):
    for row in board:
        print(" ".join(row))

def check_winner(board, player):
    for row in board:
        if all(mark == player for mark in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    player_idx = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    for _ in range(9):
        print(f"Player {players[player_idx]}'s turn")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if board[row][col] == " ":
            board[row][col] = players[player_idx]
            print_board(board)
            if check_winner(board, players[player_idx]):
                print(f"Player {players[player_idx]} wins!")
                break
            player_idx = 1 - player_idx
        else:
            print("That cell is already occupied. Try again.")

    else:
        print("It's a draw!")

tic_tac_toe()
