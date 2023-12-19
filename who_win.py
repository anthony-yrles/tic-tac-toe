import pygame

def who_win(cubes, winner, game_over, victories, draws, defeats):
    y_pos = 0
    for x in cubes:
        if sum(x) == 3:
            winner = 1
            game_over = True
            victories += 1
        if sum(x) == -3:
            winner = 2
            game_over = True
            defeats += 1
        if cubes[0][y_pos] + cubes[1][y_pos] + cubes[2][y_pos] == 3:
            winner = 1
            game_over = True
            victories += 1
        if cubes[0][y_pos] + cubes[1][y_pos] + cubes[2][y_pos] == -3:
            winner = 2
            game_over = True
            defeats += 1
        y_pos += 1
    if cubes[0][0] + cubes[1][1] + cubes[2][2] == 3 or cubes[0][2] + cubes[1][1] + cubes[2][0] == 3:
            winner = 1
            game_over = True
            victories += 1
    if cubes[0][0] + cubes[1][1] + cubes[2][2] == 3 or cubes[0][2] + cubes[1][1] + cubes[2][0] == -3:
            winner = 2
            game_over = True
            defeats += 1
    return winner, game_over, victories, defeats

def draw_winner(winner, font, screen, play_again_rect):
     win_text = 'Félicitation joueur ' + str(winner) + ' belle victoire!'
     win_image = font.render(win_text, True, 'red')
     pygame.draw.rect(screen, 'blue', (465, 90, 480, 40))
     screen.blit(win_image, (475, 100))

     again_text = 'Cliquez içi pour rejouer'
     pygame.draw.rect(screen, 'blue', play_again_rect)
     again_image = font.render(again_text, True, 'red')
     screen.blit(again_image, (540, 160))

def reset(cubes, pos, player, winner, human, computer, game_over, easy, medium, hard):
    cubes = []
    pos = []
    player = 1
    winner = 0
    human = False
    computer = False
    game_over = False
    easy = False
    medium = False
    hard = False
    return cubes, pos, player, winner, human, computer, game_over, easy, medium, hard