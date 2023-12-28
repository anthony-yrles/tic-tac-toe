import pygame
import random
from draw_render import *
from who_win import *
from medium import *
from hard import *
from save_json import *
from event import *

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("tic-tac-toe")
image_bcg = pygame.image.load('./assets/images/bcg_image.jpg').convert_alpha()
image_fight = pygame.image.load('./assets/images/fight.png').convert_alpha()
image_pate_gris = pygame.image.load('./assets/images/pate_gris.png').convert_alpha()
image_pate_roux = pygame.image.load('./assets/images/pate_roux.png').convert_alpha()
image_vs_player = pygame.image.load('./assets/images/vs_player.png').convert_alpha()
image_vs_player_pos = (80,310)
vs_player_rect = pygame.Rect(80, 310, 240, 35)
image_vs_cpu = pygame.image.load('./assets/images/vs_cpu.png').convert_alpha()
image_vs_cpu_pos = (80,350)
vs_cpu_rect = pygame.Rect(80, 350, 240, 35)
image_opponent = pygame.image.load('./assets/images/opponent.png').convert_alpha()
image_difficulty = pygame.image.load('./assets/images/select_difficulty.png').convert_alpha()
image_easy = pygame.image.load('./assets/images/easy_bis.png').convert_alpha()
image_easy_pos = (10, 500)
vs_easy_rect = pygame.Rect(10, 500, 120, 80)
image_medium = pygame.image.load('./assets/images/medium_bis.png').convert_alpha()
image_medium_pos = (140, 500)
vs_medium_rect = pygame.Rect(140, 500, 120, 80)
image_hard = pygame.image.load('./assets/images/hard_bis.jpg').convert_alpha()
image_hard_pos = (270, 500)
vs_hard_rect = pygame.Rect(270, 500, 120, 80)
image_player = pygame.image.load('./assets/images/gamer.jpg').convert_alpha()
image_player_pos =(550, 20)
player_rect = pygame.Rect(550, 20, 300, 56)
font = pygame.font.SysFont(None, 40)
play_again_rect = pygame.Rect(530, 150, 345, 40)
user_text = ''

cubes = []
clicked = False
pos = []
player = 1
winner = 0
human = False
computer = False
easy = False
medium = False
hard = False
game_over = False
input_in = False
enter = False
victories = 0
draws = 0
defeats = 0

for x in range(3):
    row = [0] * 3
    cubes.append(row)

continuer = True
while continuer:
    draw_render(screen, image_bcg, image_fight, image_vs_player, image_vs_cpu, image_opponent, image_difficulty, image_easy, image_medium, image_hard, image_player, font, user_text, input_in, enter, victories, draws, defeats)
    draw_image(cubes, screen, image_pate_gris, image_pate_roux)
    draw_grid(screen)
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
                test_colliding = colliding(vs_player_rect, vs_cpu_rect, vs_easy_rect, vs_medium_rect, vs_hard_rect, player_rect, pos, human, computer, easy, medium, hard, input_in)
                human, computer, easy, medium, hard, input_in = test_colliding
                if human:
                    if x >= 520 and x <= 880 and y >= 220 and y <= 700:
                        if cubes[(x - 520) // 120][(y - 220) // 120] == 0:
                            cubes[(x - 520) // 120][(y - 220) // 120] = player
                            end_game = who_win(cubes, winner, game_over, victories, draws, defeats)
                            winner, game_over, victories, defeats = end_game
                            save_user(user_text, victories, draws, defeats)
                            player *= -1
                if computer and player == 1:
                    if x >= 520 and x <= 880 and y >= 220 and y <= 700:
                        if cubes[(x - 520) // 120][(y - 220) // 120] == 0:
                            cubes[(x - 520) // 120][(y - 220) // 120] = player
                            player *= -1
                            end_game = who_win(cubes, winner, game_over, victories, draws, defeats)
                            winner, game_over, victories, defeats = end_game
                            save_user(user_text, victories, draws, defeats)
            if event.type == pygame.KEYDOWN:
                if len(user_text) < 12:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        save_user(user_text, victories, draws, defeats)
                        input_in = False
                        enter = True
                    else:
                        user_text += event.unicode
    if computer and easy and player == -1:
        empty_cells = get_empty_cells(cubes)
        if empty_cells:
            computer_move = random.choice(empty_cells)
            cubes[computer_move[0]][computer_move[1]] = player
            player *= -1
            end_game = who_win(cubes, winner, game_over, victories, draws, defeats)
            winner, game_over, victories, defeats = end_game
            save_user(user_text, victories, draws, defeats)

    if computer and medium and player == -1:
        empty_cells = get_empty_cells(cubes)
        for move in empty_cells:
            if is_winner_move(cubes, move, player, victories, draws, defeats):
                cubes[move[0]][move[1]] = player
                player *= -1
                end_game = who_win(cubes, winner, game_over, victories, draws, defeats)
                winner, game_over, victories, defeats = end_game
                save_user(user_text, victories, draws, defeats)
                break
        else:
            computer_move = random.choice(empty_cells)
            cubes[computer_move[0]][computer_move[1]] = player
            player *= -1
            end_game = who_win(cubes, winner, game_over, victories, draws, defeats)
            winner, game_over, victories, defeats = end_game
            save_user(user_text, victories, draws, defeats)

    if computer and hard and player == -1:
        empty_cells = get_empty_cells(cubes)

        best_move = None
        best_eval = float('-inf')

        for move in empty_cells:
            temp_board = [row.copy() for row in cubes]
            temp_board[move[0]][move[1]] = player

            eval = minimax(temp_board, 2, False, victories, draws, defeats)

            if eval > best_eval:
                best_eval = eval
                best_move = move

        cubes[best_move[0]][best_move[1]] = player
        player *= -1
        end_game = who_win(cubes, winner, game_over, victories, draws, defeats)
        winner, game_over, victories, defeats = end_game
        save_user(user_text, victories, draws, defeats)


    if game_over == True:
        draw_winner(winner, font, screen, play_again_rect)
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
        if play_again_rect.collidepoint(pos):
            reset_game = reset(cubes, pos, player, winner, human, computer, game_over, easy, medium, hard, victories, draws, defeats)
            cubes, pos, player, winner, human, computer, game_over, easy, medium, hard, victories, draws, defeats = reset_game
            for x in range(3):
                row = [0] * 3
                cubes.append(row)
            pygame.Surface.fill(screen, (0,0,0))

    pygame.display.update()
pygame.quit()