import pygame as Py

screen = Py.display.set_mode((1000, 600))

image_bcg = Py.image.load('./assets/images/bcg_image.jpg').convert_alpha()
image_select = Py.image.load('./assets/images/select.jpg').convert_alpha()
image_player = Py.image.load('./assets/images/player.jpg').convert_alpha()
image_gris = Py.image.load('./assets/images/chat_gris.jpg').convert_alpha()
image_roux = Py.image.load('./assets/images/chat_roux.jpg').convert_alpha()
image_versus = Py.image.load('./assets/images/versus.png').convert_alpha()
image_fight = Py.image.load('./assets/images/fight.png').convert_alpha()