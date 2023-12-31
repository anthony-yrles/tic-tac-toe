import pygame

def colliding(vs_player_rect, vs_cpu_rect, vs_easy_rect, vs_medium_rect, vs_hard_rect, player_rect, pos, human, computer, easy, medium, hard, input_in):
    if vs_player_rect.collidepoint(pos) and computer == False:
        human = True
    if vs_cpu_rect.collidepoint(pos) and human == False:
        computer = True
    if vs_easy_rect.collidepoint(pos) and human == False and medium == False and hard == False:
        easy = True
    if vs_medium_rect.collidepoint(pos) and human == False and easy == False and hard == False:
        medium = True
    if vs_hard_rect.collidepoint(pos) and human == False and easy == False and medium == False:
        hard = True
    if player_rect.collidepoint(pos):
        input_in = True
    return human, computer, easy, medium, hard, input_in