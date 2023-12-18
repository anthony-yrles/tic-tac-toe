import pygame

def input_player(image_player, image_player_pos, event, input_in):
    if image_player_pos[0] <= event.pos[0] <= image_player_pos[0] + image_player.get_width() and \
        image_player_pos[1] <= event.pos[1] <= image_player_pos[1] + image_player.get_height():
        input_in = True
        return input_in