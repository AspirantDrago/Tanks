import pygame
from modules.functions import quit, check_quit_event, load_image
from modules.config import *
from modules.game import game

def menu(screen):
    image = load_image(FN_IMAGE_MENU_BACK)
    screen.blit(image, (0, 0))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            check_quit_event(event)
            if event.type == pygame.KEYDOWN:
                game(screen)
