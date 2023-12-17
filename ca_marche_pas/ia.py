from globals import *

def ia(board, signe, chat_gris, chat_roux):
    if chat_gris == True:
        signe = 'O'
    elif chat_roux == True:
        signe = 'X'

    # Recherche d'une case vide pour jouer
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = signe
                return signe, row, col

    # Si aucune case vide n'est trouvée, renvoyer False ou faire quelque chose d'autre
    return False


