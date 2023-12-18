from who_win import *
from medium import get_empty_cells

def minimax(board, depth, maximizing_player):
    winner, game_over = who_win(board, 0, False)

    if game_over or depth == 0:
        return 0 if winner == 0 else (10 if winner == 1 else -10)

    empty_cells = get_empty_cells(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in empty_cells:
            temp_board = [row.copy() for row in board]
            temp_board[move[0]][move[1]] = -1
            eval = minimax(temp_board, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in empty_cells:
            temp_board = [row.copy() for row in board]
            temp_board[move[0]][move[1]] = 1
            eval = minimax(temp_board, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval