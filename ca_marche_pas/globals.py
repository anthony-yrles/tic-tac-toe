import pygame as Py

screen = Py.display.set_mode((1000, 600))
render1 = True

image_bcg = Py.image.load('./assets/images/bcg_image.jpg').convert_alpha()
image_select = Py.image.load('./assets/images/select.jpg').convert_alpha()
image_select_pos = (50,30)
image_player = Py.image.load('./assets/images/player.jpg').convert_alpha()
image_player_pos = (200,30)
image_versus = Py.image.load('./assets/images/versus_bis.png').convert_alpha()
image_versus_pos = (90,80)
image_gris = Py.image.load('./assets/images/chat_gris_bis.jpg').convert_alpha()
image_gris_pos = (20,80)
image_roux = Py.image.load('./assets/images/chat_roux_bis.jpg').convert_alpha()
image_roux_pos = (250,80)
image_fight = Py.image.load('./assets/images/fight.png').convert_alpha()
image_fight_pos = (580,10)
image_pate_gris = Py.image.load('./assets/images/pate_gris.png').convert_alpha()
image_pate_roux = Py.image.load('./assets/images/pate_roux.png').convert_alpha()
image_opponent = Py.image.load('./assets/images/opponent.png').convert_alpha()
image_opponent_pos = (50,260)
image_vs_player = Py.image.load('./assets/images/vs_player.png').convert_alpha()
image_vs_player_pos = (80,310)
image_vs_cpu = Py.image.load('./assets/images/vs_cpu.png').convert_alpha()
image_vs_cpu_pos = (80,350)
image_difficulty = Py.image.load('./assets/images/select_difficulty.png').convert_alpha()
image_difficulty_pos = (100,440)
image_easy = Py.image.load('./assets/images/easy_bis.png').convert_alpha()
image_easy_pos = (10, 500)
image_medium = Py.image.load('./assets/images/medium_bis.png').convert_alpha()
image_medium_pos = (140, 500)
image_hard = Py.image.load('./assets/images/hard_bis.jpg').convert_alpha()
image_hard_pos = (270, 500)