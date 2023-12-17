import pygame
import random
from pygame.locals import *
from draw_grid import *
from draw_image import *
from draw_render import *
from who_win import *

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("tic-tac-toe")
image_bcg = pygame.image.load('./assets/images/bcg_image.jpg').convert_alpha()
image_fight = pygame.image.load('./assets/images/fight.png').convert_alpha()
image_pate_gris = pygame.image.load('./assets/images/pate_gris.png').convert_alpha()
image_pate_roux = pygame.image.load('./assets/images/pate_roux.png').convert_alpha()
image_vs_player = pygame.image.load('./assets/images/vs_player.png').convert_alpha()
image_vs_player_pos = (80,310)
image_vs_cpu = pygame.image.load('./assets/images/vs_cpu.png').convert_alpha()
image_vs_cpu_pos = (80,350)
image_opponent = pygame.image.load('./assets/images/opponent.png').convert_alpha()
image_difficulty = pygame.image.load('./assets/images/select_difficulty.png').convert_alpha()
image_easy = pygame.image.load('./assets/images/easy_bis.png').convert_alpha()
image_medium = pygame.image.load('./assets/images/medium_bis.png').convert_alpha()
image_hard = pygame.image.load('./assets/images/hard_bis.jpg').convert_alpha()
font = pygame.font.SysFont(None, 40)
play_again_rect = pygame.Rect(530, 150, 345, 40)

cubes = []
clicked = False
pos = []
player = 1
winner = 0
human = False
computer = False
game_over = False

for x in range(3):
    row = [0] * 3
    cubes.append(row)

continuer = True
while continuer:
    draw_render(screen, image_bcg, image_fight, image_vs_player, image_vs_cpu, image_opponent, image_difficulty, image_easy, image_medium, image_hard)
    draw_grid(screen)
    draw_image(cubes, screen, image_pate_gris, image_pate_roux)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        if game_over == False:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                if image_vs_player_pos[0] <= event.pos[0] <= image_vs_player_pos[0] + image_vs_player.get_width() and \
        image_vs_player_pos[1] <= event.pos[1] <= image_vs_player_pos[1] + image_vs_player.get_height() and computer == False:
                    human = True
                if image_vs_cpu_pos[0] <= event.pos[0] <= image_vs_cpu_pos[0] + image_vs_cpu.get_width() and \
        image_vs_cpu_pos[1] <= event.pos[1] <= image_vs_cpu_pos[1] + image_vs_cpu.get_height() and human == False:
                    computer = True
                if human:
                    if x >= 520 and x <= 880 and y >= 220 and y <= 700:
                        if cubes[(x - 520) // 120][(y - 220) // 120] == 0:
                            cubes[(x - 520) // 120][(y - 220) // 120] = player
                            player *= -1
                            end_game = who_win(cubes, winner, game_over)
                            winner, game_over = end_game
                if computer and player == 1:
                    if x >= 520 and x <= 880 and y >= 220 and y <= 700:
                        if cubes[(x - 520) // 120][(y - 220) // 120] == 0:
                            cubes[(x - 520) // 120][(y - 220) // 120] = player
                            player *= -1
                            end_game = who_win(cubes, winner, game_over)
                            winner, game_over = end_game
    if computer and player == -1:
        empty_cells = [(i, j) for i in range(3) for j in range(3) if cubes[i][j] == 0]
        if empty_cells:
            computer_move = random.choice(empty_cells)
            cubes[computer_move[0]][computer_move[1]] = player
            player *= -1
            end_game = who_win(cubes, winner, game_over)
            winner, game_over = end_game


    if game_over == True:
        draw_winner(winner, font, screen, play_again_rect)
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if play_again_rect .collidepoint(pos):
                reset_game = reset(cubes, pos, player, winner, human, computer, game_over)
                cubes, pos, player, winner, human, computer, game_over = reset_game
                for x in range(3):
                    row = [0] * 3
                    cubes.append(row)
                pygame.Surface.fill(screen, (0,0,0))

    pygame.display.update()
pygame.quit()