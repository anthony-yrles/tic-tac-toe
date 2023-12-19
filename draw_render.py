import pygame

def draw_render(screen, image_bcg, image_fight, image_vs_player, image_vs_cpu, image_opponent, image_difficulty, image_easy, image_medium, image_hard, image_player, font, user_text, input_in, enter, victories, draws, defeats):
    screen.blit(image_bcg, (400,0))
    screen.blit(image_fight, (100,30))
    screen.blit(image_opponent, (50,260))
    screen.blit(image_vs_player, (80,310))
    screen.blit(image_vs_cpu, (80,350))
    screen.blit(image_difficulty, (100,440))
    screen.blit(image_easy, (10, 500))
    screen.blit(image_medium, (140, 500))
    screen.blit(image_hard, (270, 500))
    if enter == False:
        screen.blit(image_player, (550, 20))
        if input_in == True:
            text_surface = font.render(user_text, True, 'black')
            pygame.draw.rect(screen, 'blue', (550, 75, 200, 35))
            screen.blit(text_surface, (555, 80))
    else:
        text_surface = font.render(f'Bienvenue {user_text}', True, 'black')
        screen.blit(text_surface, (555, 10))
        records_surface = font.render(f'Victoire: {victories} / Nul: {draws} / Défaites: {defeats}', True, 'black')
        screen.blit(records_surface, (500, 50))