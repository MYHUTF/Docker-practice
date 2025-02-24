#!/usr/bin/env python3

def print_board(board):
    print("\n")
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def tic_tac_toe():
    board = [' ']*9
    current_player = 'X'
    for turn in range(9):
        print_board(board)
        move = input("Player {}: Enter your move (1-9): ".format(current_player))
        try:
            move = int(move) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")
            continue

        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print("Player {} wins!".format(current_player))
            return

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

    print_board(board)
    print("It's a draw!")

if __name__ == '__main__':
    tic_tac_toe()

