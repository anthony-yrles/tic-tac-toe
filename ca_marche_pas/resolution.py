from globals import *
from tkinter import messagebox as mb
import time

def verification_case(position, grid, chat_gris, chat_roux):
    if position is not None:
        row, col = position
        if grid[row][col] == ' ':
            if chat_gris:
                grid[row][col] = 'X'
                return 'X'
            elif chat_roux:
                grid[row][col] = 'O'
                return 'O'

def est_victoire(grid, symbole):
    if symbole != ' ':
        for i in range(3):
                if all(grid[i][j] == symbole for j in range(3)) or all(grid[j][i] == symbole for j in range(3)):
                    return True
        if all(grid[i][i] == symbole for i in range(3)) or all(grid[i][2 - i] == symbole for i in range(3)):
            return True
    return False

def victory(chat_gris, chat_roux):
    if chat_gris:
        message = "Bravo ! Le joueur Mistigry a gagné !"
        time.sleep(0.5)
        mb.showinfo("Partie terminée", message)
        
    elif chat_roux:
        message = "Bravo ! Le joueur Roucky a gagné !"
        time.sleep(0.5)
        mb.showinfo("Partie terminée", message)



