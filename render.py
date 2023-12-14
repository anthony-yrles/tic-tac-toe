from globals import *
from grid_creation import *

def render():
    screen.blit(image_bcg, (400,0))
    screen.blit(image_player, (50,70))
    screen.blit(image_select, (200,70))
    screen.blit(image_gris, image_gris_pos)
    screen.blit(image_versus, image_versus_pos)
    screen.blit(image_roux, image_roux_pos)
    screen.blit(image_fight, image_fight_pos)

    grid_creation()