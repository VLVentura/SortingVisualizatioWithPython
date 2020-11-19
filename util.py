import pygame

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 780

BAR_SIZE = 20
N_BARS = WINDOW_WIDTH // BAR_SIZE

def text_object(pos, text, size, color):
    font = pygame.font.SysFont('freemono', size, True)

    txt = font.render(text, 1, color)
    rect = txt.get_rect()
    rect.center = pos

    return (txt, rect)