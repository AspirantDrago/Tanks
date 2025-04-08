import pygame

from modules.config import *
from modules.intro import intro
from modules.menu import menu
from modules.game import game
from modules.functions import quit, load_image


pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(NAME)
pygame.display.set_icon(load_image(FN_ICON))
intro(screen)
# menu(screen)
game(screen)
quit()
