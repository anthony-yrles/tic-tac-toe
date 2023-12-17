import pygame

def draw_image(cubes, screen, image_pate_gris, image_pate_roux):
    x_pos = 0
    for x in cubes:
        y_pos = 0
        for y in x:
            if y == 1:
                screen.blit(image_pate_gris, (520 + x_pos * 120, 220 + y_pos * 120))
            if y == -1:
                screen.blit(image_pate_roux, (520 + x_pos * 120, 220 + y_pos * 120))
            y_pos +=1
        x_pos +=1
