"""

"""

import pygame as Py
from globals import *
from render import *

Py.init()

continuer = True

while continuer:
    render()
    for event in Py.event.get():
        if event.type == Py.QUIT:
            continuer = False
    Py.display.flip()
        