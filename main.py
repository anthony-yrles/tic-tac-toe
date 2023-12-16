"""

"""

import pygame as Py
from render import *
from event import *
from resolution import *

Py.init()
continuer = True
chat_gris = False
chat_roux = False
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
            position = mouse_pos()
            symbole = verification_case(position, grid, chat_gris, chat_roux)
            if symbole:
                chat_gris, chat_roux = chat_roux, chat_gris

    render(symbole, position, grid)
    if est_victoire(grid, symbole):
        victory(chat_gris, chat_roux)
        chat_gris = False
        chat_roux = False
        grid = [[' ' for _ in range(3)] for _ in range(3)]
        symbole = ' '
        position = [0, 0]
    Py.display.flip()


        