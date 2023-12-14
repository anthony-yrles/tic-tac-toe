"""

"""

import pygame as Py
from render import *
from event import *

Py.init()

continuer = True
chat_gris = False
chat_roux = False

while continuer:
    render()
    for event in Py.event.get():
        if event.type == Py.QUIT:
            continuer = False
        elif event.type == Py.MOUSEBUTTONDOWN:
            chat_gris = gris_ou_roux(event, chat_gris, chat_roux)
            chat_roux = roux_ou_gris(event, chat_gris, chat_roux)
            fight(event, chat_gris, chat_roux, fight_on)
            position = mouse_pos()
    Py.display.flip()


        