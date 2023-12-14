import pygame as Py
from globals import *

def grid_creation():
    for i in range(0, 4):
        for j in range (0, 4):
            Py.draw.line(screen, 'black', (520 + i * 120, 220), (520 + i * 120, 220 + j * 120), 3)
            Py.draw.line(screen, 'black', (520, 220 + i * 120), (520 + j * 120, 220 + i * 120), 3)

