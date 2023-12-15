from globals import *
from grid_creation import grid_creation

# def fight_render(chat_gris, chat_roux):
#     if chat_gris == True or chat_roux == True:
#         screen.blit(image_fight, image_fight_pos)

# def grid_render(fight_on):
#     if fight_on == True:
#         grid_creation()

def draw_on_grid(symbole, position, chat_gris, chat_roux, fight_on):
    row, col = position
    cell_x = 520 + col * 120
    cell_y = 220 + row * 120
    if symbole == 'X':
        screen.blit(image_pate_gris, (cell_x, cell_y))
    if symbole == 'O':
        screen.blit(image_pate_roux, (cell_x, cell_y))