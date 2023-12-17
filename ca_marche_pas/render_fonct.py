from globals import *
from grid_creation import grid_creation


def draw_on_grid(symbole, position):
    row, col = position
    cell_x = 520 + col * 120
    cell_y = 220 + row * 120
    if symbole == 'O':
        screen.blit(image_pate_gris, (cell_x, cell_y))       
    if symbole == 'X':
        screen.blit(image_pate_roux, (cell_x, cell_y))