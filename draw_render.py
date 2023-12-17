import pygame

def draw_render(screen, image_bcg, image_fight, image_vs_player, image_vs_cpu, image_opponent, image_difficulty, image_easy, image_medium, image_hard):
    screen.blit(image_bcg, (400,0))
    screen.blit(image_fight, (100,30))
    screen.blit(image_opponent, (50,260))
    screen.blit(image_vs_player, (80,310))
    screen.blit(image_vs_cpu, (80,350))
    screen.blit(image_difficulty, (100,440))
    screen.blit(image_easy, (10, 500))
    screen.blit(image_medium, (140, 500))
    screen.blit(image_hard, (270, 500))