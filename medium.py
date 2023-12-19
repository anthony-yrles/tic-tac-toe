from who_win import *

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

def is_winner_move(board, move, player, victories, draws, defeats):
    temp_board = [row.copy() for row in board]
    temp_board[move[0]][move[1]] = player
    return who_win(temp_board, 0, False, victories, draws, defeats)[1] == True