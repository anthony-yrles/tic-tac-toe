import pygame

def draw_grid(screen):
    for x in range(0,4):
        pygame.draw.line(screen, "white", (520 + x * 120, 220), (520 + x * 120, 220 + 120 * 3), 3)
        pygame.draw.line(screen, "white", (520, 220 + x * 120), (520 + 120 * 3, 220 + x * 120), 3)