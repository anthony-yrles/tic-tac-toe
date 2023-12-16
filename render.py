from globals import *
from render_fonct import *
from resolution import est_victoire

def render(symbole, position, grid):
    global render1
    if render1: 
        screen.blit(image_bcg, (400,0))
        screen.blit(image_player, (50,70))
        screen.blit(image_select, (200,70))
        screen.blit(image_gris, image_gris_pos)
        screen.blit(image_versus, image_versus_pos)
        screen.blit(image_roux, image_roux_pos)
        screen.blit(image_fight, image_fight_pos)
        render1 = False
    grid_creation()
    if position is not None:
        draw_on_grid(symbole, position)
    if est_victoire(grid, symbole):
        render1 = True
