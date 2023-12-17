"""

"""

import pygame as Py
from render import *
from event import *
from resolution import *
from ia import *

Py.init()
continuer = True
chat_gris = False
chat_roux = False
human = False
computer = False
human_turn = True
computer_turn = False
grid = [[' ' for _ in range(3)] for _ in range(3)]  # Matrice pour les symboles
symbole = ' '
position = [0, 0]

while continuer:
    for event in Py.event.get():
        if event.type == Py.QUIT:
            continuer = False
        elif event.type == Py.MOUSEBUTTONDOWN:
            chat_gris = gris_ou_roux(event, chat_gris, chat_roux)
            chat_roux = roux_ou_gris(event, chat_gris, chat_roux)
            human = choice_human(event, human, computer, chat_gris, chat_roux)
            computer = choice_computer(event, computer, human, chat_gris, chat_roux)
            if human:
                position = mouse_pos()
                symbole = verification_case(position, grid, chat_gris, chat_roux)
                print(symbole)
                chat_gris, chat_roux = chat_roux, chat_gris
            
            if computer:
                if human_turn:
                    position = mouse_pos()
                    joueur_symbole = verification_case(position, grid, chat_gris, chat_roux)
                    if joueur_symbole:
                        symbole = joueur_symbole
                    human_turn = False
                    computer_turn = True
                if computer_turn:
                    result = ia(grid, symbole, chat_gris, chat_roux)
                    if result:
                        signe, row, col = result
                        position = row, col
                    human_turn = True
                    computer_turn = False

    render(symbole, position, grid)
    if est_victoire(grid, symbole):
        victory(chat_gris, chat_roux)
        chat_gris = False
        chat_roux = False
        human = False
        computer = False
        grid = [[' ' for _ in range(3)] for _ in range(3)]
        symbole = ' '
        position = [0, 0]
    Py.display.flip()


        