from globals import *

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
    return None


# def draw_on_grid(symbole, col, row):
#     cell_x = 520 + col * 120
#     cell_y = 220 + row * 120
#     if symbole == 'X':
#         screen.blit(image_pate_gris, (cell_x, cell_y))
#     if symbole == 'O':
#         screen.blit(image_pate_roux, (cell_x, cell_y))

